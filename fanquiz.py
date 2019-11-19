question_one = "1. What state has the most 14ers?"
question_two = "2. What continent are tigers most often found?"
question_three = "3. What is the color of an NBA basketball?"
question_four = "4. What city is the largest in the United States?"
question_five = "5. Where can the most accurate clock be found?"
question_six = "6. The B-2 is flown for over 24 hours when in use"
question_seven = "7. The fastest plane is the Blackbird"
question_eight = "8. There are 6 generations of jets"

def first_question():
    scoring = 0
    question_response = ['(a) California', '(b) Washington', '(c) Utah', '(d) Colorado', '(e) Alaska']

    print(question_one)
    for answer in question_response:
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

def second_question():
    question_response = ['(a) North America', '(b) South America', '(c) Asia', '(d) Africa', '(e) Antarctica']

    print(question_two)
    for answer in question_response:
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

def third_question():
    question_response = ['(a) green', '(b) black', '(c) blue', '(d) clear', '(e) brown']

    print(question_three)
    for answer in question_response:
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

def fourth_question():
    question_response = ['(a) New York City', '(b) Miami', '(c) Los Angeles', '(d) Seattle', '(e) Boston']

    print(question_four)
    for answer in question_response:
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

def fifth_question():
    question_response = ['(a) Berlin, Germany', '(b) Moscow, Russia', '(c) Colorado, United States', '(d) London, England', '(e) Syndey, Australia']

    print(question_five)
    for answer in question_response:
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

def sixth_question():
    print(question_six)
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

def seventh_question():
    print(question_seven)
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

def eighth_question():
    print(question_eight)
    response = input("True or False? [T or F]:")
    print('You answered: ' + str(response))

    if response.upper() == 'F':
        print("correct! :)")
        scoring = 1
    elif response.upper() != 'F':
        print("Incorrect, the correct answer is False")
        scoring = 0

    print("scoring: " + str(scoring))
    return scoring

def scoring_calculation():
    scoring = 0
    scoring_list = []
    if first_question() == 1:
        scoring += 1
        scoring_list.append("Question 1: 1")
    else:
        scoring_list.append("Question 1: 0")
    if second_question() == 1:
        scoring += 1
        scoring_list.append("Question 2: 1")
    else:
        scoring_list.append("Question 2: 0")
    if third_question() == 1:
        scoring += 1
        scoring_list.append("Question 3: 1")
    else:
        scoring_list.append("Question 3: 0")
    if fourth_question() == 1:
        scoring += 1
        scoring_list.append("Question 4: 1")
    else:
        scoring_list.append("Question 4: 0")
    if fifth_question() == 1:
        scoring += 1
        scoring_list.append("Question 5: 1")
    else:
        scoring_list.append("Question 5: 0")
    if sixth_question() == 1:
        scoring += 1
        scoring_list.append("Question 6: 1")
    else:
        scoring_list.append("Question 6: 0")
    if seventh_question() == 1:
        scoring += 1
        scoring_list.append("Question 7: 1")
    else:
        scoring_list.append("Question 7: 0")
    if eighth_question() == 1:
        scoring += 1
        scoring_list.append("Question 8: 1")
    else:
        scoring_list.append("Question 8: 0")
    
    for score in scoring_list:
        print(score)
    print("")
    print("Calculated scoring is: " + str(scoring))
    return scoring

def fan_quiz_scoring():
    scoring = scoring_calculation()
    print("You shall be named:")
    if scoring == 8:
        phrase = "Master is an undestatement"
    elif scoring == 6:
        phrase = "Eh you almost mastered it"
    elif scoring == 4:
        phrase = "woah, you're pretty good"
    elif scoring == 2:
        phrase = "ou nice try"
    else:
        phrase = "nameless"
    print(phrase)

def run_quiz():
    print('\n\n\nRandom knowledge quiz\n\n\n')

    fan_quiz_scoring()

run_quiz()