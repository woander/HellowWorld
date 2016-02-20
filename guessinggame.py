from random import randint

board = []

for x in range(5):
    board.append(['O'] * 5)
# now there are 5 lists of 5 "O"

def print_board(board):
    for row in board:
        print(' '.join(row))
# now the board doesn't print like a list but instead just 5 x 5 "O" with a space between each "O"

print("Let's play Battleship!")
print_board(board)
# the board now appears on the screen

def random_row(board):
    return randint(0, len(board) -1)
# this is saying chose a number between 0 and the length of the board which is 5
# and then minus 1 so now it will guess 0 1 2 3 4

def random_col(board):
    return randint(0, len(board[0]) -1)
# this is saying the same thing as the function above, except it starts at index 0
# in other words, it only chooses from the first list of "O"'s which is the top of the row of the board

ship_row = random_row(board)
ship_col = random_col(board)

# now the battleship has a spot on the board

try:
    for turn in range(4):
        guess_row = ''
        guess_col = ''

        while guess_row == '' and guess_col == '':
            guess_row = input('Guess Row:')
            guess_col = input('Guess Column:')

            try:
                guess_row = int(guess_row)
                guess_col = int(guess_col)

            except:
                print('Please enter a number!')
                guess_row = ''
                guess_col = ''

        if guess_row == ship_row and guess_col == ship_col:
            print('Congratulations! You sunk my Battleship!')
            break

        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print ("Oops, that's not even in the ocean.")
            elif (board[guess_row][guess_col] == 'X'):
                print("You guessed that one already.")
            else:
                print('You missed my Battleship!')
                board[guess_row][guess_col] = 'X'
                if turn == 3:
                    print('Game Over')

            if turn == 0:
                print('Turn', turn + 2)
            else:
                print('Turn', turn + 1)
            print_board(board)
except:
    print("Game Error, try again!")