import re
import pprint

size = 5

def getInput():
	with open("input.txt") as fp:
		lines = fp.readlines()
		return lines

def readBingo(data):
	bingoboards = []
	currentboard = []
	for row in data:
		# If new line, then add to board
		if re.match("[\\n\\r]+", row):
			bingoboards.append(currentboard.copy())
			currentboard = []
			continue

		# Split each number into list + Strip whitespace & newline
		nums = [x.strip() for x in re.findall('...', row, re.DOTALL)]
		currentboard.append(nums)
	# Add last copy
	bingoboards.append(currentboard.copy())
	return bingoboards

def checkBingo(currentmoves, board):
	# Check horizontal (convert to set to use 'in' keyword)
	currentmoves = set(currentmoves)
	num = 0
	for i in range(0, size):
		num = 0
		for j in range(0, size):
			if board[i][j] in currentmoves:
				num += 1
			else:
				break
		# Return if 5 in a row
		if num == 5:
			return True

	# Check vertical
	num = 0
	for i in range(0, size):
		num = 0
		for j in range(0, size):
			if board[j][i] in currentmoves:
				num += 1
			else:
				break
		if num == 5:
			return True

	return False

def getScore(currentmoves, board):
	currentsum = 0
	set_moves = set(currentmoves)
	# Calculate board
	for i in range(0, size):
		for j in range(0, size):
			if board[i][j] not in set_moves:
				currentsum += int(board[i][j])
	# Multiply by last move
	currentsum = currentsum * int(currentmoves[-1])
	return currentsum

lines = getInput()

# Get moves + bords
bingomoves = lines.pop(0).split(",")
bingoboards = readBingo(lines[1:])
score = 0
numboards = len(bingoboards)
winners = [0] * numboards

for idx, move in enumerate(bingomoves):
	for bidx, board in enumerate(bingoboards):
		winner = checkBingo(bingomoves[:idx], board)
		if winner != False:
			score = getScore(bingomoves[:idx], board)
			winners[bidx] = 1
		# If all winners have been calculated
		if winners.count(1) == numboards:
			print(score)
			exit()

# Part 1 would just break the loop once the first win was detected instead of continuing the for loop
print(score)