# The 5 x 5 matrix of 'O' is a ocean with a battleship hidden at a random i x j position find the position within 5 turns


from random import randint

from pip._vendor.distlib.compat import raw_input

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


def random_row(board):
    return randint(1, len(board))


def random_col(board):
    return randint(1, len(board))


ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

for turn in range(1, 6):
    print("Turn", turn)
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break

    else:
        if guess_row not in range(6) or \
                guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
            if turn == 3:
                print("Game Over")
        elif board[guess_row - 1][guess_col - 1] == "X":
            print("You guessed that one already.")
            if turn == 3:
                print("Game Over")
        else:
            print("You missed my battleship!")
            board[guess_row - 1][guess_col - 1] = "X"
            if turn == 3:
                print("Game Over")

    print_board(board)
