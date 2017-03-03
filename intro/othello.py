import copy
import re

board = [['This is here to make things easier, along with the first blank spot in each line'],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['dummy', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#Blank board:
##[['This is here to make things easier, along with the first blank spot in each line'],
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
def get_player_move(player, board):
    if player == '1':
        letter = 'X'
    else:
        letter = 'O'
    pattern = re.compile('[1-8] [1-8]')
    while True:
        move = raw_input('Player 1, choose the row and column you want to move in (ex. \'7 4\'): ')
        #Checks if the input matches the wanted pattern
        if pattern.match(move):
            move = move.split(' ')
            row = int(move[0])
            column = int(move[1])
        else:
            print 'Invalid input! Make sure your input matches the example shown.'
        new_board = make_move(row, column, letter, board)
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
                else:
                    opposite_count += 1
        for row in new_board:
            for piece in row:
                if piece == letter:
                    new_letter_count += 1
                elif piece == ' ':
                    pass
                else:
                    new_opposite_count += 1
        
        if letter_count + 1 == new_letter_count and opposite_count == new_opposite_count:
            print 'That move is not legal. Make a different move.'
        else:
            board = new_board
            draw_board(board)
            break
    


def make_move(row, column, letter):
    new_board = copy.copy(board)
    if letter == 'X':
        opposite = 'O'
    else:
        opposite = 'X'
    #First: Check to see if the square is empty
    if board[row][column] == ' ':
        #Second: Check to see if there is an opposite piece in an adjacent square
        if opposite in [new_board[row][column + 1],
                        new_board[row][column - 1],
                        new_board[row + 1][column],
                        new_board[row - 1][column],
                        new_board[row + 1][column + 1],
                        new_board[row + 1][column - 1],
                        new_board[row - 1][column + 1],
                        new_board[row - 1][column - 1]]:
            #Third: Check to see if a same piece is in the row, column, or diagonal,
            # AND isn't behind a same piece
            change_left(row, column, letter, new_board)
            change_right(row, column, letter, new_board)
            change_down(row, column, letter, new_board)
            change_up(row, column, letter, new_board)
            change_upleft(row, column, letter, new_board)
            change_upright(row, column, letter, new_board)
            change_downleft(row, column, letter, new_board)
            change_downright(row, column, letter, new_board)
            return new_board


###################################################################################################
#The logic for checking and making a move begins here...
###################################################################################################
def change_left(row, column, letter, board):
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

def change_right(row, column, letter, board):
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

def change_down(row, column, letter, board):
    row_num = row
    row += 1
    column_num = column
    column = []
    for num in range(9-row):
        column.append(board[row][column_num])
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
        board[row_num + second_count][column_num] = piece
        second_count += 1
    board[row_num][column_num] = letter


def change_up(row, column, letter, board):
    row_num = row
    row -= 1
    column_num = column
    column = []
    for num in range(row):
        column.append(board[row][column_num])
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
        board[row_num - second_count][column_num] = piece
        second_count += 1
    board[row_num][column_num] = letter


def change_downright(row, column, letter, board):
    diagonal = []
    for num in range(9-row):
        if column + num == 9 or row + num == 9:
            break
        diagonal.append(board[row + num][column + num])
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
        board[row + second_count][column + second_count] = piece
        second_count += 1
    board[row][column] = letter

def change_upleft(row, column, letter, board):
    diagonal = []
    for num in range(row):
        if column - num == 0 or row - num == 0:
            break
        diagonal.append(board[row - num][column - num])
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
        board[row - second_count][column - second_count] = piece
        second_count += 1
    board[row][column] = letter
    
def change_downleft(row, column, letter, board):
    diagonal = []
    for num in range(9-row):
        if row + num == 9 or column - num == 0:
            break
        diagonal.append(board[row + num][column - num])
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
        board[row + second_count][column - second_count] = piece
        second_count += 1
    board[row][column] = letter

def change_upright(row, column, letter, board):
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
        board[row - second_count][column + second_count] = piece
        second_count += 1
    board[row][column] = letter
###################################################################################################
#And ends here...
###################################################################################################




















