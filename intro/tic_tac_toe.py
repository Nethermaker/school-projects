import random
import copy

#We will represent the board as a string with
# TEN THINGS in it. The first thing will be blank (always),
# and the next nine will be 'X', 'O', or ' '.


board = ' XO XO XOO'

def draw_board(board):
    print '   |   |   '
    print ' {} | {} | {} '.format(board[7], board[8], board[9])
    print '   |   |   '
    print '-----------' #11 dashes
    print '   |   |   '
    print ' {} | {} | {} '.format(board[4], board[5], board[6])
    print '   |   |   '
    print '-----------' #11 dashes
    print '   |   |   '
    print ' {} | {} | {} '.format(board[1], board[2], board[3])
    print '   |   |   '

def input_player_letter():
    #Lets the player type which letter they want to be.
    #Returns a list with the player's letter first, and the
    # computer letter second
    letter = ''
    while letter not in ['X', 'O']:
        letter = raw_input('Do you want to be X or O? ').upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():
    #Randomly returns either 'computer' or 'player'
    return random.choice(['player', 'computer'])

def play_again():
    return raw_input('Do you want to play again (yes/no)? ').lower().startswith('y')

def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le))

def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or board[int(move)] != ' ':
        move = raw_input('What is your next move (1-9)? ')
    return int(move)




























