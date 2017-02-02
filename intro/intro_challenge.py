# Problem 1
# Write a function called switch_ends() that takes a string
# and returns the string with the front and back letter switched
# Ex: switch_ends('part') -> 'tarp'
#     switch_ends('abcdefg') -> 'gbcdefa'
#     switch_ends('dog') -> 'god'

def switch_ends(string):
    first = string[0]
    last = string[-1]
    return last + string[1:-1] + first

# Problem 2
#
# Write a function called remove_vowels() that takes a string
# and returns the same string but with the vowels removed.
#
# Ex: remove_vowels('handelman') -> 'hndlmn'
#     remove_vowels('programming') -> 'prgrmmng'
#     remove_vowels('sequoia') -> 'sq'
#     remove_vowels('aeiou') -> ''

def remove_vowels(string):
    for letter in string:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            string = string.replace(letter, '')
    return string

# Problem 3
# Write a function called count_same() that takes two strings
# and returns the number of characters that are exactly the same.
# The two strings do not have to be the same length.
# HINT: Use zip to put the characters together
# Ex: count_same('smart', 'start') -> 4
#     count_same('handelman', 'handyman') -> 4
#     count_same('abcde','edcba') -> 1
#     count_same('abc', 'defghijk') -> 0

def count_same(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    count = 0
    for letter1, letter2 in zip(list1, list2):
        if letter1 == letter2:
            count += 1
    return count

# Problem 4
# Write a function called median() that takes a list of numbers
# It will return the median of the list of numbers. Remember, the median
# is the middle number of a set.  If there are an even number of numbers,
# then you take the two middle numbers and average them together.
# Hint: You will need to sort the list first, AND you will need to
# do different things whether or not the list has an even number
# or odd number of elements.
# Ex: median([1,2,3,4,5]) -> 3
# Ex: median([3,1,2,5,4]) -> 3
# Ex: median([1,3,5,7]) -> 4 (average of 3 and 5)
# Ex: median([]) -> 0

def median(num_list):
    pass

# Problem 5
# Write a function called double_letters() that takes a word
# and returns True if the word has double letters anywhere inside of it
# double_letters('balloon') -> True
# double_letters('Handelman') -> False
# double_letters('bookkeeper') -> True
# HINT: There are a handful of ways to do this. MY OPINION is that the
# easiest and cleanest ways are either to use the enumerate function
# or to make creative use of the zip function.

def double_letters(word):
    pass

# Problem 6
# Write a function called add_digits that takes a number and
# adds all the digits of that number together.
# Hint: You can do this completely mathematically for a challenge, but
# it might be easier if you turn the number into a string first.
# Example: add_digits(12345) -> 15
#          add_digits(5062) -> 13
#          add_digits(10000000000001) -> 2

def add_digits(number):
    num = str(number)
    lst = list(num)
    new_list = []
    for entry in lst:
        new_list.append(int(entry))
    return sum(new_list)
    

# Problem 7
# Write a function called add_sequence() that takes a number and
# adds its digits to get a new number. It then takes that number and adds
# its digits to get yet a new number. It will keep doing this until it returns
# a 1-digit number and then returns the 1-digit number.
# Example: add_sequence(12345) -> 6 (first 15, then 6)
#          add_sequence(987654) -> 3 (first 39, then 12, then 3)
#          add_sequence(1000001) -> 2 (just 2)

def add_sequence(number):
    while True:
        




























