#License
def license(age):
    if age >= 16:
        return True
    else:
        return False


#Makes triangle (w/ challenge)
def makes_triangle(one, two, three):
    if one > two and one > three:
        return two + three > one
    if two > one and two > three:
        return one + three > two
    if three > one and three > two:
        return one + two > three
    


#Longer Word
def longer_word(string1, string2):
    if len(string1) > len(string2):
        return string1
    elif len(string2) > len(string1):
        return string2
    else:
        return "Same length!"


#Max of three numbers
#I originally had this working as was probably intended (using 'else' for three), except
# max_three(10,10,9) returned 9 as the max, and this is the closest
# I could get to fixing it.
def max_three(one, two, three):
    if one > two and one > three:
        var_max = one
        return var_max
    elif two > one and two > three:
        var_max = two
        return var_max
    elif three > one and three > two:
        var_max = three
        return var_max
    else:
        return 'None of these numbers are greater than both of the others'


#Palindrome? (w/ challenge)
def is_palindrome(word):
    return word.lower() == word[::-1].lower()


#BMI (height is in inches)
def bmi(weight, height):
    bmi = (weight*720) / (height ** 2)
    if bmi < 17.0:
        print bmi
        return 'BMI is lower than the normal range.'
    elif 17 <= bmi <= 25:
        print bmi
        return 'BMI is within the normal range.'
    else:
        print bmi
        return 'BMI is higher than the normal range.'
    return

#Challenge
def leap_year(year):
    #Check if the year is a century
    if str(year)[-2:] == '00':
        #If True, check if year is divisible by 400
        if year % 400 == 0:
            print 'The year is a leap year.'
            return True
        else:
            print 'The year is not a leap year.'
            return False
    #Otherwise check the year is divisible by four
    else:
        if year % 4 == 0:
            print 'The year is a leap year.'
            return True
        else:
            print 'The year is not a leap year.'
            return False
        






















