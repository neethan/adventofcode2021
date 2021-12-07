def getInput():
	with open("input.txt") as fp:
		lines = fp.readline()
		return lines

crabs = [int(x) for x in getInput().split(",")]

bestfuel = 99999999999
for i in range(min(crabs), max(crabs)):
	fuel = 0
	for crab in crabs:
		n = abs(crab - i)
		fuel += round((n**2 + n) / 2)
	bestfuel = fuel if fuel < bestfuel else bestfuel

print(bestfuel)