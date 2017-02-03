

def rotate_letter(letter, number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if letter.isalpha():
        if letter.islower():
            location = alphabet.index(letter)
            location = (location + number) % 26
            return alphabet[location]
        else:
            location = alphabet.index(letter.lower())
            location = (location + number) % 26
            return alphabet[location].upper()
    else:
        return letter

def caesar_cipher(string, number, encode):
    new_string = ''
    if encode == False:
        number *= -1
    for letter in string:
        new_string += rotate_letter(letter, number)
    return new_string

def multiple_caesar(string):
    count = 1
    while count <= 25:
        print caesar_cipher(string, count, True)
        count += 1

#Code 1: Great job at figuring out how to crack the first code. To solve the other one, the
# keyword is the last name of the author of the novels The Shining, Misery, and Carrie.

#Keyword = King
