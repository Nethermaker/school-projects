#How do I rotate a letter?????

#I am going to give you two completely different methods.

#Method 1: The ASCII method!

#The ord() function will take a letter and return its ASCII value.

print ord('a')
print ord('J')

#The chr() function takes an ASCII value and returns its character.

print chr(97)
print chr(74)

letter = 'p'
number = 5

rotation = ord('p') + 5
print chr(rotation)


#Your job (if you use this method): if you go past the range that you should be in, you need to
# subtract (or add) 26 until you're back in the correct range.


#Method 2: The Alphabet String Method

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter = 'e'
number = -5

location = alphabet.index(letter)
location = (location + number) % 26
print alphabet[location]

#Your job (if you use this method): this does not currently work for upper case letters
# or non-letters. You have to make it work for any character.
