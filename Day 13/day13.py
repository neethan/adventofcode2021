import re
import numpy as np
from pprint import pprint as pp
from collections import defaultdict
from math import floor

def getInput():
	with open("input.txt") as fp:
		lines = []
		commands = []
		swap = False
		for x in fp.readlines():
			x = x.strip()
			if x == "":
				swap = True
				continue
			commands.append(x) if swap else lines.append(x)
		return lines, commands

def papersize(coords, idx):
	_max = -1
	for c in coords:
		if c[idx] > _max: _max = c[idx]
	return _max + 1

coords, cmds = getInput()
coords = [list(map(int, i)) for i in [x.split(",") for x in coords]]
paper_y = papersize(coords, 1)
paper_x = papersize(coords, 0)
paper = np.zeros((paper_y, paper_x))

for coord in coords:
	x, y = coord
	paper[y][x] = 1

for cmd in cmds:
	direction, value = cmd.strip("fold along ").split("=")
	direction = 1 if direction == "x" else 0
	value = int(value)

	paper, paper_flip = np.split(np.delete(paper, value, direction), 2, direction)

	if direction:
		paper_x = floor(paper_x / 2)

		for fr_x, bk_x in zip(range(0, paper_x), range(paper_x - 1, -1, -1)):
			for y in range(0, paper_y):
				paper[y][fr_x] = int(paper[y][fr_x]) | int(paper_flip[y][bk_x])
	else:
		paper_y = floor(paper_y / 2)

		for fr_y, bk_y in zip(range(0, paper_y), range(paper_y - 1, -1, -1)):
			for x in range(0, paper_x):
				paper[fr_y][x] = int(paper[fr_y][x]) | int(paper_flip[bk_y][x])

	print(np.sum(paper))
	np.clip(paper, a_min=0, a_max=1, out=paper)
	break