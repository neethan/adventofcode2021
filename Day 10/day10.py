import re
import numpy as np

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		return lines

data = getInput()

openers = ["{", "[", "(", "<"]
closers = ["}", "]", ")", ">"]
incorrectchars = []
score = 0
for line in data:
	linepath = []
	tmpchars = []
	for char in line:
		if char in closers:
			last = linepath[-1]
			if not closers.index(char) == openers.index(last):
				tmpchars.append(char)
				break
			else:
				linepath.pop()
		else:
			linepath.append(char)

	if len(linepath) != 0 and len(tmpchars) == 0:
		continue
	else:
		incorrectchars.extend(tmpchars)

for i in incorrectchars:
	if i == "}": score += 1197
	if i == "]": score += 57
	if i == ")": score += 3
	if i == ">": score += 25137

print(incorrectchars)
print(score)