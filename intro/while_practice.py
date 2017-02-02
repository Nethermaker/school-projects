#1.
def print_n(string, num):
    count = 0
    while count < num:
        print string
        count += 1
    
#2.
def bottles(num):
    while num >= 1:
        print '{} bottles of soda on the wall'.format(num)
        print '{} bottles of soda'.format(num)
        print 'Take one down, pass it around'
        num -= 1
        print '{} bottles of soda on the wall'.format(num)
        print ''
    return

#3.
def factorial(num):
    current = 1
    total = 1
    while current <= num:
        total *= current
        current += 1
    return total

#4a.
def password():
    answer = raw_input('Enter password: ')
    while answer != 'please':
        print 'Invalid password'
        answer = raw_input('Enter password: ')
    print 'Access granted.'
    return

#4b.
def password2():
    attempts = 5
    while attempts > 0:
        answer = raw_input('Enter password: ')
        if answer.lower() == 'please':
            break
        else:
            attempts -= 1
            print 'Invalid password. {} attempts remaining'.format(attempts)
    if attempts == 0:
        print 'Access Denied'
    else:
        print 'Access Granted'
    return

#5.
def sum_of_odd(n):
    current = 1
    total = 0
    while current <= n:
        total += current
        current += 2
    return total
    

#6.
def biggest():
    biggest = -10000000000000000000000000000000000000
    while True:
        answer = raw_input('Enter a number: ')
        if answer == '':
            break
        elif int(answer) > biggest:
            biggest = int(answer)
        elif int(answer) < biggest:
            pass
    return biggest
            
#Fibonacci challenge
def fib(n):
    count = 1
    num1 = 1
    temp_num1 = 1
    num2 = 1
    temp_num2 = 1
    while count <= n:
        print num1
        temp_num2 = num1 + num2
        temp_num1 = num2
        num1 = temp_num1
        num2 = temp_num2
        count += 1
    return

#Prime number challenge
def is_prime(number):
    count = 2
    while count < number:
        if number % count > 0:
            count +=1
        elif number % count == 0:
            return False
    return True
        
        
        


























