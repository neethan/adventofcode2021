from statistics import median

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		return [x.strip() for x in lines]

data = getInput()

openers = ["{", "[", "(", "<"]
closers = ["}", "]", ")", ">"]
autocompletes = []
scores = []

for line in data:
	linepath = []
	autocomplete = []
	for char in line:
		if char in closers:
			last = linepath[-1]
			if not closers.index(char) == openers.index(last):
				linepath = []
				break
			else:
				linepath.pop()
		else:
			linepath.append(char)

	if len(linepath) != 0:
		print(linepath)
		while len(linepath) != 0:
			last = linepath[-1]
			autocomplete.append(closers[openers.index(last)])
			linepath.pop()
		autocompletes.append(autocomplete)

for line in autocompletes:
	score = 0
	for i in line:
		score *= 5
		if i == "}": score += 3
		if i == "]": score += 2
		if i == ")": score += 1
		if i == ">": score += 4
	scores.append(score)

print(scores)
print(median(scores))