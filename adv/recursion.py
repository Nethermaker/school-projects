###########################################################################
#
# R E C U R S I O N
#
###########################################################################

def repeat():
    #raw_input('Press Enter to continue.')
    print 'We must go deeper.'
    return repeat()

#What is recursion?
#Recursion is a method of 'looping' in which a function calls itself to proceed.

#A recursion function has two main part:
# 1) The base case: with what input will the function come to a stop
#   and finally return something?
# 2) The recursive case: Call the function again, but with different
#   (smaller) input.


# Sum of a list

def my_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + my_sum(lst[1:])

# Product of a list

def my_product(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[0] * my_product(lst[1:])

# Palindrome

def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

# Factorial

def my_factorial(number):
    if number == 1:
        return 1
    else:
        return number * my_factorial(number-1)

# Fibonacci
#This function will take a number n and return the nth fibonacci number

def fib(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)

def better_fib(number):
    pass

# Minimum element in a list

#Don't know if this really counts, but it works (if you don't have a number higher than the one below)
def my_min(lst, minimum=999999999999999999999999999999999999999999999999999999999999999999999999):
    if len(lst) == 0:
        return minimum
    elif lst[0] < minimum:
        return my_min(lst[1:], minimum=lst[0])
    else:
        return my_min(lst[1:], minimum=minimum)
    
# Length of a list...not allowed to use len()!!!!

def my_len(lst):
    if lst == []:
        return 0
    else:
        return 1 + my_len(lst[1:])

# Given a string, return the number of instances of a letter
# sandwiched by two similar letters, such as 'axa'. The letter
# in the middle must be different, so 'aaa' would not count as
# Sandwiches may overlap, so 'axaxa' would return 3, since 'axa'
# appears twice and 'xax' appears once.

def sandwiches(string):
    if len(string) < 3:
        return 0
    elif string[0] == string[2] and string[0] != string[1]:
        return 1 + sandwiches(string[1:])
    else:
        return sandwiches(string[1:])

# Challenge: sum of a nested list

def nested_sum(lst):
    pass


# Checks to see if a list is sorted or not and returns True.
# It must be recursive and MAY NOT use any sort function. For one reason
# it's trivial to do it with, and for another, it's less efficient for the
# computer to sort and then check than it is to just check if it's sorted.

def is_sorted(lst):
    if len(lst) <= 1:
        return True
    elif lst[0] < lst[1]:
        return is_sorted(lst[1:])
    else:
        return False

# Remove all instances of a character from a string:

def my_remove(string, char):
    if len(string) == 0:
        return ''
    elif string[0] == char:
        return my_remove(string[1:], char)
    else:
        return string[0] + my_remove(string[1:], char)

# Count the occurrences of a character in a string:

def my_count(string, char):
    if len(string) == 0:
        return 0
    elif string[0] == char:
        return 1 + my_count(string[1:], char)
    else:
        return my_count(string[1:], char)
    
    
# Challenge: Greatest common divisor. Takes two numbers and returns the
# largest number that is a divisor of both numbers.  To solve this one, look
# up the Euclidean Algorithm. Though this is a challenge, it can actually
# be written in probably the smallest amount of code of any problem.

def gcd(a, b):
    pass

# Take a number and find the sum of its digits.  You MAY NOT solve
# this one by turning the number into a string/list of numbers.

def digital_sum(n):
    if n < 10:
        return n
    else:
        return n%10 + digital_sum(n/10)

# Keep applying the digital sum until you are down to a single digit.
# For example, 2019 = 2 + 0 + 1 + 9 = 12 + 1 + 2 = 3
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(digital_sum(n))

# Hailstone sequence: If a number is even, divide it by 2 and keep
# going.  If a number is odd, then multiply it by 3 and add 1.  If the
# number is 1, then stop (since you will get caught in an endless loop of
# 1,4,2,1,4,2...)

def hailstone(n):
    print n
    if n == 1:
        return
    elif n%2 == 0:
        return hailstone(n/2)
    else:
        return hailstone((n*3)+1)


# Challenge: Returns True if an element is inside a list, EVEN IF that element is
# actually inside a list within that list (or a list in a list in a list), etc.

def nested_contains(lst, elem):
    pass


# Challenge: Takes a list that may or may not contain nested lists and "flattens"
# it...that is, it returns a list of all the elements at the top level.
# For example: flatten([1,[2,3,[4,5,6],7],8,[[[9]]]]


#I have no idea how to do any of these challenges
def flatten(lst, new_lst=[]):
    if len(lst) == 0:
        return new_lst
    else:
        if type(lst[0]) == list:
            return flatten(lst[0], new_lst=new_lst)
        else:
            return flatten(lst[1:], new_lst=new_lst.append(lst[0]))





















    
    
        
