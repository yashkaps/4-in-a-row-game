# import tkinter as tk
import numpy as np
import pygame
import sys

ROW_COUNT = 6
COL_COUNT = 7

BLUE = (0,0,200)
BLACK = (0,0,0)


def create_board():
    return np.zeros((6, 7))


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_column(board, col):
    if col >= 0 and col <= 6 and board[0][col] == 0:
        return True
    else:
        return False


def get_next_open_row(board, col):
    for i in range(ROW_COUNT-1, -1, -1):
        if board[i][col] == 0:
            return i


def check_win(board):
    for piece in [1,2]:

        # check win for each row
        for i in range(ROW_COUNT):
            row = board[i]
            # for each window of 4
            for j in range(4):
                window = row[j:j+4]
                if not np.any(window - piece):
                    return "Player " + str(piece) + " is the winner!"

        # check win for each column
        for i in range(COL_COUNT):
            col = board[:,i]
            # for each window of 4
            for j in range(3):
                window = col[j:j+4]
                if not np.any(window - piece):
                    return "Player " + str(piece) + " is the winner!"

        # check win for the diagonals
        # offsets from -2 to 2
        for i in range(-2,2):
            diag = np.diagonal(board,i)
            for j in range(len(diag)-3):
                window = diag[j:j+4]
                if not np.any(window - piece):
                    return "Player " + str(piece) + " is the winner!"

        # check win for the diagonals in the other direction
        # offsets from -2 to 2
        temp = np.flip(board.copy(), axis=1)
        for i in range(-2, 2):
            diag = np.diagonal(temp, i)
            for j in range(len(diag) - 3):
                window = diag[j:j + 4]
                if not np.any(window - piece):
                    return "Player " + str(piece) + " is the winner!"
    return False


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(1,ROW_COUNT+1):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE//2), RADIUS)

board = create_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = SQUARESIZE//2 - 5

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
            # ask for player 1 input
            # if turn == 0:
            #     col = int(input("Player 1, make your selection (0-6): "))
            #     while not is_valid_column(board, col):
            #         col = int(input("Player 1, make your selection (0-6): "))
            #     row = get_next_open_row(board, col)
            #     drop_piece(board, row, col, 1)
            #
            # # ask for player 2 input
            # else:
            #     col = int(input("Player 2, make your selection (0-6): "))
            #     while not is_valid_column(board, col):
            #         col = int(input("Player 2, make your selection (0-6): "))
            #     row = get_next_open_row(board, col)
            #     drop_piece(board, row, col, 2)
            #
            # print(board)
            #
            # win = check_win(board)
            # if win:
            #     print(win)
            #     game_over = True
            #
            # turn += 1
            # turn = turn % 2

# HEIGHT = 500
# WIDTH = 600
#
# root = tk.Tk()
# root.minsize(WIDTH, HEIGHT)
# root.title("Game")
#
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()
#
# board_image = tk.PhotoImage(file='./board.png')
# background_label = tk.Label(root, bg='#80c1ff')
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# board = tk.Label(root, image=board_image, bd=5)
# board.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')
#
#
#
#
# root.mainloop()