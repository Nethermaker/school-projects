import random

def start(high_score):
    print 'Welcome to the guessing game!'
    print 'Please choose a mode: 1P, 2P, or CPU.'
    mode = raw_input('Enter your choice: ')
    if mode.lower() == '1p':
        return one_player(high_score)
    elif mode.lower() == '2p':
        return two_player(high_score)
    elif mode.lower() == 'cpu':
        return computer()
    else:
        print 'Invalid choice!'
        return start(high_score)


def one_player(high_score):
    if high_score == 0:
        print 'High score not yet set.'
    else:
        print 'Current high score: {}.'.format(high_score)
    secret_num = random.randint(1,100)
    attempts = 0
    print 'I\'m thinking of a number between 1 and 100. Try and guess it!'
    while True:
        guess = raw_input('Enter a number: ')
        if int(guess) > secret_num:
            print 'That was too high!'
            attempts += 1
        elif int(guess) < secret_num:
            print 'That was too low!'
            attempts += 1
        elif int(guess) == secret_num:
            attempts += 1
            print 'You got it right!'
            print 'It took you {} tries to get it right.'.format(attempts)
            if high_score == 0:
                high_score = attempts
                print 'High score set!'
            else:
                if attempts < high_score:
                    high_score = attempts
                    print 'You got a new high score!'
            return end(attempts, 'one_player')


def two_player(high_score):
    secret_num = int(raw_input('Player 1, please enter a number between 1 and 100: '))
    if secret_num > 100 or secret_num < 1:
        print 'Invalid number!'
        return two_player()
    else:
        blanks = 0
        while blanks <= 100:
            print ''
            blanks += 1
        attempts = 0
        print 'Player 2 may begin guessing.'
        while True:
            guess = raw_input('Enter a number: ')
            if int(guess) > secret_num:
                print 'That was too high!'
                attempts += 1
            elif int(guess) < secret_num:
                print 'That was too low!'
                attempts += 1
            elif int(guess) == secret_num:
                attempts += 1
                print 'Player 2 got it right!'
                print 'It took Player 2 {} tries to get it right.'.format(attempts)
                return end(high_score, 'two_player')

def computer():
    pass

def end(high_score, mode):
    choice = raw_input('Would you like to play again, choose a new mode, or quit (again/mode/quit)? ')
    if choice.lower() == 'again':
        if mode == 'one_player':
            return one_player(high_score)
        elif mode == 'two_player':
            return two_player(high_score)
        elif mode == 'computer':
            return computer()
    elif choice.lower() == 'mode':
        return start(high_score)
    elif choice.lower() == 'quit':
        pass


start(0)




















