def hamming(num1, num2):
    biggest_num = bin(max([num1, num2]))[2:]
    smallest_num = bin(min([num1, num2]))[2:]
    difference = len(biggest_num) - len(smallest_num)
    smallest_num = '0'*difference + smallest_num
    count = 0
    total = 0
    for digit in biggest_num:
        if digit != smallest_num[count]:
            count += 1
            total += 1
        else:
            count += 1
    return total


def triangle_type(one,two,three):
    a,b,c = sorted([one,two,three])
    if a**2 + b**2 == c**2:
        print 'The triangle is right.'
    elif a**2 + b**2 > c**2:
        print 'The triangle is acute.'
    else:
        print 'The triangle is obtuse.'


def vertical(lst):
    longest = len(max(lst))
    for i in range(longest):
        string = ''
        for word in lst:
            #kinda messy but it words
            try:
                string += word[i]
            except:
                string += ' '
        print string


def count_words(filename):
    count = {}
    with open(filename, 'rb') as infile:
        for line in infile:
            line = line.split(' ')
            for word in line:
                word = word.strip()
                for letter in word:
                    if not letter.isalpha():
                        word = word.replace(letter, '')
                word = word.lower()
                if word not in count:
                    count[word] = 1
                elif word in count:
                    count[word] += 1
    count.pop('')
    print sorted(count.keys(), key=count.get, reverse=True)[0:10]


def substring(word):
    #these are kind of useful
    return [word[index1:index2] for index1 in range(len(word)) \
            for index2 in range(1,len(word) + 1) if word[index1:index2] != '']






















    
            
