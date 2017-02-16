# 1. Create a dictionary that connects the numbers 1-12 with each
# number's corresponding month. 1 --> January, for example.

months = {1:'January',
          2:'February',
          3:'March',
          4:'April',
          5:'May',
          6:'June',
          7:'July',
          8:'August',
          9:'September',
          10:'October',
          11:'November',
          12:'December'}



# 2. Write a function called write_date() that takes a date written in
# the format "6/28/1983" and prints it out in the format "28 of June, 1983".
# Hint: The split function can work with more than just spaces!

def write_date(date):
    month_day_year = date.split('/')
    return '{} of {}, {}'.format(month_day_year[1],
                                 months[int(month_day_year[0])],
                                 month_day_year[2])



# 3. Write a dictionary that contains at least five words as keys,
# and choose a value for each that will replace the word.  For example,
# you may have the word "Handelman" as a key and "Batman" as its value.
# Shhh...don't tell anyone.

words_dict = {'Handelman':'Batman',
              'is':'isn\'t',
              'I':'you',
              'will':'won\'t',
              'can':'can\'t'}


# 4. Write a function called replace_words() that takes a sentence and
# returns the same sentence, but with any of the keys in your dictionary
# from problem 3 replaced with their respective values.  Note: if more
# than one of the words appears in the sentence, then all words should
# be correctly replaced!

# Ex: replace_words('Mr. Handelman is my programming teacher')
# 'Mr. Batman is my programming teacher.'


#This is pretty finnicky and sensitive to punctuation, but it works
def replace_words(sentence):
    word_list = sentence.split()
    new_string = []
    for word in word_list:
        if word in words_dict:
            new_string.append(words_dict[word])
        else:
            new_string.append(word)
    return ' '.join(new_string).capitalize()

        

# 4. Write a function called count_words() that takes a string (possibly
#   a long string!) as input and counts the number of time each word
#   appears in the string.  It then returns the count of all words as a
#  dictionary.

# Ex: count_words('So patient a doctor to doctor a patient so')
# {'so':2, 'patient': 2, 'a': 2, 'doctor': 2, 'to': 1}

def count_words(string):
    count_words = {}
    for word in string.lower().split():
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    return count_words































