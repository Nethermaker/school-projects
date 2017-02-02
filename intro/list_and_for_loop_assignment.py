# 1. Write a function called common_end() that takes two lists.
#    It will return True if the two lists either have the same
#    first element, the same LAST element, or both.

# common_end([1,2,3], [7,3]) ---> True
# common_end([1,2,3], [7,3,2]) ---> False
# common_end([1,2,3], [1,7]) ---> True

def common_end(list1, list2):
    if list1[0] == list2[0]:
        return True
    elif list1[-1] == list2[-1]:
        return True
    else:
        return False

# 2. Write a function called list_product() that takes a list.
#    It returns the product of all the numbers in the list.

# list_product([1,2,3,4,5]) ---> 120
# list_product([8,4,3]) ---> 96
# list_product([120, 57, 98, 0, 12]) ---> 0

def list_product(num_list):
    total = 1
    for number in num_list:
        total *= number
    return total

# 3.  Write a function called rotate_left() that takes a list
#      and rotates all the elements in the list one space to
#      the left (Hint: no loop necessary!)
#
#  rotate_left([1,2,3]) ---> [2,3,1]
#  rotate_left(['this', 'is', 'a', 'sentence']) --->
#       ['is', 'a', 'sentence', 'this']

def rotate_left(lst):
    first = lst.pop(0) #Defaults to LAST ENTRY IN LIST
    lst.append(first)
    return lst

# 4.  Write a function called count_evens() that takes a list
#   of numbers and returns the count of the number of even
#   numbers in that list. Hint: To see if a number is even,
#   check if the remainder when dividing by 2 is 0...x%2==0

#  count_evens([2,1,2,3,4]) ---> 3
#  count_evens([1,3,5,7,9]) ---> 0
#  count_evens([2,4,6,8,10,12]) ---> 6

def count_evens(num_list):
    count = 0
    for number in num_list:
        if number % 2 == 0:
            count += 1
    return count

# 5. Write a function called list_range() that takes a list
#    of numbers and returns the range of the list, which is
#    the largest number minus the smallest number.
#    Hint: You can do this with a for loop, but there's actually
#      a built in way to get the largest or smallest number in
#      a list...try Googling!


# list_range([10, 3, 5, 4, 6]) ---> 7
# list_range([7,2,10, 9)] ---> 8
# list_range([2, 10, 7, 2]) ---> 8
# list_range([]) ---> 0

#No Google
def list_range(num_list):
    num_list.sort()
    if num_list == []:
        return 0
    return num_list[-1] - num_list[0]

#Using Google
def list_range2(num_list):
    if num_list == []:
        return 0
    return max(num_list) - min(num_list)

# 6.  Write a function called no_a() that takes a list
#     of words and returns a new list that contains only
#     the words that DON'T have an 'a' in them.

# no_a(['apple', 'banana', 'grape', 'kiwi', 'mango', 'coconut'])
#    ---> ['kiwi', 'coconut']

# no_a(['Africa', 'Europe', 'Asia', 'Antarctica', 'South America', 'North America', 'Australia']
#    ---> ['Europe']

#My version
def no_a(lst):
    no_a_list = []
    for word in lst:
        original_word = word
        word = word.lower()
        num_a = word.count('a')
        if num_a == 0:
            no_a_list.append(original_word)
    return no_a_list

#The official version
def no_a2(lst):
    new_list = []
    for word in lst:
        if 'a' not in word.lower():
            new_list.append(word)
    return new_list

# CHALLENGE: Write a function called has_duplicates()
#   that takes a list and returns True if there is ANY
#   element in the list that repeats.

def no_duplicates(lst):
    for entry in lst:
        if lst.count(entry) > 1:
            return False
    return True
            





































