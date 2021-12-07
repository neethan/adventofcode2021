def getInput():
	with open("input.txt") as fp:
		lines = fp.readline()
		return lines

crabs = [int(x) for x in getInput().split(",")]

bestfuel = 99999999999
for base in crabs:
	fuel = 0
	for crab in crabs:
		fuel += abs(crab - base)
	bestfuel = fuel if fuel < bestfuel else bestfuel

print(bestfuel)