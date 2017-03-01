import copy
import re

board = [['This is here to make things easier, along with the first blank spot in each line'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' '],
         [' ', ' ', ' ', 'X', 'O', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


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
def get_player_move(player, board):
    if player == '1':
        letter = 'X'
        pattern = re.compile('[1-8] [1-8]')
        is_valid_move = False
        while is_valid_move == False:
            move = raw_input('Player 1, choose the row and column you want to move in (ex. \'7 4\'): ')
            #Checks if the input matches the wanted pattern (it's extremely picky, but it works
            if pattern.match(move):
                move = move.split(' ')
                is_valid_move = valid_move(move, letter)
            else:
                print 'Invalid Move! Make sure that your move matches the format shown.'
                
            
            
        #check_if_valid(int(row), int(column), board)
        return row, column
    else:
        letter = 'O'


def valid_move(move, letter):
    if letter == 'X':
        opposite = 'O'
    else:
        opposite = 'X' 
    row = int(move[0])
    column = int(move[1])
    #First: Check to see if the square is empty
    if board[row][column] == ' ':
        #Second: Check to see if there is an opposite piece in an adjacent square
        if 'O' in [board[row][column + 1],
                   board[row][column - 1],
                   board[row + 1][column],
                   board[row - 1][column],
                   board[row + 1][column + 1],
                   board[row + 1][column - 1],
                   board[row - 1][column + 1],
                   board[row - 1][column - 1]]:
            #Third: Check to see if a same piece is in the row, column, or diagonal,
            # AND isn't behind a same piece
            return True


###################################################################################################
#The logic for checking and making a move begins here...
###################################################################################################
def change_left(row, column, letter):
    original_column = column
    if letter in board[row][1:column]:
        column -= 1
        new_row = board[row][:]
        valid = True
        while new_row[column] != letter:
            if new_row[column] == ' ':
                valid = False
                break
            else:
                new_row[column] = letter
                column -= 1
        if valid:
            board[row] = new_row
            board[row][original_column] = letter

def change_right(row, column, letter):
    original_column = column
    if letter in board[row][column+1:]:
        column += 1
        new_row = board[row][:]
        valid = True
        while new_row[column] != letter:
            if new_row[column] == ' ':
                valid = False
                break
            else:
                new_row[column] = letter
                column += 1
        if valid:
            board[row] = new_row
            board[row][original_column] = letter

def change_down(row, column, letter):
    row_num = row
    row += 1
    column_num = column
    column = []
    for num in range(9-row):
        column.append(board[row][column_num])
        row += 1
    print column
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
            print column
    second_count = 1
    for piece in column:
        board[row_num + second_count][column_num] = piece
        second_count += 1
    board[row_num][column_num] = letter


def change_up(row, column, letter):
    row_num = row
    row -= 1
    column_num = column
    column = []
    for num in range(row):
        column.append(board[row][column_num])
        row -= 1
    print column
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
            print column
    second_count = 1
    for piece in column:
        board[row_num - second_count][column_num] = piece
        second_count += 1
    board[row_num][column_num] = letter


def change_downright(row, column, letter):
    diagonal = []
    for num in range(9-row):
        diagonal.append(board[row + num][column + num])
    diagonal = diagonal[1:]
    print diagonal
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
            print diagonal
    second_count = 1
    for piece in diagonal:
        board[row + second_count][column + second_count] = piece
        second_count += 1
    board[row][column] = letter

def change_upleft(row, column, letter):
    diagonal = []
    for num in range(row):
        diagonal.append(board[row - num][column - num])
    diagonal = diagonal[1:]
    print diagonal
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
            print diagonal
    second_count = 1
    for piece in diagonal:
        board[row - second_count][column - second_count] = piece
        second_count += 1
    board[row][column] = letter
    
def change_downleft(row, column, letter):
    diagonal = []
    for num in range(9-row):
        diagonal.append(board[row + num][column - num])
    diagonal = diagonal[1:]
    print diagonal
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
            print diagonal
    second_count = 1
    for piece in diagonal:
        board[row + second_count][column - second_count] = piece
        second_count += 1
    board[row][column] = letter

def change_upright(row, column, letter):
    diagonal = []
    for num in range(row):
        diagonal.append(board[row - num][column + num])
    diagonal = diagonal[1:]
    print diagonal
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
            print diagonal
    second_count = 1
    for piece in diagonal:
        board[row - second_count][column + second_count] = piece
        second_count += 1
    board[row][column] = letter
###################################################################################################
#And ends here...
###################################################################################################




















