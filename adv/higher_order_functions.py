###################################################
#
# HIGHER ORDER FUNCTIONS!
#
###################################################

import math
# Higher order functions are functions that take another function as input
#  and then use that function to perform a task


# We've seen sorted before...

lst = [1,-2,0, -3, 4, -8]

# I want to sort these by their absolute values, NOT by their normal values

#print sorted(lst, key=abs)


words = ['how','I','love','a','great','challenge']

# I want to sort these by their length.

#print sorted(words, key=len)


# But what if there's not a built in function that gives me the values I want?
# That's where the lambda keyword comes into play.

# What if I want to sort words by their second letter?

#def second_letter(word):
#    return word[1]

names = ['Superman', 'Batman', 'Aquaman', 'Wonder Woman', 'Flash']

#print sorted(names, key=second_letter)

print sorted(names, key=lambda x: x[1])

# This works exactly the same for the max and min functions: I can decide
# what the criteria for "max" and "min" actually mean, and use that instead
# of the default value.


print max(names, key=lambda x: x[1])


# The map function is an EVEN SHORTER way to create new lists.
# It takes a function and a list, and applies the function to every
# element in the old list and returns a new list.

# Let's say I want to change all the numbers in a list into strings.
# I COULD write a for loop to do this:

number_lst = [1,2,3,4,5]
new_lst = []
for number in number_lst:
    new_lst.append(str(number))

# I could do this in a list comprehension:

number_lst = [1,2,3,4,5]
new_list = [str(x) for x in number_lst]

# Or I can map the str function onto the number_lst using map:

new_list = map(str, number_lst)

# Now I want to take a list of numbers and add 10 to every number. There
# is no built in function that does that, so I can write my own on the fly.

number_list = [5,28,19,47,100,-6]
add_ten = map(lambda x: x+10, number_list)

# The filter function takes a function and a list and returns every item in
# the list that passes a certain test.

# I want to take a list of numbers and return only the numbers that are greater
# than ten.

greater_than_ten = filter(lambda x: x>10, number_list)

# The reduce function takes a function and a list and walks through the elements
# of the list in pairs, applying the function to reduce them into one value, and
# then ending up with a single value at the end.

# I want to take a list of numbers and return their sum.

add_list = reduce(lambda x,y: x+y, number_list)

#####################################################################

# The following problems can "generally" be done in one line of code.
# Make good use of the sorted, max, min, map, filter, and reduce functions!
# The lambda keyword will also come in handy.

# 1. Write a function that takes a list of words and returns the list sorted by
# their last letter.

def last_letter(lst):
    return sorted(lst, key=lambda x: x[-1])


# 2. Write a function that takes a list of numbers and returns a list of their
#    opposites. (Ex: 5 --> -5)

def opposite(lst):
    return map(lambda x: x-(x*2), lst)


# 3. Write a function that takes a list and returns the word in the list that has
# the smallest number of vowels.

def least_vowels(lst):
    return min(lst, key=lambda x: sum(x.count(vowel) for vowel in 'aeiou'))
                               
# 4. Write a function that takes a list and returns a list of only the elements
# that were made up of only letters.

def only_letters(lst):
    return filter(lambda x: x.isalpha(), lst)

# 5. Write a function that takes  a list of numbers and returns a list of only
# the even numbers.

def only_evens(lst):
    return filter(lambda x: x%2==0, lst)

# 6. Write a function that takes a list of temperatures in Celsius and returns
# a list of temperatures that are in Fahrenheit.

def c_to_f(lst):
    return map(lambda x: x*(9/5.0) + 32.0, lst)

# 7. Write a function that takes a list of words and returns only the words that have
# no repeated letters.

def no_repeats(lst):
    return filter(lambda x: max([x.count(letter) for letter in x]) < 2, lst)

# 8. Write a function that takes a list of numbers and returns their product.

def product(lst):
    return reduce(lambda x,y: x*y, lst)

# 9. Write a function that takes a list an returns the item that appears the most.
# CHALLENGE: Do it using the reduce function.

def most(lst):
    return max(lst, key=lst.count)    

# 10. Function that finds the largest one, but use reduce

def max_reduce(lst):
    return reduce(lambda x,y: x if x>y else y, lst)





