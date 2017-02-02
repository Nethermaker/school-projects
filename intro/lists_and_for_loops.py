#LISTS AND FOR LOOPS

#Let's write a function that add three numbers and returns their sum.
def add_three(x,y,z):
    return x + y + z

def add_four(a, b, c, d):
    return a + b + c + d

#A list is a data type that is a collection of other objects.

numbers = [3, 8, 19, -4, 6]

superheroes = ['Batman', 'Superman', 'Deadpool', 'Spider-Man', 'Wonder Woman', 'Squirrel Girl']

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

print len(numbers) #There are 5 numbers in my list
print len(superheroes) #There are 6 superheroes in my list

print numbers[0] #3
print superheroes[2] #Deadpool
print superheroes[-1] #Squirrel Girl


#If I want to add something to a list after it has already been created,
# I use a function called .append()

superheroes.append('Ant Man')

#Notice that I DO NOT HAVE TO RESET THE VALUE OF THE LIST TO ADD SOMETHING TO IT!!!
# THIS IS DIFFERENT THAN STRINGS!
# When I call a function on a list, the list is automatically forever changed.
# This is called a MUTABLE data type.

#The count function counts the number of elements of a certain value
# in the list.

breakfast = ['spam', 'spam', 'spam', 'eggs', 'spam']
print breakfast.count('spam') #4
print breakfast.count('cereal') #0


#The index function returns the index of the location of an element.

print superheroes.index('Wonder Woman') #4


#The insert function takes a new element and a location and inserts
# that element at that location.

superheroes.insert(1, 'Hulk')
print superheroes


#The pop function will return an element AND get rid of that element.

hero = superheroes.pop(3)
print hero
print superheroes

#The remove function takes an element takes an element and removes it from the list.

breakfast.remove('spam')
print breakfast


#The sort function... well, it sorts.

#Smallest to largest
numbers.sort()
print numbers

#Alphabetically
superheroes.sort()
print superheroes





###################################################################################################

#In order to loop through lists, we use a type of loop called a FOR LOOP.

#A for loop is like an assembly line.

#It goes through every element in a list and performs some task on that element.
#It automatically will stop when it gets to the end of the list.

#I would like to take a list of numbers, add them all together, and
# return their sum.

def add_numbers(num_list):
    total = 0
    for number in num_list: #Go through each thing in num_list,
                            # and call it 'number'.
        total += number
    return total
        
#This next function will take a list of numbers, add ten to every number,
# and then return a NEW list of numbers.

def add_ten(num_list):
    new_list = []
    for number in num_list:
        new_list.append(number + 10)
    return new_list

#Write a function called double().
#It takes a list of numbers and returns a list of doubled numbers.

def double(num_list):
    new_list = []
    for number in num_list:
        new_list.append(number * 2)
    return new_list

#There is exactly one country in the world that ends with 'g'.
#What is it?

place_list = ['Georgia', 'Greece', 'Luxembourg', 'USA', 'Hong Kong']

#Write a function called ends_in_g().
#It takes a list of words and returns a list of only those words
# that end in 'g'.

#Hint 1: Needs a for loop
#Hint 2: Needs an if statement in said for loop
#Hint 3: You will need to check if the last letter is a 'g'.

def ends_in_g(place_list):
    new_list = []
    for country in place_list:
        if country.endswith('g'):
            new_list.append(country)

    return new_list


#Let's write a function called first_n_squares().
#It takes a number and it returns a list of all the squares from
# 1**2 to n**2.

#There is a built-in function called range().
# range() takes a starting number and an ending number,
# and returns all the numbers in between, EXCLUDING THE ENDING NUMBER.

#Written by myself
def first_n_squares(n):
    num_list = range(1, n+1)
    new_list = []
    for number in num_list:
        new_list.append(number ** 2)
    return new_list

#How Mr. Handelman does it
def first_n_squares2(number):
    squares = []
    for n in range(1, number + 1):
        squares.append(n ** 2)
    return squares

#Write a function called yell().
#This function will take a list of words and return all of the words
# in all caps.

def yell(word_list):
    new_list = []
    for word in word_list:
        new_list.append(word.upper())
    return new_list




#Write a function called yell_long().
#This function takes a list of words and capitalizes only the words
# that are longer than 4 letters.

def yell_long(word_list):
    new_list = []
    for word in word_list:
        if len(word) > 4:
            new_list.append(word.upper())
        else:
            new_list.append(word)
    return new_list

def yell_string(words):
    string = ''
    capitals = []
    for word in words:
        if len(word) > 4:
            string = string + word.upper() + ' '
        else:
            string = string + word + ' '
    return string












































