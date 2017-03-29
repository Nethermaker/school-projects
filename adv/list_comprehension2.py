########################################################
#
# L I S T    C O M P R E H E N S I O N S
#
########################################################

# Use this space to explain what list comprehensions are
# used for.
# 
# A list comprehension is a way to generate a list in one line.
# I just have to tell the program what the list should look like and
# it will create it automatically.

# Generate a list of the first ten squares

##squares = []
##for i in range(1,11):
##    squares.append(i**2)
##print squares

squares = [i**2 for i in range(1,11)]


# Take a list, and multiply everything in the list by 3

list1 = [1,8,13,4,6,2,9,11,6]

new_list = [num*3 for num in list1]

# Take a list of words, and return a list of just the
# capitalized first letters of those words.

list2 = ["here's","a","horrible","acronym"]

acronym = [word[0].upper() for word in list2]

# Take a string make a list of all the characters in the string
# that are numbers.

sentence = "My social security number is 123-45-6789. It's true!"

ssn = [number for number in sentence if number.isdigit()]

# Add one to all the even numbers, do nothing to the odd numbers.

list3 = range(1,12)

new_numbers = [x + 1 if x%2==0 else x for x in list3]

# Create a list of all points between (1,1) and (10,10)

coordinates = [(x,y) for x in range(1,11) for y in range(1,11)]

deck = [(rank, suit) for rank in 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ') \
        for suit in 'Hearts Spades Diamonds Clubs'.split()]


# Create a dictionary (!) out of two lists.

names = ['Groucho','Chico','Harpo','Gummo','Zeppo']
grades = [89,42,61,88,46]

pairs = {name: grade for name, grade in zip(names, grades)}

pairs = dict(zip(names, grades))

# Solve the following problems using LIST COMPREHENSIONS.  All the problems
# are solvable using a good old-fashioned for loop, but then we wouldn't be
# learning something new, would we???

# 1. Write a function that takes a list of numbers, adds ten to every number,
# and returns a new list.

def add_ten(lst):
    return [x + 10 for x in lst]

# 2. Write a function that takes a number and generates the cubes from 1
# to that number cubed in a list.

def cube_list(number):
    return [x**3 for x in range(1, number+1)]

# 3. Write a function that takes a list of words, and returns a list
# of only the words that were of even length.

def even_length(lst):
    return [word for word in lst if len(word)%2==0]

# 4. Write a function that takes a list of words and returns the letters
# sorted (in a string! use the join function) if the word begins with 'a'
# through 'm' and reverse sorted if the word begins with 'n' through 'z'

def resort_letters(lst):
    return [''.join(sorted(word)) if word.lower()[0] in 'abcdefghijklmn' \
            else ''.join(sorted(word, reverse=True)) for word in lst]

# 5. The zip function is super neat and useful when you want to pair
# stuff together.  However, let's pretend it doesn't exist for a moment.
# Write a function that does exactly what zip does: it takes two lists
# and uses a list comprehension to pair elements from each list together.

def my_zip(list1,list2):
    return [(list1[num], list2[num]) for num in range(len(list1))]

# 6. There is another (super useful!) built-in function called enumerate()
# that takes a list and returns the elements of the list paired with their
# index in the list.
# enumerate(['zero','one','two'])
# ---> [(0,'zero'),(1,'one'),(2,'two')]
# Pretend enumerate doesn't exist and write a function that does the same thing.

def my_enumerate(lst):
    return [(index, lst[index]) for index in range(len(lst))]

# 7. Write a function that takes a word and returns a list of all
# versions of the word with one letter removed. For example, 'abcde'
# would return ['bcde','acde','abde','abcd']

def one_removed(lst):
    return [(list1[i], list2[i]) for i in range(len(list1))]

# 8. CHALLENGE! Write a function that takes a word and returns a list of all
# versions of the word with one letter added in any place in the word. For
# example, 'abcd' would return a list that contains 'aabcd', 'abycd',
# 'abcdz', 'abcpd', and all other possibilities. Hint: It's pretty similar
# to problem 7, but you will need a double for loop.

def one_added(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word += ' '
    return [word[:i] + x + word[i:] for i in range(len(word)) for x in alphabet]
    

# 9. CHALLENGE! Write a function that takes a word and returns a list
# of all versions of the word with one letter changed. For example,
# 'abc' would return ['bbc','cbc','dbc','ebc',...,'abx','aby','abz'].
# The list in this example would be 75 elements long because there
# are 25 different ways to change it. Hint: It's pretty similar to #8,
# but you will need a minor change and an if statement at the end.

def one_changed(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [word[:i] + x + word[i+1:] for i in range(len(word)) \
            for x in alphabet if x != word[i]]




