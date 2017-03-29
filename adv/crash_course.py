print 'Welcome to Advanced Programming'

#Math
print 3 + 4
print 3 - 4
print 3 * 4
print 3 / 4

name = 'Handelman'

number = 27

number2 = 15

print 'My name is {}.'.format(name)

#your_name = raw_input('What is your name? ')
#print 'Hello there, {}!'.format(your_name)

def average_of_three(x,y,z):
    return (x + y + z) / 3.0

print average_of_three(58, 72, 91)

#String methods
word = 'programming'
print word[3]#print a 'g'
print word[-1]#print the last thing 'g'
print word[2:6]#prints 'o' through 'a'
print word[:5]
print word[5:]

word += ' class'
print word
print len(word) #length = 17
print name.lower()
print name.upper()
print name.count('a') #counts the 'a's in name
print name.index('d') #finds the 'd' (3)

#Conditional statements

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#You need elif if there are three or more possibilities

#Loops

def print_to_n(n):
    x = 1
    while x < n:
        print x
        x += 1

def keep_printing():
    while True:
        print 'This goes forever!'
        x = raw_input()
        if x != '':
            break

my_list = [1,2,3,4,5,6,7,8,9,10]

def add_one(lst):
    new_list = []
    for thing in lst:
        new_list.append(thing+1)
    return new_list

def add_to_n(n):
    return sum(range(1,n+1))


#Dictionaries

#A dictionary pairs off two values with each other.

capitals = {'Spain':'Madrid',
            'Norway':'Oslo',
            'Djibouti':'Djibouti'}

print capitals['Norway']

#File I/O

with open('demofile.txt', 'w') as my_file:
    my_file.write('This is a test.\n')
    my_file.write('I am Mr. {}.'.format(name))
    
with open('demofile.txt', 'rb') as my_file:
    string = my_file.read()

print string
































    
