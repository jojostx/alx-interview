#!/usr/bin/python3
"""Python3 program to solve N Queen
Problem using backtracking
"""
import sys


def Error_Exit(message):
    print(message)
    sys.exit(1)

def is_valid(state):
    state = [1, 3]
    r = len(state) - 1
       # 0, 1
    for (i, v) in enumerate(state):
        diff = abs(v - state[r])
        if diff == 0 or diff == r - i:
           return False
    
    return True

def is_safe(row, col, board, n):
  x = row
  y = col
  
  # Check for same upper col
  while(x>=0):
    if board[x][y] == "Q":
      return False
    else:
      x -= 1
      
  # Check for Upper Right Diagonal
  x = row
  y = col
  while(y<n and x>=0):
    if board[x][y] == "Q":
      return False
    else:
      y += 1
      x -= 1
      
  # Check for Upper Left diagonal
  x = row
  y = col
  while(y>=0 and x>=0):
    if board[x][y] == "Q":
      return False
    else:
      x -= 1
      y -= 1
  return True


def solveNQueens(row, ans, board, n):
   pass


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 2:
        Error_Exit('Usage: nqueens N')

    N = argv[1]

    if N.isdigit() is False:
        Error_Exit('N must be a number')

    N = int(N)

    if N < 4:
        Error_Exit('N must be at least 4')
    
    # 2D array of string will make our board
    # which is initially all empty
    board = [['0' for i in range(N)] for j in range(N)]
    
    # Store all the possible answers
    ans = []
    solveNQueens(0, ans, board, N)
    
    if ans == []:
      print("Solution does not exist")
    else:
      print(ans)
