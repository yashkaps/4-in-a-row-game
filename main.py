
import numpy as np
import pygame
import sys

ROW_COUNT = 6
COL_COUNT = 7

RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
colors = [BLACK, RED, YELLOW]


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
                    return "Player " + str(piece) + " wins!!"

        # check win for each column
        for i in range(COL_COUNT):
            col = board[:,i]
            # for each window of 4
            for j in range(3):
                window = col[j:j+4]
                if not np.any(window - piece):
                    return "Player " + str(piece) + " wins!!"

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
            pygame.draw.circle(screen, colors[int(board[r-1][c])], (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE//2), RADIUS)

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

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            pygame.draw.circle(screen, RED if turn == 0 else YELLOW, (event.pos[0], SQUARESIZE//2), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos[0] // 100)
            # ask for player 1 input
            if turn == 0:
                # col = int(input("Player 1, make your selection (0-6): "))
                col = event.pos[0] // SQUARESIZE
                while not is_valid_column(board, col):
                    col = int(input("Player 1, make your selection (0-6): "))
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
            #
            # # ask for player 2 input
            else:
                # col = int(input("Player 2, make your selection (0-6): "))
                col = event.pos[0] // SQUARESIZE
                while not is_valid_column(board, col):
                    col = int(input("Player 2, make your selection (0-6): "))
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

            print(board)

            win = check_win(board)
            if win:
                label = myfont.render(win, 1, (255,255,255))
                screen.blit(label, (30,10))
                # print(win)
                game_over = True

            turn += 1
            turn = turn % 2

            draw_board(board)
            pygame.display.update()

            if game_over:
                pygame.time.wait(3000)

