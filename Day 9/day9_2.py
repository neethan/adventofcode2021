import re
import numpy as np

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		output = []
		for line in lines:
			splitted = [int(x) for x in line.strip()]
			output.append(splitted)
		return output

def checkBasin(y, x):
	global basin

	if basinused[y][x] == 1 or data[y][x] == 9:
		if data[y][x] == 9:
			basinused[y][x] = 1
		return None	

	basinused[y][x] = 1

	above = None if y == 0 else checkBasin(y - 1, x)
	below = None if y >= h - 1 else checkBasin(y + 1, x)
	left = None if x == 0 else checkBasin(y, x - 1)
	right = None if x >= w - 1 else checkBasin(y, x + 1)

	tests = [x for x in [above, below, left, right] if x != None]

	if not tests:
		basin.append(data[y][x])
		return True
	else:
		if above != None and basinused[y - 1][x] != 1: basin.append(data[y - 1][x])
		if below != None and basinused[y + 1][x] != 1: basin.append(data[y + 1][x])
		if left != None and basinused[y][x - 1] != 1: basin.append(data[y][x - 1])
		if right != None and basinused[y][x + 1] != 1: basin.append(data[y][x + 1])
		basin.append(data[y][x])
		return True

data = np.array(getInput())
w = data.shape[1]
h = data.shape[0]
basinused = np.zeros((h, w))
basins = []
basin = []

for y in range(0, h):
	for x in range(0, w):
		if basinused[y][x] == 1:
			continue
		else:
			checkBasin(y, x)
			if basin:
				basins.append(len(basin))
				basin = []

print(np.prod(sorted(basins)[-3:]))