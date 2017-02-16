#DICTIONARIES

colors = ['blue', 'green', 'red', 'yellow']

#A list (if you recall) connects a thing with its location inside the list.

print colors[0] #connects the 0th item with the color 'blue'
print colors[1] #connects the 1st item with the color 'green'

#A dictionary is a data type that allows us to pair
# two different pieces of data together.

#To create a dictionary, we use CURLY BRACKETS.

grades = {'bob':92,
          'jen':84,
          'benjamin':100,
          'lindsay':96}

print grades['bob']
print grades['lindsay']

print grades

#A dictionary HAS NO ORDER! When we put things into it, we can't worry 
# about the order that we do so, because that order is not remembered.

#The first thing in each pair is called the KEY.
#The second thing in each pair is called the VALUE.

#{KEY:VALUE, KEY:VALUE, KEY:VALUE, ...}

#print grades[96]  This gives me a KeyError

#To add things to a dictionary, we use SQUARE BRACKETS as well.

grades['maya'] = 89

print grades

#Changing a value is done the same way.

grades['jen'] = 44

print grades

#############################
#USEFUL DICTIONARY FUNCTIONS#
#############################

#.items() returns a LIST of key/value items

print grades.items()

#.keys() returns a LIST of just the keys.

print grades.keys()

#.values() returns a LIST of just the values.

print grades.values()

print sum(grades.values())/float(len(grades.values()))

###################################################################################################

#Create a dictionary called numbers.
#The keys need to be the STRINGS '0' through '9' and
# the operation symbols +, -, *, /, =.
#The values need to be the ENGLISH EQUIVALENT.
#'0' -------> 'zero'

numbers = {'0':'zero',
           '1':'one',
           '2':'two',
           '3':'three',
           '4':'four',
           '5':'five',
           '6':'six',
           '7':'seven',
           '8':'eight',
           '9':'nine',
           '+':'plus',
           '-':'minus',
           '*':'times',
           '/':'divided_by',
           '=':'equals'}

def english_equation(equation):
    '''This function will take an english equation, e.g. "2 + 3 = 5',
and it will return a sentence, e.g. "Two plus three equals five."'''
    equation = equation.split()
    answer = []
    for entry in equation:
        answer.append(numbers[entry])
    return ' '.join(answer).capitalize() + '.'

#I would like to count all the 'a's in a sentence.

def count_a(sentence):
    return sentence.count('a')

def count_a(sentence):
    total = 0
    for letter in sentence:
        if letter == 'a':
            total += 1
    return total

#What if I wanted to get the letter count for EVERY SINGLE LETTER?

def count_letters(sentence):
    counter = {}
    for letter in sentence:
        if letter.lower() not in counter:
            counter[letter.lower()] = 1
        else:
            counter[letter.lower()] += 1
    return counter




































