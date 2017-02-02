#Functions

#A function is a piece of code that takes some amount of input (or
#no input at all) and returns some sort of output (or no output!).

def area_of_rectangle(length, width):
    return length * width

def area_of_triangle(width, height):
    #return 0.5 * width * height
    return width * height / 2.0


########################################################################################

#A string is a bunch of characters that are put together .
#These characters have no literal meaning. They are just what
#you see on the screen.

name = 'Handelman'
digits = '123456789'

#String indexing is getting a particular character from a string.

#In programming, when we count the characters in a string, we ALWAYS
#START FROM ZERO. We do NOT start from ONE.

print name[0] #print 'H'
print name[5] #print 'l'
print name[8] #print 'n'

#If I want to start from the end, I use negative numbers.

print name[-1] #print the last letter ('n')
print name[-2] #print the second to last letter ('a')

#String slicing: Getting a chunk of the string (1 or more characters).

#Like indexing, but you give it the starting location, then a colon (:),
#then ONE MORE than the ending location.

print name[0:4]

#Print out the string 'elma'

print name[4:8]

#Print out 'dean'

print name[3:5] + name[7:9]

#The first number is not required. If you want to print
#from the beginning onward, you don't need the first number.

print name[:6] #print the first 6 letters of the name

#Similarly, th elast number is not required. You can leave it off
#if you just want to print to the end.

print name[2:] #print from letter 3 onwards

print name[:] #prints the whole thing!

#######################################################################################

#STRING FUNCTIONS

print len(name) #print out the length of the name

batman = 'Bruce Wayne'
print len(batman)

print name.upper() #capitalizes all letters
print name.lower() #lowercases all latters

title = 'of mice and men'

print title.title() #capitalizes the first letter of every word
print title.capitalize() #capitalizes the first letter of the string

print name.index('a') #prints the index number of the first matching substring
#print name.index('q') #error
#print name.index('h') #CAPITALIZATION MATTERS
print name.index('man') #prints the index number of where the substring starts

print name.count('a') #prints the number of matching substrings
print name.count('q') #returns 0 if not found (since there are no 'q's)

print name.swapcase() #reverses lowercase and uppercase

print name.replace('Hand', 'Foot') #replaces the first substring with the second
print name.replace('man', '') #removes 'man' from the string

#By the way, NOTHING WE HAVE DONE HAS CHANGED THE VALUE OF THE VARIABLE.

print name

#If you want to make sure that you have changed the value,
#put the new value back into a variable
name = name.upper()

print name.find('A') #find the index of 'A'
print name.find('q') #returns -1 if it can't be found

#Let's write a new function!

#Write a function to translate an English word into a pig latin word.

def pig_latin(word):
    first = word[0] #get the first letter of the word
    rest = word[1:] #get the rest of the word
    return rest + '-' + first + 'ay'





































