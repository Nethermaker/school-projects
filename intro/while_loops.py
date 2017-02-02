#While Loops

#A while loop is a type of a loop that continues to loop until a certain
# condition is no longer true.

#For example, I would like a function that prints the same sentence
# 10 times in a row.

def print_stuff(amt):
    counter = 0 #This variable will count the number of times I have
                # printed the sentence. I have "initialized" it to 0.
    while counter < amt:
        print 'All work and no play makes Jack a dull boy.'
        #counter = counter + 1
        counter += 1 #Sets the value of 'counter' to be one more than previously

#Let's write a function that will add all the integers from 1 to n.
# For example, sum_to_n(100) = 1 + 2 + 3 + ... + 99 + 100 = 5050

#First of all, there is a SUPER EASY WAY to do this.
#print sum(range(1, 101)) #In a real program, we would just do this.

def sum_to_n(number):
    current_number = 1
    total = 0
    while current_number <= number:
        total += current_number
        current_number += 1
    return total

#Create a function called countdown().
# countdown() takes a single number as input.
# It will count down from that number until it reaches 1, and then it will print
# 'Blastoff!'

def countdown(num):
    while num >= 1:
        print num
        num -= 1
    print 'Blastoff!'

#The following example is a bit odd, because we won't be using a while loop
# for this in the future.

#I would like to count the number of 'a's in a word.

def count_a(word):
    num = 0
    index = 0
    while index < len(word):
        if word[index].lower() == 'a':
            num += 1
        index += 1
    return num

#While loops are often used to keep looping an indefinite number of times
# until something changes. For example, if I want to keep asking a question
# until someone enters a correct answer, I would use a loop which will loop
# until the correct answer is given.

def is_awesome():
    answer = raw_input('Is Mr. Handelman awesome? ')
    while answer.lower() != 'yes':
        answer = raw_input('No, really, is Mr. Handelman awesome? ')
    print 'Yeah, that\'s what I thought...'

#Sometimes, I want to put the program into an infinite loop and then break
# out of the loop manually. The function below is exactly the same as the function
# above, but I won't give the while loop a specific condition.

def is_awesome_2():
    answer = raw_input('Is Mr. Handelman awesome? ')
    while True:
        if answer.lower() == 'yes':
            break #Breaks out of the loop no matter what.
        answer = raw_input('No, really, is Mr. Handelman awesome? ')
    print 'Yeah, that\'s what I thought...'































