#Zip and Enumerate

#I have two lists.
#I would like to add these two lists together, element by element.

#Ex: [1,2,3,4,5] and [8,4,11,9,6] --> [9,6,14,13,11]

#How can I do this using only what we currently know?

def add_lists(list1, list2):
    sum_list = []
    for index in range(len(list1)):
        sum_list.append(list1[index] + list2[index])
    return sum_list

#There must be a better way!

#The function zip() takes two lists and "zips" their
# elements together.

names = ['Bill', 'Leslie', 'Sara', 'Ben', 'Jessica']
ages = [68, 64, 28, 31, 34]

print zip(names, ages)

def add_lists2(list1, list2):
    sum_list = []
    for num1, num2 in zip(list1, list2):
        sum_list.append(num1 + num2)
    return sum_list

#This is a preview of an 'advanced' topic
def add_lists3(list1, list2):
    return [num1 + num2 for num1, num2 in zip(list1, list2)]

#I want to take a list of numbers,
# and I want to add their consecutive numbers together.

#[4,11,2,9,5] --> [15,13,11,14]

def add_consecutive(lst):
    sum_list = []
    for num1, num2 in zip(lst, lst[1:]):
        sum_list.append(num1 + num2)
    return sum_list

#When do you use zip()?
#You use it when the problem requires you to WALK THROUGH
# TWO LISTS AT THE SAME TIME, or requires you to look at TWO
# ELEMENTS OF THE ONE LIST AT THE SAME TIME.




###################################################################################################

#I would like to print out every elemnt of a list, AND
# its location in the list.

#Here's what I consider and "ugly" solution to that problem.

def print_index(lst):
    for index in range(len(lst)):
        print "{}:{}".format(index, lst[index])

#There's got to be a better way!

#The enumerate() function pairs an element with its index in the list.


print list(enumerate(names))
        


def print_index2(lst):
    for index, element in enumerate(lst):
        print "{}:{}".format(index, element)




#Let's only get the even indexed elements of the list.

def even_indices(lst):
    answer = []
    for index, element in enumerate(lst):
        if index % 2 == 0:
            answer.append(element)
    return answer

#When do you use enumerate?

#You use it when you need both the element AND its location.
































