import os
#set win in game
def setWin(lis, player):
	#check win by row
	for i in range(3):
		if lis[i] == [player for j in range(3)]:
			return True
	#check win by i i
	check = True
	checkneg = True
	for i in range(3):
		if lis[i][i] != player:
			check = False
		if lis[2-i][i] != player:
			checkneg = False
	if check or checkneg:
		return True
	#check win by col
	for i in range(3):
		check = True
		for j in range(3):
			if lis[j][i] != player:
				check = False
				break
		if check:
			return True
	return False
#print chessboard
def printChessBoard(lis):
	for i in range(3):
		print("+---+---+---+");
		print("|{:^3}|{:^3}|{:^3}|".format(lis[i][0], lis[i][1], lis[i][2]))
	print("+---+---+---+");
#begin screen
def printBegin():
	os.system("clear")
	print("+{:-^30}+\n".format(""))
	print("|{:^30}|\n".format("") * 2)
	print("|{:^30}|\n".format("TIC-TAC-TOE"))
	print("|{:^30}|\n".format("") * 2)
	print("+{:-^30}+\n".format(""))
	raw_input("{:^30}".format("Press any key to play..."));
	os.system("clear")

#program
printBegin()
li = [['.', '.', '.'] for i in range(3)]
Player = 'X'
index = 0
while True:
	#Print chessboard
	print(">>> " + Player)
	printChessBoard(li)
	#input player
	while True:
		dic = {1:(0,0), 2:(1,0), 3:(2,0), 4:(0, 1), 5:(1, 1), 6:(2, 1), 7:(0, 2), 8:(1, 2), 9:(2, 2)}
		try:
			player_inputa = input("Where you want to check? (input 1 to 9): ")
			if(player_inputa < 1 or player_inputa > 9):
				raise
			player_input = dic[int(player_inputa)]
			if li[player_input[1]][player_input[0]] is '.':
				li[player_input[1]][player_input[0]] = Player;
			else:
				raise 
		except:
			print("Your input is error. Input again")
			continue
		else:
			break
	#set win
	if setWin(li, Player):
		os.system('clear')
		print(Player + " is win")
		printChessBoard(li)
		break
	# set draw
	index += 1
	if index == 9:
		os.system('clear')
		print("DRAW !!!")
		printChessBoard(li)
		break
	#Change X to O and neg
	if(Player is 'X'):
		Player = 'O'
	else:
		Player = 'X'
	os.system('clear')