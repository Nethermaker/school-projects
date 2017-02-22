import random

def load(filename):
    with open(filename, 'rb') as infile:
        line_counter = 1
        question = ''
        answer = ''
        questions = {}
        for line in infile:
            line = line.strip()
            if line_counter % 2 == 1:
                question = line
                line_counter += 1
            else:
                answer = line
                line_counter += 1
            questions[question] = answer
        questions = zip(questions.keys(), questions.values())
        return questions

def ask_questions(questions, high_score):
    questions = random.sample(questions, len(questions))
    correct = 0
    incorrect = 0
    count = 0
    while count < len(questions):
        question = questions[count]
        user_input = raw_input(question[0] + ' ').lower()
        for letter in user_input:
            if letter == ' ' or letter.isalpha():
                pass
            else:
                user_input = user_input.replace(letter, '')
        user_input = user_input.strip()
        print user_input
        if user_input == question[1].lower().strip():
            print 'Correct!'
            correct += 1
            count += 1
        else:
            print 'Wrong!'
            incorrect +=1
            count += 1
    print 'Number correct: {}'.format(correct)
    print 'Number incorrect: {}'.format(incorrect)
    return correct, incorrect, high_score


def main(high_score):
    trivia_file = raw_input('Enter the file you would like to load, or type \'help\' for help: ')
    if trivia_file == 'help':
        return main(high_score) #COME HERE AND FIX THIS ALSO
    else:
        questions = load(trivia_file)

    print 'This sessions\'s high score is: {}'.format(high_score)
    ask_questions(questions, high_score)

main(0)
































    


        
