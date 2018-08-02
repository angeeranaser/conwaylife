# Game of Life
# Program by: Angeera Naser
# angeeraxn@gmail.com
# github.com/angeeranaser
# Project referenced from https://robertheaton.com/2018/07/20/project-2-game-of-life/

import numpy as np
import random
from time import sleep

def random_board(height, width):
    # Creates a random board of a specified height and width.
    board = np.empty((height, width), dtype=int)
    for i in range(0, height):
        for j in range(0, width):
            board[i][j] = random.randint(0,1)
    return board

def load_board(filename):
    # Loads a text file with an existing board.
    with open(filename, "r") as f:
        board = f.readlines()
    board = [i.strip() for i in board]
    board = [[int(j) for j in i] for i in board]
    return board

def dead_state(height, width):
    # Creates a board of zeroes of a specified height and width.
    dead = np.zeros((height, width), dtype=int)
    return dead

def live_neighbors(y, x, board):
    # Counts the number of live neighbors of a board element (max: 8).
    count = 0
    if (board[y][x] == 1): count += -1 # Doesn't count itself as a neighbor.
    for i in range(3):
        for j in range(3):
            try: # Find live neighbors that are within the bounds of the board.
                if (board[y-1+i][x-1+j] == 1) & (y-1+i >= 0) & (x-1+j >= 0): count += 1 # i and j help iterate through neighbors of cell (x,y).
            except(IndexError): pass
    return count

def check(y, x, board):
    # Returns the next state (live or dead) of a given element.
    if (board[y][x] == 0) & (live_neighbors(y, x, board) == 3): return 1 # If cell (x,y) is dead and has exactly 3 neighbors, it comes alive.
    elif (board[y][x] == 1) & (live_neighbors(y, x, board) >= 2) & (live_neighbors(y, x, board) <= 3): return 1 # If cell (x,y) is alive and has 2-3 neighbors, it stays alive.
    else: return 0 # Everything else dies. Or stays dead. Whichever.

def next_board(board):
    # Generates the next board.
    height = len(board)
    width = len(board[0])
    new_board = dead_state(height, width) # Generates an empty (zeroed out) board of the same dimensions as the original.
    for y in range(0, height):
        for x in range(0, width):
            new_board[y][x] = check(y, x, board) # Checks each element and updates the empty board with the next state of each.
    return new_board

def prettify(board):
    # Sets the board up for pretty-printing.
    pretty = ''
    for i in range(0,len(board)):
        pretty += '| '
        for j in range(0,len(board[i])):
            if (board[i][j] == 0):
                pretty += '   '
            else:
                pretty += ' O '
        pretty += ' |\n'
    return pretty

def draw(board):
    # Prints the prettified boards.
    print(prettify(board))
    # sleep(0.2)
    next = next_board(board)
    print(prettify(next))
    # sleep(0.2)
    while(True):
        next = next_board(next)
        print(prettify(next)) # Continually feeds the next board to the pretty-printer.
        # sleep(0.2)

def main():
    # Lets user choose type of board (premade/random), and then prints it.
    boardtype = input("load/random: ")
    if boardtype == 'load':
        while True: # Check for valid input.
            try:
                filename = input('filepath: ')  # Sample: "./start/glider.txt"
                board = load_board(filename)
                break
            except: pass
        draw(board)
    elif boardtype == 'random':
        while True: # Check for valid input.
            try:
                height = int(input("height: "))
                if height > 0: break
            except: pass
        while True: # Check for valid input.
            try:
                width = int(input("width: "))
                if width > 0: break
            except: pass
        board = random_board(height, width)
        draw(board)
    else: print('invalid input')

if __name__ == "__main__":
    main()
