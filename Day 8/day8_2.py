import re

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		return lines

def getDigit(lst, size):
    for x in lst:
        if len(x) == size:
        	return x

digits = [x.strip().split(" | ") for x in getInput()]
count = 0
for row in digits:
	inputs = row[0].split(" ")
	display = row[1].split(" ")
	decoder = [""] * 10
	# Easy numbers
	decoder[1] = getDigit(inputs, 2)
	decoder[4] = getDigit(inputs, 4)
	decoder[7] = getDigit(inputs, 3)
	decoder[8] = getDigit(inputs, 7)

	# Find for lengths of 5
	decoder[3] = [x for x in inputs if len(x) == 5 and set(decoder[1]) <= set(x)][0]
	diff = set(decoder[4]).difference(set(decoder[3]))
	decoder[5] = [x for x in inputs if len(x) == 5 and x not in decoder and diff <= set(x)][0]
	decoder[2] = [x for x in inputs if len(x) == 5 and x not in decoder][0]

	# Find for lengths of 6
	diff = set(decoder[4]).difference(set(decoder[5]))
	decoder[6] = [x for x in inputs if len(x) == 6 and x not in decoder and not diff.issubset(set(x))][0]
	diff = set(decoder[6]).difference(set(decoder[5]))
	decoder[9] = [x for x in inputs if len(x) == 6 and x not in decoder and not diff.issubset(set(x))][0]
	decoder[0] = [x for x in inputs if len(x) == 6 and x not in decoder][0]
	decoder = ["".join(sorted(x)) for x in decoder]

	lookuptable = dict(zip(decoder, range(0,10)))
	count += int("".join([str(lookuptable["".join(sorted(x))]) for x in display]))

print(count)
