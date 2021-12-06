days = 80

def getInput():
	with open("input.txt") as fp:
		lines = fp.readline()
		return lines

fishies = [int(x) for x in getInput().split(",")]
nextfishies = []

for i in range(0, days):
	nextfishies = [8] * fishies.count(0)
	fishies = list(map(lambda x: 7 if x == 0 else x, fishies))
	fishies = [x - 1 for x in fishies]

	fishies.extend(nextfishies)
	nextfishies = []

print(len(fishies))
