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



    