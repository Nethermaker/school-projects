print 'This is programming class'
print 'My name is Mr. Handelman'
print 5 + 6

#This is a comment. None of this code gets evaluated.
#We write comments to explain what is going on in our program!

print "I can use two quotation marks too!"
print '"This doesn\'t work," she said.'

#Use three quotation marks in a row when you want to print something long!

print """There once was a man from Nantucket.
Blah blah blah.
This is another line.
Now I am done!"""

#A variable is a location that we can store a value.

name = 'Handelman'
age = 33
age = age + 1
age += 1 #This means the same thing as the line above.

#How do we print variables?
#There is a good way and a bad way.
#Here's the bad way.

print 'My name is Mr. ' + name + ' and I am ' + str(age) + ' years old.'

#Here's the good way.

print 'My name is Mr. {} and I am {} years old.'.format(name, age)

#To get input from a user, we need to use the raw_input() function.
#The raw_input() function will wait for the user to type something,
#and then will return what they type as a string.

food = raw_input("What is your favorite food? ")
print "{}? That is soooooo tasty!".format(food)

#Writes some code that will ask the user what their IQ is.
#Whatever they type, the computer should brag that its
#IQ is 10 points higher.

iq = int(raw_input("What is your IQ? "))
print "{}? Mine is {}!".format(iq, iq + 10)

#Write some code that will ask the user for the side
#length of a square.
#The program will then say "The area of the square is ___"

side = float(raw_input("What is the side length of the square? "))
print "{} is the area of the square.".format (side**2)
