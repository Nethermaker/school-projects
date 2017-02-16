numbers = [5,28,13,1,-6,27,-11,4,-100,9]
languages = ['Java', 'Python', 'C', 'Ruby', 'Lisp', 'Javascript', 'Haskell', 'Prolog',
                'Scheme', 'Cobol', 'Pascal', 'BASIC', 'Visual Basic']
grades = [('Lisa Simpson',68), ('Bob Zmuda',100), ('Harry Houdini', 82), ('Kermit Frog', 95),
          ('Britney Spears', 91), ('Jason Voorhees', 42),('Jon Stewart', 96)]

# 1a) Write a line of code that will sort the numbers list numerically.

print sorted(numbers) # Write code inside the parentheses


# 1b) Write a line of code that will sort the numbers list numerically in REVERSE order.

print sorted(numbers, reverse=True) # Write code inside the parentheses


# 1c) Write a line of code that will sort the numbers list numerically by absolute value.
#     Hint: You will need to use the key argument of the sorted function.
#     Hint: Finding absolute value is built in! There is an abs() function.


print sorted(numbers, key=abs) # Write code inside the parentheses

# 2a) Write a function that takes a number and returns the PRODUCT of its digits.
#     For example, product(25) = 10, product(356) = 90, product(1234567890) = 0
#     Hint: We have already written this function for the sum of the digits on a previous
#           assignment. Find that code and make the necessary minor changes.

def product(number):
    total = 1
    number = str(number).replace('-', '')
    for digit in str(number):
        total *= int(digit)
    return total


# 2b) Write a line of code that will sort the numbers list by the product of their digits.
#     USE YOUR ANSWER FROM 2A.


print sorted(numbers, key=product) # Write code inside the parentheses


# 3a) Write a line of code that sorts the languages list by length.

print sorted(languages, key=len) # Write code inside the parentheses


# 4a) Write a function that counts the number of capital letters in a string.
#    Example: capitals('Lincoln, Nebraska') = 2, capitals('SHOUT') = 5


def capitals(string):
    total = 0
    for letter in string:
        if letter.isupper():
            total += 1
    return total


# 4b) Write a line of code that will sort the languages by the number of capitals
#     (BASIC should be last...as it deserves to be)

print sorted(languages, key=capitals) # Write code inside the parentheses


# 5a) A word value is the sum of the letters of the word, where A=1, B=2, C=3, and so on.
#     For example, MATH = 13 + 1 + 20 + 8 = 42, and PYTHON = 16 + 25 + 20 + 8 + 15 + 14 = 98
#     Write a function that takes a word and returns its word value.

def word_value(string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    for letter in string.upper():
        total += alphabet.find(letter) + 1
    return total


# 5b) Write a line of code that sorts the languages list by the word values.

print sorted(languages, key=word_value) # Write code inside the parentheses


# 6a) Write a function that takes a name/grade pair and returns the grade.

def get_grade(pair):
    return pair[1]

# 6b) Write a line of code that will sort the grades list by grade.

print sorted(grades, key=get_grade) # Write code inside the parentheses


# 7a) Write a function that takes a name/grade pair and returns just the LAST name.
#     You may assume that every name consists of a first and last name, in that order
#     Example: last_name(('John Doe', 84)) = 'Doe'

def get_last_name(pair):
    return pair[0].split()[1]

# 7b) Write a line of code that sorts the grades list by last name.

print sorted(grades, key=get_last_name) # Write code inside the parentheses
