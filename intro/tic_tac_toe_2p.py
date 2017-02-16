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

def choose_random_move_from_list(board, moves_list):
    #The computer will get a list of moves to choose from.
    #It will go through all of them and find if any are valid.
    #Then, it chooses randomly from the valid moves.
    possible_moves = []
    for move in moves_list:
        if board[move] == ' ': #This is a SPACE, NOT and EMPTY STRING
            possible_moves.append(move)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        None

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    #TIC TAC TOE A.I.
    #1. Check to see if the computer can win!

    for number in range(1,10):
        board_copy = copy.copy(board) #Make a copy of the board
        if board_copy[number] == ' ':
            board_copy[number] = computer_letter #Make the move!
            if is_winner(board_copy, computer_letter):
                return number
    
    #2. Check to see if the computer can block a win!
    for number in range(1,10):
        board_copy = copy.copy(board) #Make a copy of the board
        if board_copy[number] == ' ':
            board_copy[number] = player_letter #Make the move!
            if is_winner(board_copy, player_letter):
                return number

    #3. If a corner is free, take it.
    move = choose_random_move_from_list(board, [1,3,7,9])
    if move != None:
        return move

    #4. If the center is free, take it.
    move = choose_random_move_from_list(board, [5])
    if move != None:
        return move

    #5. If an edge is free, take it.
    return choose_random_move_from_list(board, [2,4,6,8])

#############################################################
#                                                           #
#                        MAIN PROGRAM                       #
#                                                           #
#############################################################

def main():
    print 'Welcome to Tic-Tac-Toe!'
    player_num = raw_input('Would you like to play a 1-player or 2-player game (1/2)? ')
    if player_num == '1':
        one_player()
    elif player_num == '2':
        two_player()
    else:
        print 'Invalid choice!'
        return main()


def one_player():
    wins = 0
    losses = 0
    ties = 0
    while True:
        board = [' ']*10
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first() #Will either be 'player' or 'computer'
        print 'The {} will go first.'.format(turn)
        game_is_playing = True

        while game_is_playing:

            if turn == 'player':
                draw_board(board)
                move = get_player_move(board)
                board[move] = player_letter
                
                if is_winner(board, player_letter):
                    draw_board(board)
                    print 'Horray! You have won the game!'
                    wins += 1
                    game_is_playing = False
                elif board.count(' ') == 1:
                    draw_board(board)
                    print 'The game is a tie!'
                    ties += 1
                    game_is_playing = False
                else:
                    turn = 'computer'

            elif turn == 'computer':
                move = get_computer_move(board, computer_letter)
                board[move] = computer_letter #Make the move! (moron)

                if is_winner(board, computer_letter):
                    draw_board(board)
                    print 'The computer has beaten you. You lose!'
                    losses += 1
                    game_is_playing = False
                elif board.count(' ') == 1:
                    draw_board(board)
                    print 'The game is a tie!'
                    ties += 1
                    game_is_playing = False
                else:
                    turn = 'player'
        print 'Wins: {}'.format(wins)
        print 'Losses: {}'.format(losses)
        print 'Ties: {}'.format(ties)

        if not play_again():
            print 'Have a nice day!'
            break

def two_player():
    player1_wins = 0
    player2_wins = 0
    ties = 0
    while True:
        board = [' ']*10
        player1_letter = random.choice(['X', 'O'])
        if player1_letter == 'X':
            player2_letter = 'O'
        else:
            player2_letter = 'X'
        turn = random.choice(['player 1', 'player 2'])
        print '{} will go first.'.format(turn.capitalize())
        game_is_playing = True

        while game_is_playing:

            if turn == 'player 1':
                draw_board(board)
                move = get_player_move(board)
                board[move] = player1_letter
                
                if is_winner(board, player1_letter):
                    draw_board(board)
                    print 'Horray! Player 1 has won the game!'
                    player1_wins += 1
                    game_is_playing = False
                elif board.count(' ') == 1:
                    draw_board(board)
                    print 'The game is a tie!'
                    ties += 1
                    game_is_playing = False
                else:
                    turn = 'player 2'

            if turn == 'player 2':
                draw_board(board)
                move = get_player_move(board)
                board[move] = player2_letter
                
                if is_winner(board, player2_letter):
                    draw_board(board)
                    print 'Horray! Player 2 has won the game!'
                    player2_wins += 1
                    game_is_playing = False
                elif board.count(' ') == 1:
                    draw_board(board)
                    print 'The game is a tie!'
                    ties += 1
                    game_is_playing = False
                else:
                    turn = 'player 1'
        print 'Player 1 Wins: {}'.format(player1_wins)
        print 'Player 2 Wins: {}'.format(player2_wins)
        print 'Ties: {}'.format(ties)

        if not play_again():
            print 'Have a nice day!'
            break


main()
        



























