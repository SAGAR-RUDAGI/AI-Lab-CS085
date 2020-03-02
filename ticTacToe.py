from random import randint
global col,row
class Game:
	def __init__(self):
		self.board =[[None for i in range(3)]for i in range(3)]
		self.player_one, self.player_two = 5,5
		self.count = 0
		self.pawn = {"X": "Player", "O": "Computer"}
		self.winner = False

	def printBoard(self):
		print()
		for i in range(3):
			print(self.board[i])

	def checkFilled(self,row,col):
		return self.board[row][col]

	def computer(self):
		flag = True
		if flag:
			row = randint(0,2)
			col = randint(0,2)
			flag = False

		else:
			ai_check()

		if self.board[row][col] != None:
			self.computer()
		else:
			self.board[row][col] = "O"
			if self.check(row,col):
				print("Computer Wins")

	def player(self):
		row = int(input("Row : "))
		col = int(input("Col : "))
		if not self.checkFilled(row,col):
			self.board[row][col] = "X"
			if self.check(row,col):
				print("Player Wins")
		else:
			print("Position is not empty... Try again")
			self.player()

	def place(self):
		if self.count < 9:
			if self.count % 2 == 0:
				self.player()
			else:
				self.computer()

			self.count += 1
			self.printBoard()


	def check(self,row,col):
		if self.board[row][0] == self.board[row][1] ==  self.board[row][2]:
			self.winner = True
			return True
		elif self.board[0][col] == self.board[1][col] ==  self.board[2][col]:
			self.winner = True
			return True
		elif row == col and self.board[0][0] == self.board[1][1] ==  self.board[2][2]:
			self.winner = True
			return True
		elif row + col == 2 and self.board[2][0] == self.board[1][1] ==  self.board[0][2]:
			self.winner = True
			return True

	def ai_check(self,row,col):
		empty = None
		empty_j = None
		for i in range(3):
			if board[row][i] == None:
				empty = i
			if board[row][i] = 'X' and i != col:
				board[row][empty] = 'O'

		for i in range(3):
			if board[i][col] == None:
				empty = i
			if board[i][col] == 'X' and i != row:
				board[empty][col] = 'O'

		if row == col:
			for i in range(3):
				if board[i][i] == None:
					empty = i

				if board[i][i] == 'X' and i != row:
					board[empty][empty] = 'O'

		if row + col == 2:
			for i,j in zip(range(3),range(2,-1,-1)):
				if board[i][j] == None:
					empty = i
					empty_j = j
				if board[i][j] == 'X' and i != row and j != col:
					board[empty][empty_j] = 'O'

 


	def play(self):
		print("Player : X")
		print("Computer : O")
		for i in range(9):
			if self.count<9 and not self.winner:
				self.place()
			else:
				break
obj = Game()
obj.play()
