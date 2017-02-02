#Booleans and Conditionals

#A Boolean value is a value that is either True or False.

#A Boolean expression is an expression that evaluates to give True or False.

print 3 < 4 # "Is 3 less than 4?"
print 3 > 4 # "Is 3 greater than 4?"


#Here are some comparison operators that are built-in.

print 10 < 6 #Is 10 LESS THAN 6?
print 10 > 6 #Is 10 GREATER THAN 6?
print 10 <= 6 #Is 10 LESS THAN OR EQUAL TO 6?
print 10 >= 6 #Is 10 GREATER THAN OR EQUAL TO 6?

print 10 == 6 #Is 10 EQUAL TO 6?

#Wait, why does this have ==, not = sign?
#A single = is for assignment.
#A double == is to check if two things have the same value.
#If it's a command, use =, if it's a question, use ==.

print 10 != 6 #Is 10 NOT EQUAL TO 6?

#What if I need to check if more than one thing is True?

#If I need ALL conditions to be true, I use the keyword "and".

a = 5
b = 4

#I want to check if their sum is between 0 and 10 (exclusive).
a + b < 10 and a + b > 0 #This is True, because BOTH STATEMENTS are True
a + b < 8 and a + b > 0 #This is False, because ONE SIDE is False.

password = 'chimichanga'

password == 'chimichanga' or password == 'CHIMICHANGA'
#This statement is True because ONE of the statements is True.
#We use 'or' when we want at least one of the expressions to be valid.

#The following WILL NOT WORK!!!
password == 'chimichanga' or 'CHIMICHANGA'

#If I want to return the opposite truth value of an expression,
# I use the keyword 'not'

print password == 'bananas' #Obviously,this is False.
print not (password == 'bananas') #This is True.

#BUILT-IN BOOLEAN FUNCTIONS

#The 'in' keyword
#This checks to see if the value is a substring of a longer string.

state = 'Mississippi'

print 'a' in state #False, there is no 'a' in 'Mississippi'
print 'i' in state #True, there is an 'i' in 'Mississippi'
print 'ssiss' in state #True
print 'm' in state #False
print 'm' in state.lower() #True

password = 'programming123'
name = 'handelman'

print name.islower() # "Is this all lower-case?" True
print password.islower() #True

###################################################################################################

#Now that I know how to check if something is True or False,
# I want to be able to make a decision on whether a decision is True.
# We call this decision a CONDITIONAL STATEMENT. It's also called
# an 'if/then' statement.

def is_teenager(age):
    if age < 13:
        print 'You are too young to be a teenager!'
        return False
    elif 13 <= age <= 19:
        print 'You are a teenager!'
        return True
    else:
        print 'You are too old to be a teenager!'
        return False
    
##age = int(raw_input('Please enter your age: '))
##is_teenager(age)

#I am about to type two different functions that look like they do
# the same thing.

#Type them both in, and then figure out the difference.

def mystery(word):
    if 'q' in word:
        print 'There is a q in the word!'
    elif word[0].isupper():
        print 'The word starts with a capital letter!'
    else:
        print 'None of these things are true!'

def mystery2(word):
    if 'q' in word:
        print 'There is a q in the word!'
    if word[0].isupper():
        print 'The word starts with a capital letter!'
    else:
        print 'None of these things are true!'

#Write a function called fortune(number).
#The function takes a single number as input.
#Whether the number is 1, 2, or 3 gives a different fortune.
#If it isn't any one of those three numbers, then it asks you to pick
# a different number.

def fortune(number):
    if number == 1:
        return 'You will have good luck'
    elif number == 2:
        return 'You will have bad luck'
    elif number == 3:
        return 'You will not have luck'
    else:
        return 'Please pick a different number'


#Write a function called withdraw()

#This function takes two values:
#   1. An amount you would like to take out of the bank.
#   2. Your current bank balance.

#If you have enough money, say that the transaction was successful,
# then return the NEW balance after the money was withdrawn.

#If you don't have enough money, print an overdraw warning, then return the OLD balance.

def withdraw(amt, bal):
    if 0 <= amt <= bal:
        print 'Transaction successful!'
        return bal - amt
    elif amt < 0:
        print 'You cannot withdraw a negative amount.'
        return
    elif bal < 0:
        print 'You\'re already in debt, you are not allowed to withdraw.'
        return
    elif amt > bal:
        print 'You cannot withdraw more than you have.'
        return bal
    

#A password is valid if
#   1. It is at least 8 characters long
#   2. It has a digit in it
#   3. It has a capital letter in it

def is_valid(password):
    return len(password) >= 8 and not password.islower() and \
       ('0' in password or '1' in password or '2' in password)



































