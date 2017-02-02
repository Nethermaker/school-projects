import random
import time

#IN ORDER TO WIN
#LUCKY NUMBER > 5
#AGE <+ 10020
#EXPLORE > OLD MAN DOESN'T MATTER > WIN
#YOU CAN ALSO CHOOSE THE SMARTPHONE AS YOUR WEAPON, AND THEN STAY AT THE BEGINNING,
# AND IF YOU GET LUCKY (33%) AND CHOOSE TO FIGHT THE BEAR, THAT PUTS YOU ON THE BACKWARD() PATH.

#Begin the game and ask for the five pieces of information
def start():
    name = raw_input('What is your name? ')
    age = int(raw_input('What is your age? '))
    job = raw_input('What is your profession? ')
    #This next line was added in last second
    print 'For this next one, if you don\'t have a disk drive installed, just use the C drive. It won\'t affect anything.'
    drive = raw_input('What drive letter is your CD Drive located on (A/B/C/etc.)? ')
    return choose_a_weapon(name, age, job, drive)

#Ask the user for the weapon they want to use
def choose_a_weapon(name, age, job, drive):
    print 'Choose a weapon!'
    weapon = raw_input('Will you take a sword, a bow, or a smartphone (sword/bow/smartphone)? ').lower()
    if weapon == 'sword' or weapon == 'bow' or weapon == 'smartphone':
        return choose_a_number(name, age, job, weapon, drive)
    else:
        print 'Invalid choice!'
        return choose_a_weapon(name, age, job, drive)


#Ask the user for a number between 1 and 10. Make sure said number is between 1 and 10.
def choose_a_number(name, age, job, weapon, drive):
    lucky_num = int(raw_input('Choose a number between 1 and 10: '))
    if lucky_num < 1:
        print 'That number is not valid.'
        return choose_a_number(name, age, job, weapon, drive)
    elif lucky_num > 10:
        print 'That number is not valid.'
        return choose_a_number(name, age, job, weapon, drive)
    else:
        return begin(name, age, job, weapon, lucky_num, drive)

#Start the fun stuff
def begin(name, age, job, weapon, lucky_num, drive):
    print '"Your name is {}, and you shall be the ruler of this world."'.format(name[::-1].lower())
    print 'At least, that\'s what you think you heard before you fell asleep.'
    print 'You\'re pretty sure that {} isn\'t what your name used to be, but how can you be sure?'.format(name[::-1].lower())
    print 'You are currently in the middle of a clearing in a dense forest.'
    choice = raw_input('Do you want to explore or remain here (explore/stay)? ')
    if choice.lower() == 'explore':
        return explore(age, job, weapon, lucky_num, drive)
    elif choice.lower() == 'stay':
        return stay(age, job, weapon, lucky_num, drive)
    else:
        print 'Invalid choice!'
        return begin(name, age, job, weapon, lucky_num, drive)

#lucky_num is used here to determine which way you go
def explore(age, job, weapon, lucky_num, drive):
    print 'Since you can\'t decide which direction to move in, you decide to spin in circles.'
    print '{} seconds seems like a good amount of time to spin for'.format(lucky_num)
    if lucky_num <= 5:
        print "You end up facing in the direction you originally were facing anyways."
        return forward(age, job)
    else:
        print 'You end up facing away from the direction you originally were facing.'
        return backward(age, job, drive)

def forward(age, job):
    print 'You enter the dense forest and quickly realize that there is a path in front of you.'
    print 'As you follow it, the light from the sun quickly fades as the trees get closer together.'
    print 'You can barely see that up ahead, the path forks.'
    choice = raw_input('Which way do you go (left/right)? ')
    if choice.lower() == 'left':
        return left(age, job)
    elif choice.lower() == 'right':
        return right(age, job)
    else:
        print 'Invalid choice!'
        return forward(age, job)

def right(age, job):
    print 'You decide to go right.'
    print 'You can\'t see anything now, and are finding your way only by touch.'
    print 'This is unfortunate, as there is a bear trap just ahead.'
    print 'You step directly on it, and pain shoots through your leg.'
    print 'Despite your best efforts to break free, you are too weak.'
    print 'You are a bear.'
    return game_over()

def left(age, job):
    print 'You decide to go left.'
    print 'There is more light now, and you can see there is a boulder in the path ahead.'
    choice = raw_input('Would you like to climb over or turn around (over/around)? ')
    if choice.lower() == 'over':
        print 'You decide to try and climb over the boulder.'
        print 'You manage to get on top of it, and you rest for a moment.'
        print 'What you didn\'t realize is that there is a hill going down on the other side of the boulder.'
        print 'You decide to risk the drop, and break both your legs in the process.'
        print 'You lack the upper body strenght you would need to move yourself around now.'
        print 'You are doomed.'
        return game_over()
    elif choice.lower() == 'around':
        print 'You decide to return to the clearing.'
        print 'When you get back, you decide to just go straight in the direction you are facing.'
        return backward(age, job)
    else:
        print 'Invalid choice!'
        return left(age, job)
    
def backward(age, job, drive):
    print 'You enter the forest, and the light from above begins to dim.'
    print 'You can still see, but just barely.'
    print 'A small old man is sitting on a tree stump just ahead.'
    choice = raw_input('Do you approach, or continue on your way (approach/continue)? ')
    if choice.lower() == 'approach':
        return old_man(job, age, drive)
    elif choice.lower() == 'continue':
        return backward2(age)
    else:
        print 'Invalid choice!'
        return backward(age, job)

def old_man(job, age, drive):
    print 'The old man greets you as you approach.'
    print '"Ah, yes, yet another {}."'.format(job)
    print '"Here, you look thirsty, have this drink."'
    print 'You ask him what he means by that, but he refuses to elaborate.'
    print 'Instead, he asks you a question.'
    choice = raw_input('"Would you like a cup holder (yes/no)?" ')
    if choice.lower() == 'yes':
        print 'The old man looks pleased.'
        print '"Here you go!"'
        #This part opens your disk drive
        #I have no idea how this works, found it at
        #http://stackoverflow.com/questions/3174349/how-to-eject-cd-using-wmi-and-python
        #(also this only works if your disc drive is D:)
        #I could add a question back at the beginning asking for the location of the disk drive,
        # but I've decided it isn't worth the effort.
        import ctypes
        ctypes.windll.WINMM.mciSendStringW(u"open {}: type cdaudio alias {}_drive".format(drive.upper(),drive.lower()) , None, 0, None)
        ctypes.windll.WINMM.mciSendStringW(u"set {}_drive door open".format(drive.lower()), None, 0, None)
        print 'You continue on your way.'
        return backward2(age)
    if choice.lower() == 'no':
        print '"I see..."'
        return backward2(age)
    else:
        print 'Invalid choice!'
        return old_man(job, age, drive)

def backward2(age):
    print 'The foliage begins to clear up and you can see better now.'
    print 'You exit the forest and can see a large castle up ahead.'
    print 'As you walk towards the castle, you can clearly see the sign posted above the drawbridge.'
    print '"NOW ENTERING: THE WORLD"'
    time.sleep(3)
    print 'You\'re tempted to give up and lay down, as you have clearly been pranked by God...'
    time.sleep(2)
    print '...or whoever that was.'
    print 'As you think this, a voice booms out from everywhere around you.'
    print '"Ah, you\'ve finally made it! Come inside, I have many things to show you."'
    choice = raw_input('Do you go inside or give up (inside/give)? ')
    if choice.lower() == 'inside':
        return castle(age)
    elif choice.lower() == 'give':
        print 'You decide to give up on this sad excuse of a story.'
        print 'You lay down and wait for decomposition to begin.'
        print 'You are incredibly patient.'
        return game_over()
    else:
        print 'Invalid choice!'
        return backward2(age)

def castle(age):
    print 'You enter the castle\'s main hall, and see a figure sitting on the throne on the far end.'
    print 'The figure looks incredibly old.'
    print '"I have ruled this place for 10,000 years, and it has done well."'
    print 'You beg to differ, but you keep your mouth shut.'
    time.sleep(4)
    print '"As you can see, I am old. I need to find a worthy successor to be ruler of The World."'
    print '"You have proven yourself to be worthy to succeed me."'
    time.sleep(3)
    if age > 10020:
        print '"But wait! You are older than me! How is this possible?"'
        print '"You can\'t rule this place if you are older than me!"'
        print '"I\'ll just have to find someone else."'
        print 'You feel yourself begin to fade from existence.'
        print 'You are nothing.'
        return game_over()
    else:
        print 'The king steps off his throne, and takes off his crown.'
        print 'He hands you the crown, and falls over dead.'
        print 'You feel like this was a pretty big anti-climax.'
        print 'You are ruler of The World.'
        return win()
        
    

#This is the point of 3 divergences, and also the use of randomness. Each path has a 33% chance
def stay(age, job, weapon, lucky_num):
    print 'You decide to stay in the clearing and wait for divine intervention.'
    time.sleep(3)
    chance = random.randint(0,2)
    if chance == 0:
        print 'Divine intervention takes the form of a bear.'
        return bear(age, job, weapon)
    elif chance == 1:
        print '"What are you doing? I tell you that you will rule the world and you sit down?"'
        print '"Clearly you are not cut out for this business."'
        print 'The air around you begins to hum with electricity.'
        print 'You get struck by a lightning bolt!'
        print 'You are toast.'
        return game_over()
    else:
        print 'Divine intervention decides to sit this one out.'
        return sit_this_out(age, job, weapon)

def bear(age, job, weapon, drive):
    print 'The bear is in the clearing with you, eyeing you warily.'
    print 'It appears to be aggressive, and is walking slowly towards you.'
    choice = raw_input('Do you want to stay and fight, or run (fight/run)? ')
    if choice.lower() == 'run':
        print 'You try to turn and run, but the bear doesn\'t agree with you choice.'
        print 'It closes the gap quickly, and pins you down.'
        print 'You are bear food.'
        return game_over()
    elif choice.lower() == 'fight':
        return fight(age, job, weapon, drive)
    else:
        print 'Invalid choice!'
        return bear(age, job, weapon, drive)

def fight(age, job, weapon, drive):
    if weapon.lower() == 'sword':
        print 'You pull out your sword.'
        print 'The bear charges at you, and you chop off its head.'
        return sit_this_out(age, job, weapon)
    elif weapon.lower() == 'bow':
        print 'You pull out you bow and fire a warning shot.'
        print 'The bear doesn\'t really seem to care about your little stick.'
        print 'It closes the gap and pins you down before you have a chance to shoot again.'
        print 'You are bear food.'
        return game_over()
    elif weapon.lower() == 'smartphone':
        print 'You pull out your phone and throw it at the bear.'
        print 'The bear stops, clearly confused, and sniffs your phone.'
        print 'You take the opening and run for it. The bear doesn\'t follow.'
        return backward(age, job, drive)
        
        

def sit_this_out(age, job, weapon):
    print 'You are getting hungry now.'
    choice = raw_input('Would you like to search for food or starve to death (search/starve)? ')
    if choice.lower() == 'search':
        return search(age, job, weapon)
    elif choice.lower() == 'starve':
        print 'Starving to death sounds like more fun than ruling the world.'
        print 'You are a disappointment.'
        return game_over()
    else:
        print 'Invalid choice!'
        return sit_this_out(age, job, weapon)

def search(age, job, weapon):
    print 'You decide to go on a search for food.'
    print 'Your stomach\'s built-in compass sends you into the forest.'
    print 'You come across some berries that look like they might taste pretty good.'
    choice = raw_input('Do you want to eat or leave the berries (eat/leave)? ')
    if choice.lower() == 'eat':
        print 'As it turns out, these berries are poisonous.'
        print 'Your poor choice results in a horrible pain all over, followed shortly by death.'
        print 'You are no longer hungry.'
        return game_over()
    elif choice.lower() == 'leave':
        print 'These berries looked pretty tasty, but your instinct tells you they\'re not.'
        print 'You decide to return to the clearing and look for a way out of here.'
        return forward(age, job)
    else:
        print 'Invalid choice!'
        return search(age, job, weapon)
        
#For the very end, because you're bad
def game_over():
    print 'IT SEEMS THAT YOU HAVE DIED IN A SPECTACULAR WAY...'
    start_over = raw_input('WOULD YOU LIKE TO TRY AGAIN (Y/N)? ')
    if start_over.lower() == 'y':
        return start()
    elif start_over.lower() == 'n':
        return
    else:
        print 'Invalid choice!'
        return game_over()

#In case you manage to win
def win():
    print 'YOU HAVE SUCCEEDED IN YOUR TASK IN BECOMING RULER OF THE WORLD...'
    start_over = raw_input('CONGRAGULATIONS! WOULD YOU LIKE TO PLAY AGAIN (Y/N)? ')
    if start_over.lower() == 'y':
        return start()
    elif start_over.lower() == 'n':
        return
    else:
        print 'Invalid choice!'
        return game_over()

#Begin the game
start()


































