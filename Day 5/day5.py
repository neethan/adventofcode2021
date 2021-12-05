import re
import pprint
import numpy as np

size = 5

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		return lines

def createMatrix(data):
	# Replace newlines and things with commas
	sides = [x.replace("\n", "").replace(" -> ", ",").split(",") for x in data]
	# Put into a single list of values
	vals = [int(x) for y in sides for x in y]
	# Return array with values
	return np.zeros((max(vals) + 1, max(vals) + 1))

lines = getInput()
initalMatrix = createMatrix(lines)

for row in lines:
	# Split into x1, x2, y1, y2
	p1, p2 = row.split(" -> ")
	x1, y1 = [int(x) for x in p1.split(",")]
	x2, y2 = [int(x.strip()) for x in p2.split(",")]
	if x1 == x2:
		for y in range(min(y1, y2), max(y1, y2) + 1):
			initalMatrix[y][x1] += 1
	elif y1 == y2:
		for x in range(min(x1, x2), max(x1, x2) + 1):
			initalMatrix[y1][x] += 1
	else:
		# Calc direction to draw and go through
		x_dir = 1 if x1 < x2 else -1
		y_dir = 1 if y1 < y2 else -1
		x = x1
		y = y1
		for i in range(0, abs(x1 - x2) + 1):
			initalMatrix[y][x] += 1
			x += x_dir
			y += y_dir

number = (initalMatrix > 1).sum()	
print(number)