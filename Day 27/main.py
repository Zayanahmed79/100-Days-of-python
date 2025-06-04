questions = ["What is the capital of France?", "What is 2 + 2?", "What is the largest mammal?"]
answers = ["Paris", "4", "Blue Whale"]

def ask_questions(questions, answers):
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i] + " ")
        if user_answer.strip().lower() == answers[i].strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answers[i])
    print(f"You scored {score} out of {len(questions)}.")
ask_questions(questions, answers)
# This code defines a simple quiz game where the user is asked a series of questions and must provide the correct answers.
# The user receives feedback on whether their answers are correct or not.

