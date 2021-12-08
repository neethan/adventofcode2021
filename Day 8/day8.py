import re

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		return lines

# lol
digits = re.split(" |\n", "".join([x.split(" | ")[1] for x in getInput()]))
count = 0
for digit in digits:
	if len(digit) in (2, 3, 4, 7):
		count += 1

print(count)
