def question_one():
    scoring = 0
    question1_text = "1. What state has the most 14ers?"
    question1_answers = ['(a) California', '(b) Washington', '(c) Utah', '(d) Colorado', '(e) Alaska']

    print(question1_text)
    for answer in question1_answers:
        print(answer)
    response = input("Enter one letter for your answer [A, B, C, D or E]:")
    print('You answered: ' + (response))

    if response.upper() == 'D':
        print("correct! :)")
        scoring += 1

    elif response.upper() != 'D':
        print("Incorrect, the correct answer is Colorado")

    print("scoring: " + str(scoring))
    return scoring

def question_two():

    question_two_text = "2. What continent are tigers most often found?"
    question_two_answers = ['(a) North America', '(b) South America', '(c) Asia', '(d) Africa', '(e) Antarctica']

    print(question_two_text)
    for answer in question_two_answers:
        print(answer)
    response = input("Enter one letter for your answer [A, B, C, D or E]:")
    print('You answered: ' + str(response))

    if response.upper() == 'C':
        print("correct! :)")
        scoring = 1
    elif response.upper() != 'C':
        print("Incorrect, the correct answer is Asia")
        scoring = 0
    print("scoring: " + str(scoring))
    return scoring

def question_three():

    question_three_text = "3. What is the color of an NBA basketball?"
    question_three_answers = ['(a) green', '(b) black', '(c) blue', '(d) clear', '(e) brown']

    print(question_three_text)
    for answer in question_three_answers:
        print(answer)
    response = input("Enter one letter for your answer [A, B, C, D or E]:")
    print('You answered: ' + str(response))

    if response.upper() == 'E':
        print("correct! :)")
        scoring = 1
    elif response.upper() != 'E':
        print("Incorrect, the correct answer is brown")
        scoring = 0
    print("scoring: " + str(scoring))
    return scoring

def question_four():
    question_four_text = "4. What city is the largest in the United States?"
    question_four_answers = ['(a) New York City', '(b) Miami', '(c) Los Angeles', '(d) Seattle', '(e) Boston']

    print(question_four_text)
    for answer in question_four_answers:
        print(answer)
    response = input("Enter one letter for your answer [A, B, C, D or E]:")
    print('You answered: ' + str(response))

    if response.upper() == 'A':
        print("correct! :)")
        scoring = 1
    elif response.upper() != 'A':
        print("Incorrect, the correct answer is New York City")
        scoring = 0
    print("scoring: " + str(scoring))
    return scoring

def question_five():
    question_five_text = "5. Where can the most accurate clock be found?"
    question_five_answers = ['(a) Berlin, Germany', '(b) Moscow, Russia', '(c) Colorado, United States', '(d) London, England', '(e) Syndey, Australia']

    print(question_five_text)
    for answer in question_five_answers:
        print(answer)
    response = input("Enter one letter for your answer [A, B, C, D or E]:")
    print('You answered: ' + str(response))

    if response.upper() == 'C':
        print("correct! :)")
        scoring = 1
    elif response.upper() != 'C':
        print("Incorrect, the correct answer is New York City")
        scoring = 0
    print("scoring: " + str(scoring))
    return scoring

def question_six():
    question_six_text = "6. The B-2 is flown for over 24 hours when in use"

    print(question_six_text)
    response = input("True or False? [T or F]:")
    print('You answered: ' + str(response))

    if response.upper() == 'T':
        print("correct! :)")
        scoring = 1
    elif response.upper() != 'T':
        print("Incorrect, the correct answer is True")
        scoring = 0

    print("scoring: " + str(scoring))
    return scoring
question_six()