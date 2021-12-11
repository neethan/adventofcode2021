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

data = np.array(getInput())
w = data.shape[1]
h = data.shape[0]
lowpoints = []

for y in range(0, h):
	for x in range(0, w):
		above = None if y == 0 else data[y - 1][x]
		below = None if y >= h - 1 else data[y + 1][x]
		left = None if x == 0 else data[y][x - 1]
		right = None if x >= w - 1 else data[y][x + 1]

		tests = [x for x in [above, below, left, right] if x != None]
		if all(i > data[y][x] for i in tests):
			lowpoints.append(1 + data[y][x])
		 
print(sum(lowpoints))