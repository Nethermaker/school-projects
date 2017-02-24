import copy
import re

board = [['This is here to make things easier, along with the first blank spot in each line'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
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

   
#I have decided the for the sake of simplicity and my sanity, player 1 will always be O


def get_player_move(player, board):
    if player == '1':
        letter = 'O'
        pattern = re.compile('[0-8], [0-8]')
        while True:
            move = raw_input('Choose the row and column you want to move in (\'row#, column#\')? ')
            #Checks if the input matches the wanted pattern (it's extremely picky, but it works
            if pattern.match(move):
                move = move.split(',')
                row = int(move[0])
                column = int(move[1])
                #valid = check_if_valid_move(row, column)
            else:
                print 'Invalid Move!'
                
            
            
        #check_if_valid(int(row), int(column), board)
        return row, column




















        
