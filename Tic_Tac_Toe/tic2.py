#!/usr/bin/python3

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
        print ('children:',self.children)

def is_win(board):
  for i, j, k in Wins:
    if board[i] == board[k] and board[j] == board[i] and board[i] != '_':
      return [True,board[i]]
  return [False,None]

def next_turn(turn):
  if turn == 'x':
    return 'o'
  return 'x'

def CreateAllBoards(layout,parent):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    helper(layout,parent,-1,'x')

def helper(layout,parent,pos,turn):
  board = list(layout)

  if pos == -1:
    AllBoards[layout] = BoardNode(layout)
    for i in range(9):
      if board[i] == "_":
        helper(layout,BoardNode(layout),i,turn)
    return
  board[pos] = turn
  _board = "".join(board)
 # print (_board)
  node = None
  if _board in AllBoards:
    node = AllBoards[_board]
  else: 
    node = BoardNode(_board)
    AllBoards[_board] = node
  '''
  if _board not in AllBoards:
    node = BoardNode(_board)
    AllBoards[_board] = node
  else:
    node = AllBoards[_board]
    '''
  if _board not in parent.children:
    parent.children.append(_board)
  node.parents.append(parent.layout)

 
  states = is_win(board)
  #print(states)
  iswin = states[0]
  winner = states[1]
  if "_" not in board or iswin:
    print ("rejio g")
    if iswin:
      if winner == 'x':
        node.endState = 'x'
        print ("fat safwana")
      else: 
        node.endState = 'o'
        print ("fatty safwana")
    else:
      node.endState('d')
      print ("fattest safwana")
    return
  
  for i in range(9):
    print (board[i])
    print("rglt4lhig")
    if board[i] == '_':
      helper(_board,node,i,next_turn(turn))

CreateAllBoards("_________",None)

#print(AllBoards)
print(len(AllBoards))
x = 0
o = 0
d = 0
