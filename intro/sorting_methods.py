#SORTING METHODS!!!!!

numbers = [5, 9, -4, 23, 18, -12, 7]

names = ['Scott', 'Jessica', 'Charlotte', 'Quinn', 'Byron']

superheroes = [('Superman', 'Clark Kent'),
               ('Spider-Man', 'Peter Parker'),
               ('Punisher', 'Frank Castle'),
               ('Daredevil', 'Matt Murdock'),
               ('Wonder Woman', 'Diana Prince')]



#How does the sorted() function work by default?

print sorted(numbers) #default is numerical order

print sorted(names) #default is alphabetical

print sorted(superheroes) #alphabetical order by first in each pair




#I want to sort in reverse order

print sorted(numbers, reverse=True)




#But what if I want to sort in some way OTHER THAN THE DEFAULT?

#For example, I want to sort the names by length!

print sorted(names, key=len)

#Note: I did not use parentheses when using the function name.




#I would like to sort the numbers by their absolute value!

print sorted(numbers, key=abs)




#I would like to sort by the THIRD letter of everyone's name.

def third_letter(name):
    return name[2]

print sorted(names, key=third_letter)




#I want to sort alphabetically by the second thing in each pair of superheroes.

def second_in_pair(pair):
    return pair[1]

print sorted(superheroes, key=second_in_pair)




#Let's go a little bit harder.

words = ['eerie', 'strengths', 'sequoia', 'program', 'syzygy']

def vowel_count(word):
    #return sum(1 for letter in word if letter in 'aeiou')
    count = 0
    for letter in word:
        if letter in 'aeiou':
            count += 1
    return count

print sorted(words, key=vowel_count)




#I can use the functions max() and min() in a very similar way!

print min(numbers)

print min(numbers, key=abs)













































