# Sorting Algorithms

import random
import time

my_list = range(10000)

random.shuffle(my_list)

#print sorted(my_list) #We have a way to sort information.

# But how did it do that?

###################################################################

# What does "efficiency" mean in terms of a program?

# 1. Running time. Does it take a really long time to run?

# 2. Resources. (Memory, Power)

# 3. Lines of code

# 4. Manpower

def is_sorted(lst):
    if len(lst) <= 1:
        return True
    else:
        return lst[0] <= lst[1] and is_sorted(lst[1:])

def stupid_sort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst

def dumb_sort(lst):
    number_list= [None] * 10000000
    for number in lst:
        number_list[number] = number
        sorted_list = []
    for thing in number_list:
        if thing:
            sorted_list.append(thing)
    return sorted_list

def insertion_sort(lst):
    new_list = [lst[0]]
    for element in lst[1:]:
        for index, new_element in enumerate(new_list):
            if element <= new_element:
                new_list.insert(index, element)
                found = True
                break
        else:
            new_list.append(element)
    return new_list

def selection_sort(lst):
    new_list = []
    length = len(lst)
    while len(new_list) != length:
        element = min(lst)
        lst.remove(element)
        new_list.append(element)
    return new_list

def merge(left, right):
    new_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            new_list.append(left.pop(0))
        else:
            new_list.append(right.pop(0))
    return new_list + left + right

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        middle = len(lst) / 2
        return merge(merge_sort(lst[:middle]), merge_sort(lst[middle:]))

                                
start = time.time()
answer = merge_sort(my_list)
end = time.time()

print 'It took {} seconds!'.format(end-start)




























