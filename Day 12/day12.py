import re
import numpy as np
from pprint import pprint as pp
from collections import defaultdict

def getInput():
	with open("input.txt") as fp:
		lines = [x.strip() for x in fp.readlines()]
		return lines

def findRoutes(idx, caves, currentRoute, routes):
	#print("  " * len(currentRoute), "Now on:", currentRoute, " - ", idx, " - ", caves[idx])
	if idx == "end":
		#print("  " * len(currentRoute), "Added")
		routes.append(currentRoute)
		return
	

	# Check all these children for their paths
	for cave in caves[idx]:
		#print("  " * len(currentRoute), "-> Attempting", cave)
		# Try this path on the current path
		newRoute = currentRoute.copy()
		newRoute.append(cave)

		# If we visit a small twice, don't do this path
		checkDupes = [x for x in newRoute if x == x.lower() and len(x) < 3]
		# Part 2 on this line
		if len(checkDupes) != len(set(checkDupes)) and abs(len(checkDupes) - len(set(checkDupes))) == 2:
			#print("  " * len(newRoute), "-> Dupe! Continue... (", cave, ")")
			continue

		#print("  " * len(newRoute), "-> Looking for routes under", cave)
		route = findRoutes(cave, caves.copy(), newRoute, routes)

cavesConnections = np.array(getInput())
caves = {}
for connection in cavesConnections:
	start, end = connection.split("-")

	if not start in caves:
		caves[start] = []
	if not end in caves:
		caves[end] = []

	if start != "end" or end != "start":
		caves[start].append(end)
	if (start != "start" and end != "end"):
		caves[end].append(start)
	if "start" in caves[start]: caves[start].remove("start")
	if "start" in caves[end]: caves[end].remove("start")


routes = []

findRoutes("start", caves.copy(), [], routes)
print(len(routes))