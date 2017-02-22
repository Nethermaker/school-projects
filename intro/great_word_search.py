dictionary = {}

def read_file(filename):
    with open('{}'.format(filename), 'rb') as infile:
        for word in infile:
            for letter in word:
                if not letter.isalpha():
                    word = word.replace(letter, '')
            dictionary[word] = ''

def palindrome():
    lst = []
    for word in dictionary:
        if word == word[::-1]:
            lst.append(word)
    return max(lst, key=len)
#'deified'


def find_substring(substring):
    for word in dictionary:
        if substring in word:
            return word
#'stomachaches', 'wellingtons', 'calyx'


def different_word():
    lst = []
    for word in dictionary:
        if word[::-1] in dictionary:
            lst.append(word)
    return max(lst, key=len)
#'stressed'


def four_zs():
    lst = []
    for word in dictionary:
        if word.count('z') >= 4:
            lst.append(word)
    return lst
#'pizzazzes', 'razzmatazzes', 'razzmatazz', 'pizzazz'


###################################################################################################
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
    lst = []
    for number in range(1, 26):
        lst.append(caesar_cipher(string, number))
    return lst

def longest_caesar():
    final_list = []
    for word in dictionary:
        lst = multiple_caesar(word)
        for word2 in lst:
            if word2 in dictionary:
                final_list.append(word)
    return max(final_list, key=len)
#'nowhere'
###################################################################################################

def vowel_consonant():
    final_dict = {}
    for word in dictionary:
        if len(word) >= 6:
            vowels = 0
            consonants = 0
            for letter in word:
                if letter in 'aeiouy':
                    vowels += 1
                else:
                    consonants += 1
            ratio = (float(vowels) / float(consonants))
            final_dict[word] = ratio
    highest = max(final_dict, key=final_dict.get)
    lowest = min(final_dict, key=final_dict.get)
    print dictionary[highest], highest
    return lowest, dictionary[lowest]
#'eyepiece', 'strengths'

scrabble_values = {'e':1,
                   'a':1,
                   'i':1,
                   'o':1,
                   'n':1,
                   'r':1,
                   't':1,
                   'l':1,
                   's':1,
                   'u':1,
                   'd':2,
                   'g':2,
                   'b':3,
                   'c':3,
                   'm':3,
                   'p':3,
                   'f':4,
                   'h':4,
                   'v':4,
                   'w':4,
                   'y':4,
                   'k':5,
                   'j':8,
                   'x':8,
                   'q':10,
                   'z':10}


def scrabble():
    final_values = {}
    for word in dictionary:
        if len(word) == 7:
            value = 0
            for letter in word:
                value += scrabble_values[letter]
            final_values[word] = value
    return max(final_values, key=final_values.get), final_values[max(final_values, key=final_values.get)]
#'pizzazz', 45

def alternade():
    final = []
    for word in dictionary:
        word1 = ''
        word2 = ''
        count = 0
        for letter in word:
            if count % 2 == 0:
                word1 += letter
            else:
                word2 += letter
            count += 1
        if word1 in dictionary and word2 in dictionary:
            final.append(word)
    return max(final, key=len)
#'furriness' ('fries', 'urns')

def metathesis():
    new_dict = {}
    for word in dictionary:
        word = alphabetize(word)
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1
    lst = []
    for word in new_dict:
        if new_dict[word] == 2:
            lst.append(word)
    biggest = max(lst, key=len)
    for word in dictionary:
        if alphabetize(word) == biggest:
            print word
#permissivenesses, impressivenesses
#I'm assuming this is switching the double S's
        

###################################################################################################
def anagram():
    new_dict = {}
    for word in dictionary:
        word = alphabetize(word)
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1
    lst = []
    for word in new_dict:
        if new_dict[word] == 5:
            lst.append(word)
    biggest = max(lst, key=len)
    for word in dictionary:
        if alphabetize(word) == biggest:
            print word


def alphabetize(word):
    lst = []
    for letter in word:
        lst.append(letter)
    lst = sorted(lst)
    return ''.join(lst)
#sceptres
#specters
#spectres
#scepters
#respects
###################################################################################################
  
    
    
            


read_file('2of12inf.txt')























