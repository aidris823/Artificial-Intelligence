#!/usr/bin/python3

board = [['b','b','b']] * 3
print board

def add_X(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'b':
                board[i][j] = 'X'
    return board
def add_O(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'b':
                board[i][j] == 'O'
    return board
def is_filled(board):
    for i in board:
        for j in i:
            if j == 'b':
                return False
    return True

def calc_games(board, counter = 0, p1_turn = True):
    if is_filled(board):
        return counter
    for i in range(3):
        for j in range(3):
            print board[i][j]
            if board[i][j] == 'b':
                if p1_turn:
                    board[i][j] == 'X'
                else:
                    board[i][j] == 'O'
            counter += 1
            p1_turn = not p1_turn
            print board
  

print calc_games(board)
print board
    
                
    
