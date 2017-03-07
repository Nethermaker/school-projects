import copy
import re
import sys
import os.path
import webbrowser

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


scores = {}

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


def draw_board(board):
    print '  1 2 3 4 5 6 7 8'
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

   
#I have decided that for the sake of simplicity and my sanity, player 1 will always be X

#NOTE TO SELF: CHANGE THIS TO LETTER AND ROW (ex. 'd4', 'a7', etc.)
# if time allows...
def get_player_move(player):
    global board
    if player == '1':
        letter = 'X'
        opposite = 'O'
    else:
        letter = 'O'
        opposite = 'X'
    pattern = re.compile('[1-8] [1-8]')
    while True:
        move = raw_input('Player {}, choose the row and column you want to move in (ex. \'7 4\'): '.format(player))
        #Checks if the input matches the wanted pattern
        if pattern.match(move):
            move = move.split(' ')
            row = int(move[0])
            column = int(move[1])
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
                if opposite_count == new_opposite_count:
                    #THIS ISN'T WORKING CORRECTLY
                    print 'That move is not legal. Make a different move.'
                else:
                    board = new_board
                    draw_board(board)
                    break
        else:
            print 'Invalid input! Make sure your input matches the example shown.'
        

def is_valid(row, column, letter):
    new_board = copy.copy(board)
    if letter == 'X':
        opposite = 'O'
    else:
        opposite = 'X'
    #First: Check to see if the square is empty
    if board[row][column] == ' ':
        adjacent = []
        #new_board[row][column + 1],
        #new_board[row][column - 1],
        #new_board[row + 1][column],
        #new_board[row - 1][column],
        #new_board[row + 1][column + 1],
        #new_board[row + 1][column - 1],
        #new_board[row - 1][column + 1],
        #new_board[row - 1][column - 1]
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
            #draw_board(new_board)
            change_right(row, column, letter, new_board)
            #draw_board(new_board)
            change_down(row, column, letter, new_board)
            #draw_board(new_board)
            change_up(row, column, letter, new_board)
            #draw_board(new_board)
            change_upleft(row, column, letter, new_board)
            #draw_board(new_board)
            change_upright(row, column, letter, new_board)
            #draw_board(new_board)
            change_downleft(row, column, letter, new_board)
            #draw_board(new_board)
            change_downright(row, column, letter, new_board)
            #draw_board(new_board)
        else:
            return None
    else:
        return None
    return new_board

def play_again():
    while True:
        answer = raw_input('Would you like to play again (y/n)? ').lower()
        if answer.startswith('y'):
            return True
        else:
            print 'Have a nice day!'
            break

def load_scores():
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

def save_scores():
    with open('scores.txt', 'w') as outfile:
        for score in scores:
            outfile.write('{}:{}/{}\n'.format(score, scores[score][0], scores[score][2]))


def print_scores():
    for session in sorted(scores):
        print 'Session {}: Player 1 = {}, Player 2 = {}'.format(session, scores[session][0], scores[session][2])

def game_is_playing():
    count = 0
    for row in board:
        for piece in row:
            if piece == 'X' or piece == 'O':
                count += 1
    if count == 64:
        return True
    else:
        return False
        
def rules():
    webbrowser.open('http://www.hannu.se/games/othello/rules.htm')


    
###################################################################################################
#The logic for checking and making a move begins here...
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
#And ends here...
###################################################################################################



#Here comes the magic...


def play_game(board):
    turn = '1'
    game_is_over = False
    draw_board(board)
    while game_is_over == False:
        if turn == '1':
            get_player_move('1')
            turn = '2'
        elif turn == '2':
            get_player_move('2')
            turn = '1'
        game_is_over = game_is_playing()









































