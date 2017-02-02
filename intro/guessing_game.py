import random
import time

#Editor's Notes:
# All challenges have been met
# High score is only for the single-player mode
# I didn't put in very many checks to stop errors, so if you try to break it, it probably will break
# Overall, I'm pretty happy with the way this turned out

def start(high_score):
    print 'Welcome to the guessing game!'
    print 'Please choose a mode: 1P, 2P, or CPU.'
    mode = raw_input('Enter your choice: ')
    if mode.lower() == '1p':
        return one_player(high_score)
    elif mode.lower() == '2p':
        return two_player(high_score)
    elif mode.lower() == 'cpu':
        return computer(high_score)
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
    print 'Note that getting a hint counts for 2 attempts.'
    while True:
        guess = raw_input('Enter a number, or ask for a \'hint\': ')
        if guess.lower() == 'hint':
            hint(secret_num)
            attempts += 2
        elif int(guess) > secret_num:
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

def hint(secret_num):
    if (secret_num % 2) == 0:
        print 'The number is divisible by 2.'
        return
    elif (secret_num % 3) == 0:
        print 'The number is divisible by 3.'
        return
    else:
        for number in range(2, secret_num):
            prime = secret_num % number
            if prime > 0:
                pass
            elif prime == 0:
                print 'The number is not divisible by 2 or 3, and is not a prime.'
                return
        print 'The number is prime.'
        return


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

def computer(high_score):
    secret_num = int(raw_input('Enter a number between 1 and 100 for the computer to guess: '))
    if secret_num > 100 or secret_num < 1:
        print 'Invalid choice!'
        return computer(high_score)
    else:
        #Got this working more or less perfectly, I've only seen it take 7 tries at most, so I guess I win?
        #Guesses the average of the possible values (starting at 1-100) and adjusts accordingly
        guess = 50
        attempts = 0
        min_range = 1
        max_range = 100
        while True:
            time.sleep(1)
            print 'I guess {}.'.format(guess)
            if guess > secret_num:
                print 'That was too high!'
                max_range = guess
                guess = (min_range + max_range) / 2
                attempts += 1
            elif guess < secret_num:
                print 'That was too low!'
                min_range = guess
                guess = (min_range + max_range) / 2
                attempts += 1
            else:
                attempts += 1
                print 'I got it right!'
                print 'It took me {} tries.'.format(attempts)
                return end(high_score, 'computer')

def end(high_score, mode):
    choice = raw_input('Would you like to play again, choose a new mode, or quit (again/mode/quit)? ')
    if choice.lower() == 'again':
        if mode == 'one_player':
            return one_player(high_score)
        elif mode == 'two_player':
            return two_player(high_score)
        elif mode == 'computer':
            return computer(high_score)
    elif choice.lower() == 'mode':
        return start(high_score)
    elif choice.lower() == 'quit':
        pass
    else:
        print 'Invalid choice!'
        return end(high_score, mode)


start(0)




















