import math

#Area of a trapezoid
def trapezoid(b_one,b_two,height):
    return 0.5*(b_one + b_two)*height

#Fahrenheit to Celcius
def FtoC(temp):
    return (5.0/9.0)*(temp - 32)

#Choice problem (volume of a cone)
def volume_of_cone(radius,height):
    return math.pi * (radius**2.0) * (height/3.0)

####################################################

string = "Introduction to Python"

#4a-e
print string[:12]
print string[16:]
print string[13:15]
print string[2:6]
print string[:5] + string[12:16] + string[16:18]

#Arrrrr
def pirate(aye):
    #Make string lowercase
    aye = aye.lower()
    #Start sentence
    aye = "Arrr, " + aye
    #Replace 'you' with 'ye'
    aye = aye.replace('you', 'ye')
    aye = aye.replace('You', 'ye')
    #Replace punctuation
    aye = aye.replace('.', '')
    aye = aye.replace('?', '')
    aye = aye.replace('!', '')
    #Finish sentence
    aye = aye + ", ye landlubber!"
    return aye

#be positive
def be_positive(string):
    string = string.replace('not ', '')
    return string

#the rest
def the_rest(string, word):
    #Find the start of 'the rest' of the string by taking the index number of where 'word'
    #starts and adding the length of the word (and also adding 1 to account for spaces)
    start = string.index(word)
    count = len(word)
    end = start + count + 1
    return string[end:]

#Gibberish: Take each letter and replace it with its opposite (ex. a = z, b = y, etc.)
def gibberish(string):
    #make everything lowercase so this is easier
    string = string.lower()
    #replace the letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz .?!,'
    backwards = 'zyxwvutsrqponmlkjihgfedcba .?!,'
    translator = dict(zip(alphabet, backwards))
    new_word = ''
    for letter in string:
        new_word += translator[letter]
    return new_word
    



















