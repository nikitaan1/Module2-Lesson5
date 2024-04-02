#Task 1

questions_list = ["What color is the sky?", "Calculate: 5 + 5", "On which planet we live?" ]

answers = ["Blue", 10, "Earth"]


#Task 2:

def quiz(questions, answers):
    total_questions = len(questions)

    for i in range(total_questions):
        user_answer = input(questions[i] + " ")

        if user_answer.lower() == answers[i].lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {answers[i]}")

questions_list = ["What color is the sky?", "Calculate: 5 + 5", "On which planet do we live?"]
answers = ["Blue", "10", "Earth"]

quiz(questions_list, answers)

#Task3

def quiz(questions, answers):
    total_questions = len(questions)
    score = 0

    for i in range(total_questions):
        user_answer = input(questions[i] + " ")

        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[i]}")

    
    print(f"You got {score} out of {total_questions} questions correct.")

questions_list = ["What color is the sky?", "Calculate: 5 + 5", "On which planet do we live?"]
answers = ["Blue", "10", "Earth"]

quiz(questions_list, answers)

    