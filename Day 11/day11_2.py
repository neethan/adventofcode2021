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

def increase(y, x):
	global data
	global flashed
	global flashes

	if y >= w or y < 0 or x >= h or x < 0:
		return

	if flashed[y][x] == 0:
		data[y][x] += 1

	if data[y][x] == 10:
		data[y][x] = 0

		flashes += 1
		flashed[y][x] = 1

		increase(y + 1, x)
		increase(y - 1, x)
		increase(y, x + 1)
		increase(y, x - 1)
		increase(y - 1, x - 1)
		increase(y - 1, x + 1)
		increase(y + 1, x - 1)
		increase(y + 1, x + 1)

steps = 2000
data = np.array(getInput())

w = data.shape[1]
h = data.shape[0]

flashes = 0
flashed = np.zeros((h, w))

for i in range(0, steps):
	for y in range(0, h):
		for x in range(0, w):
			increase(y, x)
	
	if np.amax(flashed) == np.amin(flashed) > 0:
		print(i + 1)
		break

	flashed = np.zeros((h, w))
