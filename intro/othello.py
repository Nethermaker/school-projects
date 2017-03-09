#EDITOR'S NOTES:
# 
# You'll probably want to play against another person, and not just yourself
# You can check the rules using the menu
# Also, if you finish your game, please exit using the menu in order to save the score


# There are some (rare) possibilities that can happen that I have NOT had time to program for.
# For instance:
#   It is possible to not be able to play on a turn
#   It is possible for neither person to be able to play, and thus the game would end early
# If either of the above end up happening, you have the ability to type 'pass' on your turn.
# THIS IS ONLY LEGAL IF YOU CANNOT MOVE, but I haven't had time to program a check for that.
# If BOTH players cannot move, and type 'pass' in a row, then they will have the option to
# end the game. If they choose to do so, the current number of pieces on the board will be
# used to determine a winner. This is how it works in a real game of Othello

import copy
import re
import sys
import os.path
import webbrowser
import time

board = [['This is here to make things easier, along with the first spot in each line'],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

starting_board = [['This is here to make things easier, along with the first spot in each line'],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]



#Blank board:
##[['This is here to make things easier, along with the first spot in each line'],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


#This is pretty self-explanatory
def draw_board(board):
    print '  a b c d e f g h'
    print '1 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7], board[1][8])
    print '  ---------------'
    print '2 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7], board[2][8])
    print '  ---------------'
    print '3 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7], board[3][8])
    print '  ---------------'
    print '4 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7], board[4][8])
    print '  ---------------'
    print '5 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7], board[5][8])
    print '  ---------------'
    print '6 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7], board[6][8])
    print '  ---------------'
    print '7 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7], board[7][8])
    print '  ---------------'
    print '8 {}|{}|{}|{}|{}|{}|{}|{}'.format(board[8][1], board[8][2], board[8][3], board[8][4], board[8][5], board[8][6], board[8][7], board[8][8])

   

#This function gets the players move and makes sure it follows the format,
# calls is_valid(), which copies the board, makes the move if it's at least
# partially valid, and then returns the move. It then returns back here
# in order to make sure that a valid move actually WAS made, and if it was, updates the board.
def get_player_move(player):
    global board
    letters = {'a':1,
               'b':2,
               'c':3,
               'd':4,
               'e':5,
               'f':6,
               'g':7,
               'h':8}
    if player == '1':
        letter = 'X'
        opposite = 'O'
    else:
        letter = 'O'
        opposite = 'X'
    pattern = re.compile('[a-h][1-8]')
    while True:
        new_board = copy.deepcopy(board)
        move = raw_input('Player {}, choose the column and row you want to move in (ex. \'c6\'): '.format(player))
        #Checks if the input matches the wanted pattern
        if pattern.match(move):
            row = int(move[1])
            column = letters[move[0]]
            new_board = is_valid(row, column, letter)
            if new_board == None:
                print 'That move is not valid! Please make a different move.'
            else:
                letter_count = 0
                opposite_count = 0
                new_letter_count = 0
                new_opposite_count = 0
                for row in board:
                    for piece in row:
                        if piece == letter:
                            letter_count += 1
                        elif piece == ' ':
                            pass
                        elif piece == opposite:
                            opposite_count += 1
                for row in new_board:
                    for piece in row:
                        if piece == letter:
                            new_letter_count += 1
                        elif piece == ' ':
                            pass
                        elif piece == opposite:
                            new_opposite_count += 1
                if new_letter_count > letter_count + 1:
                    board = copy.deepcopy(new_board)
                    draw_board(board)
                    return False
                else:
                    print 'That move is not legal! Please make a different move.'
        elif move.lower() == 'pass':
            return True
        else:
            print 'Invalid input! Make sure your input matches the example shown.'
        
#Again, this function checks to see if a move is partially valid, makes the
# move, and then returns a copy of the board
def is_valid(row, column, letter):
    new_board = copy.deepcopy(board)
    if letter == 'X':
        opposite = 'O'
    else:
        opposite = 'X'
    #First: Check to see if the square is empty
    if board[row][column] == ' ':
        adjacent = []
        if column + 1 < 9:
            adjacent.append(new_board[row][column + 1])
        if column - 1 > 0:
            adjacent.append(new_board[row][column - 1])
        if row + 1 < 9:
            adjacent.append(new_board[row + 1][column])
        if row - 1 > 0:
            adjacent.append(new_board[row - 1][column])
        if row + 1 < 9 and column + 1 < 9:
            adjacent.append(new_board[row + 1][column + 1])
        if row + 1 < 9 and column - 1 > 0:
            adjacent.append(new_board[row + 1][column - 1])
        if row - 1 > 0 and column + 1 < 9:
            adjacent.append(new_board[row - 1][column + 1])
        if row - 1 > 0 and column - 1 > 0:
            adjacent.append(new_board[row - 1][column - 1])
        #Second: Check to see if there is an opposite piece in an adjacent square
        if opposite in adjacent:
            change_left(row, column, letter, new_board)
            change_right(row, column, letter, new_board)
            change_down(row, column, letter, new_board)
            change_up(row, column, letter, new_board)
            change_upleft(row, column, letter, new_board)
            change_upright(row, column, letter, new_board)
            change_downleft(row, column, letter, new_board)
            change_downright(row, column, letter, new_board)
        else:
            return None
    else:
        return None
    return new_board

#This is pretty self-explanatory
def play_again():
    while True:
        answer = raw_input('Would you like to play again (y/n)? ').lower()
        if answer.startswith('y'):
            return True
        else:
            print 'Have a nice day!'
            break

#Checks to see if scores.txt exists, and if it does, it loads scores from previous sessions.
# If it does not exist, it creates it.
def load_scores():
    scores = {}
    #finds the file path of trivia.py
    file_path = sys.argv[0]
    #gets the path of high_scores.txt (should be the same location)
    scores_path = file_path.replace('othello.py', 'scores.txt')
    #checks to see if high_scores.txt exists, and if it doesn't, it creates it
    if not os.path.isfile(scores_path):
        with open('scores.txt', 'w') as outfile:
            outfile.write('')
    #opens the file
    else:
        with open('scores.txt', 'rb') as infile:
            for line in infile:
                line = line.split(':')
                scores[line[0]] = line[1].strip()
    return scores

#Saves scores to scores.txt
def save_scores(scores):
    with open('scores.txt', 'w') as outfile:
        for score in scores:
            outfile.write('{}:{}/{}\n'.format(score, scores[score][0], scores[score][2]))

#Prints out scores
def print_scores(scores):
    for session in sorted(scores):
        print 'Session {}: Player 1 = {}, Player 2 = {}'.format(session, scores[session][0], scores[session][2])

#Checks to see if the board is filled, and if it is, it also finds the winner
def game_is_playing():
    global board
    count = 0
    for row in board:
        for piece in row:
            if piece == 'X' or piece == 'O':
                count += 1
    p1_count = 0
    p2_count = 0
    for row in board:
        for piece in row:
            if piece == 'X':
                p1_count += 1
            elif piece == 'O':
                p2_count += 1
    if count == 64:
        return True, p1_count, p2_count
    else:
        return False, p1_count, p2_count

#Opens a webpage with the rules to Othello
def rules():
    webbrowser.open('http://www.hannu.se/games/othello/rules.htm')


    
###################################################################################################
#The logic for checking and making a move begins here...
# There is one function for each of the eight directions that a move can go in.
# These are used in is_valid()
# Most are also just slight variations on each other
###################################################################################################
def change_left(row, column, letter, aboard):
    original_column = column
    if letter in aboard[row][1:column]:
        column -= 1
        new_row = aboard[row][:]
        valid = True
        while new_row[column] != letter:
            if new_row[column] == ' ':
                valid = False
                break
            else:
                new_row[column] = letter
                column -= 1
        if valid:
            aboard[row] = new_row
            aboard[row][original_column] = letter

def change_right(row, column, letter, aboard):
    original_column = column
    if letter in aboard[row][column+1:]:
        column += 1
        new_row = aboard[row][:]
        valid = True
        while new_row[column] != letter:
            if new_row[column] == ' ':
                valid = False
                break
            else:
                new_row[column] = letter
                column += 1
        if valid:
            aboard[row] = new_row
            aboard[row][original_column] = letter

def change_down(row, column, letter, aboard):
    row_num = row
    row += 1
    column_num = column
    column = []
    for num in range(9-row):
        column.append(aboard[row][column_num])
        row += 1
    count = 0
    for piece in column:
        if piece == ' ':
            break
        elif piece != letter:
            count += 1
        elif piece == letter and count == 0:
            break
        elif piece == letter:
            for num in range(count):
                column[num] = letter
    second_count = 1
    for piece in column:
        aboard[row_num + second_count][column_num] = piece
        second_count += 1
    aboard[row_num][column_num] = letter


def change_up(row, column, letter, aboard):
    row_num = row
    row -= 1
    column_num = column
    column = []
    for num in range(row):
        column.append(aboard[row][column_num])
        row -= 1
    count = 0
    for piece in column:
        if piece == ' ':
            break
        elif piece != letter:
            count += 1
        elif piece == letter and count == 0:
            break
        elif piece == letter:
            for num in range(count):
                column[num] = letter
    second_count = 1
    for piece in column:
        aboard[row_num - second_count][column_num] = piece
        second_count += 1
    aboard[row_num][column_num] = letter


def change_downright(row, column, letter, aboard):
    diagonal = []
    for num in range(9-row):
        if column + num == 9 or row + num == 9:
            break
        diagonal.append(aboard[row + num][column + num])
    diagonal = diagonal[1:]
    count = 0
    for piece in diagonal:
        if piece == ' ':
            break
        elif piece != letter:
            count += 1
        elif piece == letter and count == 0:
            break
        elif piece == letter:
            for num in range(count):
                diagonal[num] = letter
    second_count = 1
    for piece in diagonal:
        aboard[row + second_count][column + second_count] = piece
        second_count += 1
    aboard[row][column] = letter

def change_upleft(row, column, letter, aboard):
    diagonal = []
    for num in range(row):
        if column - num == 0 or row - num == 0:
            break
        diagonal.append(aboard[row - num][column - num])
    diagonal = diagonal[1:]
    count = 0
    for piece in diagonal:
        if piece == ' ':
            break
        elif piece != letter:
            count += 1
        elif piece == letter and count == 0:
            break
        elif piece == letter:
            for num in range(count):
                diagonal[num] = letter
    second_count = 1
    for piece in diagonal:
        aboard[row - second_count][column - second_count] = piece
        second_count += 1
    aboard[row][column] = letter
    
def change_downleft(row, column, letter, aboard):
    diagonal = []
    for num in range(9-row):
        if row + num == 9 or column - num == 0:
            break
        diagonal.append(aboard[row + num][column - num])
    diagonal = diagonal[1:]
    count = 0
    for piece in diagonal:
        if piece == ' ':
            break
        elif piece != letter:
            count += 1
        elif piece == letter and count == 0:
            break
        elif piece == letter:
            for num in range(count):
                diagonal[num] = letter
    second_count = 1
    for piece in diagonal:
        aboard[row + second_count][column - second_count] = piece
        second_count += 1
    aboard[row][column] = letter

def change_upright(row, column, letter, aboard):
    diagonal = []
    for num in range(row):
        if row - num == 0 or column + num == 9:
            break
        diagonal.append(board[row - num][column + num])
    diagonal = diagonal[1:]
    count = 0
    for piece in diagonal:
        if piece == ' ':
            break
        elif piece != letter:
            count += 1
        elif piece == letter and count == 0:
            break
        elif piece == letter:
            for num in range(count):
                diagonal[num] = letter
    second_count = 1
    for piece in diagonal:
        aboard[row - second_count][column + second_count] = piece
        second_count += 1
    aboard[row][column] = letter
###################################################################################################
###################################################################################################





#Controls the playing of the game
def play_game():
    global board
    turn = '1'
    game_is_over = False
    p1_pass = False
    p2_pass = False
    draw_board(board)
    while game_is_over == False:
        if turn == '1':
            p1_pass = get_player_move('1')
            turn = '2'
        elif turn == '2':
            p2_pass = get_player_move('2')
            turn = '1'
        game_is_over, p1_count, p2_count = game_is_playing()
        if p1_pass == True and p2_pass == True:
            print 'Are you sure you want to end the game? This game WILL STILL BE COUNTED if you do!'
            choice = raw_input('Type \'YES\' (all caps) in order to confirm: ')
            if choice == 'YES':
                game_is_over = True
            else:
                p1_pass = False
                p2_pass = False
                print 'The game will now resume play as normal.'
    board = copy.deepcopy(starting_board)
    if p1_count > p2_count:
        print 'Player 1 wins!'
        print 'Player 1 finished with {} pieces on the board.'.format(p1_count)
        print 'Player 2 finished with {} pieces on the board.'.format(p2_count)
        return 1
    elif p2_count > p1_count:
        print 'Player 2 wins!'
        print 'Player 1 finished with {} pieces on the board.'.format(p1_count)
        print 'Player 2 finished with {} pieces on the board.'.format(p2_count)
        return 2
    elif p1_count == p2_count:
        print 'The game was a draw! Nobody gets a point.'
        print 'Player 1 finished with {} pieces on the board.'.format(p1_count)
        print 'Player 2 finished with {} pieces on the board.'.format(p2_count)
        return 0
    


#Controls the welcome screen, and handles the scores
def main():
    scores = load_scores()
    p1_wins = 0
    p2_wins = 0
    sessions = []
    for num in scores.keys():
        sessions.append(int(num))
    if len(scores) == 0:
        session = 1
    else:
        session = max(sessions) + 1
    print 'Welcome to Othello!'
    print 'This is session #{}'.format(session)
    while True:
        print
        print '''1. Play a game against another person
2. View the rules of Othello
    (Opens a web page, and shows some things specific to this program.
3. View the scores of previous sessions
4. Exit'''
        choice = raw_input('Choose an option: ')
        if choice == '1':
            winner = play_game()
            if winner == 1:
                p1_wins += 1
            elif winner == 2:
                p2_wins += 1
            print 'Player 1 victories: {}'.format(p1_wins)
            print 'Player 2 victories: {}'.format(p2_wins)
        elif choice == '2':
            print
            print
            print '''Note that Player 1 is \'X\' (black), and Player 2 is \'O\.
There are some (rare) possibilities that can happen that I have NOT had time to program for.
For instance:
   It is possible to not be able to play on a turn
   It is possible for neither person to be able to play, and thus the game would end early
If either of the above end up happening, you have the ability to type 'pass' on your turn.
THIS IS ONLY LEGAL IF YOU CANNOT MOVE, but I haven't had time to program a check for that.
If BOTH players cannot move, and type 'pass' in a row, then they will have the option to
end the game. If they choose to do so, the current number of pieces on the board will be
used to determine a winner. This is how it works in a real game of Othello.

Also note that if you want to save the scores from this session, you must exit using the menu.'''
            time.sleep(2)
            rules()
        elif choice == '3':
            if len(scores) > 0:
                print_scores(scores)
            else:
                print 'There are no previous scores to show.'
        elif choice == '4':
            scores[str(session)] = '{}/{}'.format(p1_wins, p2_wins)
            save_scores(scores)
            break
        else:
            print 'Invalid input! Please choose a number between 1 and 3!'
            
    
main()




































