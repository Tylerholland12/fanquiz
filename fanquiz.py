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
        print("correct")
        scoring += 1

    elif response.upper() != 'D':
        print("Incorrect, the correct answer is Colorado")

    print("scoring: " + str(scoring))
    return scoring

question_one()