from collections import Counter

with open("input.txt") as fp:
	lines = fp.readlines()

	lines_o2 = list(lines)
	lines_co2 = list(lines)
	next_o2 = []
	next_co2 = []
	for i in range(0, 12):
		if len(lines_o2) != 1:	
			mostcommon_o2 = Counter(x[i] for x in lines_o2).most_common()

			if mostcommon_o2[0][1] == mostcommon_o2[1][1]:
				mostcommon_o2 = "1"
			else:
				print(mostcommon_o2)
				mostcommon_o2 = mostcommon_o2[0][0]

			for line in lines_o2:
				if line[i] == mostcommon_o2:
					next_o2.append(line)

			lines_o2 = list(next_o2)
			next_o2 = []
		if len(lines_co2) != 1:
			mostcommon_co2 = Counter(x[i] for x in lines_co2).most_common()

			if mostcommon_co2[0][1] == mostcommon_co2[1][1]:
				mostcommon_co2 = "0"
			else:
				print(mostcommon_co2)
				mostcommon_co2 = mostcommon_co2[1][0]

			for line in lines_co2:
				if line[i] == mostcommon_co2:
					next_co2.append(line)

			lines_co2 = list(next_co2)
			next_co2 = []

print(int(lines_co2[0], 2) * int(lines_o2[0], 2))