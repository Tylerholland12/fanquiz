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

def question_seven():
    question_seven_text = "7. The fastest plane is the Blackbird"

    print(question_seven_text)
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

def question_eight():
    question_eight_text = "8. There are 6 generations of jets"

    print(question_eight_text)
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
    if question_one() == 1:
        scoring += 1
        scoring_list.append("Question 1: 1")
    else:
        scoring_list.append("Question 1: 0")
    if question_two() == 1:
        scoring += 1
        scoring_list.append("Question 2: 1")
    else:
        scoring_list.append("Question 2: 0")
    if question_three() == 1:
        scoring += 1
        scoring_list.append("Question 3: 1")
    else:
        scoring_list.append("Question 3: 0")
    if question_four() == 1:
        scoring += 1
        scoring_list.append("Question 4: 1")
    else:
        scoring_list.append("Question 4: 0")
    if question_five() == 1:
        scoring += 1
        scoring_list.append("Question 5: 1")
    else:
        scoring_list.append("Question 5: 0")
    if question_six() == 1:
        scoring += 1
        scoring_list.append("Question 6: 1")
    else:
        scoring_list.append("Question 6: 0")
    if question_seven() == 1:
        scoring += 1
        scoring_list.append("Question 7: 1")
    else:
        scoring_list.append("Question 7: 0")
    if question_eight() == 1:
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