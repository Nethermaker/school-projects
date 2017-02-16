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

def caesar_cipher(string, number, encode=True):
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

#CODE 1: Great job at figuring out how to crack the first code. To solve the other one, the
# keyword is the last name of the author of the novels The Shining, Misery, and Carrie.

#Keyword = King

def letter_value(letter):
    if letter.isupper():
        return ord(letter) - 64
    else:
        return ord(letter) - 96

def fill_out(string, length):
    new_string = ''
    count = 0
    while len(new_string) < length:
        new_string = new_string + string[count % len(string)]
        count += 1
    return new_string

def remove_extras(string):
    for letter in string:
        if not letter.isalpha():
            string = string.replace(letter, '')
    return string.lower()

def remove_extras(string):
    new_one = ''
    for letter in string:
        if letter == ' ':
            pass
        elif letter.isalpha():
            new_one += letter
    return new_one

#Commented-out lines were used for debugging
def vigenere(string, keyword, encode=True):
    string = remove_extras(string)
    #print string
    
    key = fill_out(keyword, len(string)).lower()
    #print key
    
    key_num = []
    for letter in key:
        if not encode:
            key_num.append(-(letter_value(letter)))
        else:
            key_num.append(letter_value(letter))
    #print key_num

    final_string =  ''
    #print zip(string, key_num)
    for letter, num in zip(string, key_num):
        final_string += rotate_letter(letter, num)
    return final_string

#CODE 2: congratulationsyouhavemanagedtocrackthecodeyouareclearlytoosmartforthisclass
#
#or...: Congratulations you have managed to crack the code you are clearly
#       too smart for this class
