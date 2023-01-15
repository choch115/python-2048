import random

SIZE = 2
PROB_FOUR = 0.5

def get_empty_spaces(board):
	empty_spaces = []
	for i in range(SIZE):
		for j in range(SIZE):
			if board[i][j] == 0:
				empty_spaces.append((i,j))
	return empty_spaces

# modifies board itself
def add_tile(board, empty_spaces):
	space = empty_spaces[random.randint(0,len(empty_spaces)-1)]
	
	if random.random() < PROB_FOUR:
		board[space[0]][space[1]] = 4
	else:
		board[space[0]][space[1]] = 2

def initialize_board(SIZE):
	board = [[0]*SIZE for i in range(SIZE)]
	for i in range(2):
		empty_spaces = get_empty_spaces(board)
		add_tile(board, empty_spaces)
	
	return board

def print_board(board):
	for i in board:
		for j in i:
			if j == 0:
				print('-'+' '*4, end = '')
			elif j < 10:
				print(str(j)+' '*4, end = '')
			elif j < 100:
				print(str(j)+' '*3, end = '')
			elif j < 1000:
				print(str(j)+' '*2, end = '')
			else:
				print(str(j)+' ', end = '')
		print()

def move(board, input):
	successful = False

	if input == "w":
		for i in range(SIZE):
			for j in range(SIZE):
				k = j
				if board[j][i] != 0:
					while k > 0:
						if board[k-1][i] == 0:
							board[k-1][i] = board[k][i]
							board[k][i] = 0
							k-=1
							successful = True
						else:
							if board[k-1][i] == board[k][i]:
								board[k-1][i] = 2*board[k][i]
								board[k][i] = 0
								successful = True
							break
	elif input == "s":
		for i in range(SIZE):
			for j in range(SIZE):
				k = j
				if board[SIZE-1-k][i] != 0:
					while k > 0:
						if board[SIZE-k][i] == 0:
							board[SIZE-k][i] = board[SIZE-1-k][i]
							board[SIZE-1-k][i] = 0
							k-=1
							successful = True
						else:
							if board[SIZE-k][i] == board[SIZE-1-k][i]:
								board[SIZE-k][i] = 2*board[SIZE-1-k][i]
								board[SIZE-1-k][i] = 0
								successful = True
							break
	elif input == "a":
		for i in range(SIZE):
			for j in range(SIZE):
				k = j
				if board[i][k] != 0:
					while k > 0:
						if board[i][k-1] == 0:
							board[i][k-1] = board[i][k]
							board[i][k] = 0
							k-=1
							successful = True
						else:
							if board[i][k-1] == board[i][k]:
								board[i][k-1] = 2*board[i][k]
								board[i][k] = 0
								successful = True
							break
	elif input == "d":
		for i in range(SIZE):
			for j in range(SIZE):
				k = j
				if board[i][SIZE-1-k] != 0:
					while k > 0:
						if board[i][SIZE-k] == 0:
							board[i][SIZE-k] = board[i][SIZE-1-k]
							board[i][SIZE-1-k] = 0
							k-=1
							successful = True
						else:
							if board[i][SIZE-k] == board[i][SIZE-1-k]:
								board[i][SIZE-k] = 2*board[i][SIZE-1-k]
								board[i][SIZE-1-k] = 0
								successful = True
							break
	
	return successful

def is_board_alive(board):
	empty_spaces = get_empty_spaces(board)
	if len(empty_spaces) > 0: return True
	for i in range(SIZE):
		for j in range(SIZE-1):
			if board[i][j] == board[i][j+1]: return True
	for i in range(SIZE-1):
		for j in range(SIZE):
			if board[i][j] == board[i+1][j]: return True
	return False

def main():
	alive = True

	board = initialize_board(SIZE)

	# clear screen
	for i in range(100):
		print()

	while is_board_alive(board):
		
		print_board(board)
		
		uin = input("")
		print("")
		
		successful = move(board,uin)
		
		if successful:
			empty_spaces = get_empty_spaces(board)
			# guaranteed to be at least one space
			add_tile(board, empty_spaces)
			
	# after death
	
	print_board(board)
	print('Game over!')
	
			
main()