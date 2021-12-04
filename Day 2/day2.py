with open("input.txt") as fp:
	lines = fp.readlines()
	aim = 0
	horizontal = 0
	depth = 0
	for line in lines:
		cmd = line.split()
		if cmd[0] == "forward":
			horizontal += int(cmd[1])
			depth += int(cmd[1]) * aim
		elif cmd[0] == "up":
			aim -= int(cmd[1])
		elif cmd[0] == "down":
			aim += int(cmd[1])
print(depth * horizontal)