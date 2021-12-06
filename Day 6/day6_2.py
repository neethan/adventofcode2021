days = 256

def getInput():
	with open("input.txt") as fp:
		lines = fp.readline()
		return [int(x) for x in lines.split(",")]

# Fill two dicts, first with number of each occurence
fishies = {i:0 for i in range(0,9)}
for i in getInput():
	fishies[i] += 1
nextfishies = {i:0 for i in range(0,9)}

for i in range(0, days):
	# Move all fish down
	for q in range(1, 9):
		nextfishies[q - 1] += fishies[q]

	# Update special cases
	nextfishies[8] += fishies[0]
	nextfishies[6] += fishies[0]

	# Next iteration
	fishies = nextfishies
	nextfishies = {i:0 for i in range(0,9)}

print(sum(fishies.values()))
