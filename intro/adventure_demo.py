#########################################
#                                       #
#             ADVENTURE DEMO            #
#                                       #
#########################################

import random
import time

def start():
    print 'Welcome to Labyrinth'
    color = raw_input('What is your favorite color? ')
    name = raw_input('What is your name? ')
    age = int(raw_input('How old are you? '))
    return story(color, name, age)

def story(color, name, age):
    print 'You awake in what appears to be a series of twisty passages, all alike.'
    time.sleep(0.5)
    print 'You can only remember that your name is {}.'.format(name)
    time.sleep(0.5)
    print 'You see a path before you and a path behind you.'
    time.sleep(0.5)
    path = raw_input('Would you like to go forward or backward (forward/backward)? ')
    if path.lower() == 'forward':
        return forward(color, age)
    elif path.lower() == 'backward':
        return backward(color, age)
    else:
        print 'Invalid choice!'
        return story(color, name, age)

def forward(color, age):
    print 'You decide to go forward.'
    print 'You come across a kitten in your travels.'
    print 'You decide to pet it, when it suddenly goes ballistic.'
    print 'It begins to scratch you mercilessly.'
    cat = raw_input('Do you choose to fight the cat or run away (fight/run)? ')
    if cat.lower() == 'fight':
        return fight(color, age)
    elif cat.lower() == 'run':
        return run(color, age)
    else:
        print 'Invalid choice!'
        return forward(color, age)

def backward(color, age):
    print 'You decide to go backward.'
    trap_door_chance = random.randint(0, 1)
    if trap_door_chance == 0:
        print 'You accidentally step on a trap door. The floor gives way.'
        print 'You land on a rusty spike. Tetanus death!'
    else:
        print 'You take a step and see that you narrowly missed a trap door.'
        print 'Phew!'
        return keep_going(color, age)

def keep_going(color,age):
    pass



def fight(color, age):
    pass

def run(color, age):
    pass


start()
