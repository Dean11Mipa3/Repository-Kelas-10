"""
This program made by:
Name: Dean Frederic Wijaya
Class: 10.2 Computer Class
"""


import os
import random

"""
Custome BattleShip -> Intro, Congrats
"""

def intro():
	os.system("cls")
	print("Hi There, Welcome to Bermuda Triangle BattleShip")

	return input("Please input how many rows you wanna play: ")

def setting_up_board(rows):

	board = []

	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("O")
		board.append(line)

	return board

def setting_up_ship_location(rows):
	location = str(random.randint(0, rows-1)), str(random.randint(0, rows-1))
	return list(location)


def printing_board(board):
	os.system("cls")
	for row in board:
		for item in row:
			print(item, end=" ")
		print()

def check_user_input():
	while True:
		try:
			user_input = input("Enter Ship Location: ").split(" ")
			if len(user_input) != 2:
				print(f"You must input w integer numbers!")
				input()
			else:
				user_input = [str(int(user_input[0])-1), str(int(user_input[1])-1)]
		except ValueError as e:
			print(f"You must input an integer number!\nPython Error: {e}")
			input("ENTER to Try Again")
		else:
			if len(user_input) > 2:
				pass
			elif int(user_input[0]) < 0 or int(user_input[1]) > rows-1 or int(user_input[1]) < 0 or int(user_input[1]) > rows-1:
				print(f"You must input number between 1 and {rows}")
				input("ENTER to Try Again")
			else:
				break


	if my_ship == user_input:
		return True

	my_board[int(user_input[0])][int(user_input[1])] = "x"
	return False

def congrats():
	print(f"Ay!! Nice Shoot, you only take {attempt} Bullets")

win = False
attempt = 1

#recursion
while True:
	try:
		rows = int(intro())
	except ValueError as e:
		print(f"You must input an integer number!\nPython Error:{e}")
		input("ENTER to Try Again.")
	else:
		if rows < 3:
			print("You must input a number more than 2.")
			input("ENTER to Try Again")
		else:
			break

my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows) #lists

while not win:

	printing_board(my_board)
	print(my_ship)
	win = check_user_input()
	if not win:
		attempt += 1

congrats()