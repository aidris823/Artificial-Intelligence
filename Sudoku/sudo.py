#!/usr/bin/python3
import sys
import copy

fred = open(sys.argv[1],'r')
ans = open(sys.argv[2],'w')
nombre = sys.argv[3]

print("El nombre es: " + nombre)

board = list()

info = fred.read().strip().split("\n")

cliques = [[0,1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16,17],
[18,19,20,21,22,23,24,25,26],
[27,28,29,30,31,32,33,34,35],
[36,37,38,39,40,41,42,43,44],
[45,46,47,48,49,50,51,52,53],
[54,55,56,57,58,59,60,61,62],
[63,64,65,66,67,68,69,70,71],
[72,73,74,75,76,77,78,79,80],
[0,9,18,27,36,45,54,63,72],
[1,10,19,28,37,46,55,64,73],
[2,11,20,29,38,47,56,65,74],
[3,12,21,30,39,48,57,66,75],
[4,13,22,31,40,49,58,67,76],
[5,14,23,32,41,50,59,68,77],
[6,15,24,33,42,51,60,69,78],
[7,16,25,34,43,52,61,70,79],
[8,17,26,35,44,53,62,71,80],
[0,1,2,9,10,11,18,19,20],
[3,4,5,12,13,14,21,22,23],
[6,7,8,15,16,17,24,25,26],
[27,28,29,36,37,38,45,46,47],
[30,31,32,39,40,41,48,49,50],
[33,34,35,42,43,44,51,52,53],
[54,55,56,63,64,65,72,73,74],
[57,58,59,66,67,68,75,76,77],
[60,61,62,69,70,71,78,79,80]]

for i in info:
    x = i.split(',')
    board.append(x)

#Return a list of possible numbers for a particular tile.  
def get_candidates(board,pos):
    clique = {}
    for i in cliques:
        if pos in i:
            if pos not in clique:
                clique[pos] = list()
            clique[pos].append(i)
    oned_board = list()
    for i in board:
        oned_board += i
    ans = list()
    taken = list()

    for i in range(1,10):
        for j in clique:
            x = clique[j]
            for k in x:
                for l in k:
                    if oned_board[l] != '_' and int(oned_board[l]) == i:
                        taken.append(i)
    pos_ans = [1,2,3,4,5,6,7,8,9]
    for i in pos_ans:
        if i not in taken:
            ans.append(i)
    return ans
#for i in range(0,80):
    #print get_candidates(board,i)

#Base Case: Entire board is filled
def is_filled(board):
    for i in board:
        for j in i:
            if j == '_':
                return False
    return True

def solve(board):
    pos = 0
    coors = [-1,-1]
    #Basecase
    if is_filled(board):
        #print board
        return board
    else:
        for i in range(9):
            for j in range(9):
                pos += 1
                if board[i][j] == '_':
                    coors = [i,j]
                    break
            if coors != [-1,-1]:
                break
        #print coors
        #print pos
        candidates = get_candidates(board,pos)
        #print candidates
        for i in candidates:
            board[coors[0]][coors[1]] = i
            #print board
            solve(board)



            
answer = board
def solveSudo(board):
    pos = -1
    for i in range(0,9):
        for j in range(0,9):
            pos+=1
            if board[i][j] == '_':
        #        print pos
                candidates = get_candidates(board,pos)
         #       print [i,j]
          #      print candidates
                for k in candidates:
                    board[i][j] = k
                    if solveSudo(board):
                        answer = board
                        return True
                    else:
                        board[i][j] = '_'
                return False
    return True

solveSudo(board)


for i in answer:
    line = ""
    for j in i:
        line += str(j)
        line += ','
    ans.write(line[:-3])
    ans.write("\n")
fred.close()
ans.close()
