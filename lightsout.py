#!/bin/python
# Head ends here
import copy
import random

def nextMove(player,board):
    winning_move = win(board)
    if winning_move != False:
        print(str(winning_move["x"]) + " " + str(winning_move["y"]))
        return None

    losing_moves = opponentWin(board)

    for x in xrange(0,8):
        for y in xrange(0,8):
            if x > 3 and len(losing_moves) == 0:
                while(True):
                    randX = random.randint(0,7)
                    randY = random.randint(0,7)
                    if board[randX][randY] == "1":
                        print(str(randX) + " " + str(randY))
                        return None
            elif board[x][y] == "1" and str(x)+str(y) not in losing_moves:
                print(str(x) + " " + str(y))
                return None


    # if we've gotten here we're screwed, just hit the first
    for i in xrange(0,8):
        for j in xrange(0,8):
            if board[i][j] == "1":
                print(str(i) + " " + str(j))
                return None

def win(board):
    test_board = copy.copy(board)

    for x in xrange(0,8):
        for y in xrange(0,8):
            if test_board[x][y] == "1":
                # simulate a switch
                test_board[x] = test_board[x][:y] + "0" + test_board[x][y+1:]
                try:
                    if test_board[x+1][y] == "1":
                        test_board[x+1] = test_board[x+1][:y] + "0" + test_board[x+1][y+1:]
                    else:
                        test_board[x+1] = test_board[x+1][:y] + "1" + test_board[x+1][y+1:]
                except:
                    pass
                try:
                    if test_board[x][y+1] == "1":
                        test_board[x] = test_board[x][:y+1] + "0" + test_board[x][y+2:]
                    else:
                        test_board[x] = test_board[x][:y+1] + "1" + test_board[x][y+2:]
                except:
                    pass

                # check if the simulated state causes a win
                if(checkWin(test_board) == True):
                    return {"x":x, "y":y}
                else:
                    test_board = copy.copy(board)

    return False

def opponentWin(board):
    test_board = copy.copy(board)
    losingMoves = []

    for x in xrange(0,8):
        for y in xrange(0,8):
            if test_board[x][y] == "1":
                # simulate a switch
                test_board[x] = test_board[x][:y] + "0" + test_board[x][y+1:]
                try:
                    if test_board[x+1][y] == "1":
                        test_board[x+1] = test_board[x+1][:y] + "0" + test_board[x+1][y+1:]
                    else:
                        test_board[x+1] = test_board[x+1][:y] + "1" + test_board[x+1][y+1:]
                except:
                    pass
                try:
                    if test_board[x][y+1] == "1":
                        test_board[x] = test_board[x][:y+1] + "0" + test_board[x][y+2:]
                    else:
                        test_board[x] = test_board[x][:y+1] + "1" + test_board[x][y+2:]
                except:
                    pass

                # check if the simulated state causes a win
                winningMove = win(test_board)
                if(winningMove != False):
                    losingMoves.append(str(x)+str(y))
                elif(checkEndGame(test_board)):
                    losingMoves.append(str(x)+str(y))

                test_board = copy.copy(board)

    return losingMoves

def checkWin(board):
    for x in xrange(0,8):
        for y in xrange(0,8):
            if board[x][y] == "1":
                return False

    return True

def checkEndGame(board):
    on_count = 0
    for x in xrange(0,8):
        for y in xrange(0,8):
            if board[x][y] == "1":
                on_count = on_count + 1

    if on_count < 5 and on_count > 0:
        if(board[6][6] == "1" and board[6][7] == "1" and board[7][6] == "1" and board[7][7] == "1"):
            return True
        elif(board[6][6] == "0" and board[6][7] == "1" and board[7][6] == "1" and board[7][7] == "0"):
            return True
        else:
            return False
    else:
        return False




# Tail starts here
#If player is 1, I'm the first player.
#If player is 2, I'm the second player.
player = raw_input()

#Read the board now. The board is a 8x8 array filled with 1 or 0.
board = []
for i in xrange(0, 8):
    board.append(raw_input())

nextMove(player,board)