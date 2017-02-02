import random
import time

#Begin the game and ask for the five pieces of information
def start():
    name = raw_input('What is your name? ')
    age = int(raw_input('What is your age? '))
    job = raw_input('What is your profession? ')
    return choose_a_weapon(name, age, job)

#Ask the user for the weapon they want to use
def choose_a_weapon(name, age, job):
    print 'Choose a weapon!'
    weapon = raw_input('Will you take a sword, a bow, or a smartphone (sword/bow/smartphone)? ').lower()
    if weapon == 'sword' or weapon == 'bow' or weapon == 'smartphone':
        return choose_a_number(name, age, job, weapon)
    else:
        print 'Invalid choice!'
        return choose_a_weapon(name, age, job)


#Ask the user for a number between 1 and 10. Make sure said number is between 1 and 10.
def choose_a_number(name, age, job, weapon):
    lucky_num = int(raw_input('Choose a number between 1 and 10: '))
    if lucky_num < 1:
        print 'That number is not valid.'
        return choose_a_number(name, age, job, weapon)
    elif lucky_num > 10:
        print 'That number is not valid.'
        return choose_a_number(name, age, job, weapon)
    else:
        return begin(name, age, job, weapon, lucky_num)

#Start the fun stuff
def begin(name, age, job, weapon, lucky_num):
    print '"Your name is {}, and you shall be the ruler of this world."'.format(name)
    print 'At least, that\'s what you think you heard before you fell asleep.'
    print 'You\'re pretty sure that {} isn\'t what your name used to be, but how can you be sure?'.format(name)
    print 'You are currently in the middle of a clearing in a dense forest.'
    choice = raw_input('Do you want to explore or remain here (explore/stay)? ')
    if choice.lower() == 'explore':
        return explore(age, job, weapon, lucky_num)
    elif choice.lower() == 'stay':
        return stay(age, job, weapon, lucky_num)
    else:
        print 'Invalid choice!'
        return begin(name, age, job, weapon, lucky_num)

def explore(age, job, weapon, lucky_num):
    print 'Since you can\'t decide which direction to move in, you decide to spin in circles.'
    print '{} seconds seems like a good amount of time to spin for'.format(lucky_num)
    time.sleep(lucky_num / 2)
    if lucky_num <= 5:
        return forward(age, job, weapon)
    else:
        return backward(age, job, weapon)

def forward(age, job, weapon):
    pass

def backward(age, job, weapon):
    pass
    


def stay(age, job, weapon, lucky_num):
    print 'You decide to stay in the clearing and wait for divine intervention.'
    chance = random.randint(0,2)
    if chance == 0:
        print 'Divine intervention takes the form of a bear.'
        return bear(age, job, weapon, lucky_num)
    elif chance == 1:
        print '"What are you doing? I tell you that you will rule the world and you sit down?"'
        print '"Clearly you are not cut out for this business"'
        print 'The air around you begins to hum with electricity.'
        print 'You get struck by a lightning bolt!'
        print 'You are toast.'
        return game_over()
    else:
        return sit_this_out(age, job, weapon)

def bear(age, job, weapon, lucky_num):
    pass

def sit_this_out(age, job, weapon):
    print 'Divine intervention decides to sit this one out.'
    print 'You are getting hungry now.'
    choice = raw_input('Would you like to search for food or starve to death (search/starve)? ')
    if choice.lower() == 'search':
        return search(age, job, weapon)
    elif choice.lower() == 'starve':
        print 'Starving to death sounds like more fun that ruling the world.'
        print 'You are a disappointment.'
        return game_over()
    else:
        return sit_this_out(age, job, weapon)
        
#For the very end, when all else is lost
def game_over():
    pass

#Begin the game
start()


































