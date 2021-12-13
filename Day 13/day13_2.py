import re
import numpy as np
from pprint import pprint as pp
from collections import defaultdict
from math import floor

import colorama
def color_sign(x):
    c = colorama.Fore.GREEN if x > 0 else colorama.Fore.BLACK
    return f'{c}{x}'

np.set_printoptions(edgeitems=30, linewidth=100000, formatter={'float': color_sign})

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
	paper = np.delete(paper, value, direction)

	paper, paper_flip = np.array_split(paper, [value], direction)

	if direction:
		paper_x = paper.shape[1]
		paper_flip_x = paper_flip.shape[1]

		for fr_x, bk_x in zip(range(paper_x - paper_flip_x, paper_x), range(paper_flip_x - 1, -1, -1)):
			for y in range(0, paper_y):
				paper[y][fr_x] = int(paper[y][fr_x]) | int(paper_flip[y][bk_x])
	else:
		paper_y = paper.shape[0]
		paper_flip_y = paper_flip.shape[0]

		for fr_y, bk_y in zip(range(paper_y - paper_flip_y, paper_y), range(paper_flip_y - 1, -1, -1)):
			for x in range(0, paper_x):
				paper[fr_y][x] = int(paper[fr_y][x]) | int(paper_flip[bk_y][x])


print(paper)
