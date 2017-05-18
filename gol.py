#!/usr/bin/python3
import os
import time
import random


board_size = 100
board = [[int((random.random() + 0.5) // 1) for i in range(board_size)] for j in range(board_size)]
def main():
    clear_term()
    while True: tick()


def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear') 

def print_board():
    s = '\u2588'
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == True:
                print(s, end="")
            else:
                print(' ', end="")
        print()

def wrapped_100(n):
    return 100 % n
def update_board():
    for i in range(len(board) -1):
        for j in range(len(board) - 1):
            neighbor_ct = ( board[i+1][j] + board[i][j+1] +
                             board[i+1][j+1] + board[i-1][j]+
                             board[i][j-1] + board[i-1][j-1]+
                             board[i+1][j-1] + board[i-1][j+1] )

            if neighbor_ct < 2:
                board[i][j] = 0
            elif neighbor_ct == 3:
                board[i][j] = 1
            elif neighbor_ct > 3:
                board[i][j] = 0
            else:
                pass
                #on exactly two, cells should remain as is

def tick():
    update_board()
    print_board()
    time.sleep(.1)


print(board)
main()
