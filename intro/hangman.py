import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
  ======''','''

  +---+
  |   |
  O   |
      |
      |
      |
  ======''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
  ======''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
  ======''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
  ======''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
  ======''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
  ======''']


#These words were shamelessly stolen from:
# https://answers.yahoo.com/question/index?qid=20080510101849AAN28jL
words = 'abruptly affix askew axiom azure bagpipes bandwagon banjo \
bayou bikini blitz bookworm boxcar boxful buckaroo buffalo buffoon \
cobweb croquet daiquiri disavow duplex dwarves equip exodus fishhook fixable \
foxglove galaxy galvanize gazebo gizmo glowworm guffaw haiku haphazard hyphen \
icebox injury ivory ivy jaundice jawbreaker jaywalk jazzy jigsaw jiujitsu jockey \
jovial joyful juicy jumbo kazoo keyhole khaki kilobyte kiosk kiwifruit knapsack \
larynx luxury marquis megahertz microwave mystify nightclub nowadays numbskull \
ovary oxidize oxygen pajama peekaboo pixel pizazz pneumonia polka quartz quiz \
quorum razzmatazz rhubarb rickshaw schizophrenia sphinx spritz squawk subway \
swivel topaz unknown unworthy unzip uptown vaporize vixen vodka vortex walkway \
waltz wavy waxy wheezy whiskey whomever wimpy wizard woozy xylophone yachtsman \
yippee youthful zephyr zigzag zilch zodiac zombie'.split()

def get_random_word(word_list):
    return random.choice(word_list)

def display_board(HANGMANPICS, missed_letters,
                  correct_letters, secret_word):
    print HANGMANPICS[len(missed_letters)]
    print
    print 'Missed letters:',
    for letter in missed_letters:
        print letter,
    print
    for letter in secret_word:
        if letter in correct_letters:
            print letter,
        else:
            print '_',
    print

#Write a function called get_guess(already_guessed).

#It will take as input a string of already guessed letters.

#Ask the user to type in a letter.
#Make sure that the following things are True:
#1. If they enter more than one letter, tell them to enter a single letter
#2. If they enter an already guessed letter, tell them to pick a different one.
#3. If they pick something that is NOT A LETTER, tell them to pick a letter!
#Hint: The function .isalpha() will help you here.
#Loop until they pick something that is valid, then return that letter.


def get_guess(already_guessed):
    while True:
        guess = raw_input('Please guess a letter: ').lower()
        if len(guess) > 1:
            print 'Please guess only a SINGLE letter.'
        elif guess in already_guessed:
            print 'Please guess a letter that hasn\'t been already guessed.'
        #elif guess.isalpha() == False:
        elif not guess.isalpha():
            print 'Please guess a LETTER!'
        else:
            return guess

#Will return True or False depending on whether they want to play again
def play_again():
    answer = raw_input("Do you want to play again (yes/no)? ")
    return answer.lower().startswith('y')

###################################################################################################

def main():
    print 'H A N G M A N'
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words) #GET THE RANDOM WORD
    game_is_done = False #This is called a flag variable

    

    while True:
        display_board(HANGMANPICS, missed_letters,
                      correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)

        #CHECK IF THE GUESS IS CORRECT
        if guess in secret_word:
            correct_letters += guess
            #CHECK TO SEE IF I HAVE WON!
            found_all_letters = True
            for letter in secret_word:
                if letter not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print 'Yes! The secret word was {}! You have won.'.format(secret_word)
                game_is_done = True
        #CHECK TO SEE IF THE GUESS IS INCORRECT
        else:
            missed_letters += guess
            #CHECK TO SEE IF I HAVE LOST
            if len(missed_letters) >= 6:
                display_board(HANGMANPICS, missed_letters,
                              correct_letters, secret_word)
                print 'You lost! The secret word was {}!'.format(secret_word)
                game_is_done = True
        if game_is_done:
            if play_again():
                #RESET THE GAME
                missed_letters = ''
                correct_letters = ''
                secret_word = get_random_word(words)
                game_is_done = False
            else:
                print 'Have a wonderful day!'
                break
    














main()




























