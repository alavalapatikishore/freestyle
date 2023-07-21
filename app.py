def display_question(question, options):
    print(question)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    user_choice = int(input("Your answer (enter the option number): "))
    return user_choice


def check_answer(user_choice, correct_answer):
    return user_choice == correct_answer


def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct_answer": 2,
        },
        # Add more questions here
        # Question 2
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Mars", "Venus", "Earth", "Mercury"],
            "correct_answer": 4,
        },
        # Add more questions here
        # ...
        # Question 20
        {
            "question": "What is the chemical symbol of water?",
            "options": ["H2O", "CO2", "O2", "CH4"],
            "correct_answer": 1,
        },
    ]

    total_questions = len(questions)
    correct_answers = 0

    for q in questions:
        user_choice = display_question(q["question"], q["options"])
        if check_answer(user_choice, q["correct_answer"]):
            print("Correct!\n")
            correct_answers += 1
        else:
            print("Incorrect!\n")

    print(f"You answered {correct_answers} out of {total_questions} questions correctly.")

    if correct_answers >= 15:
        print("Congratulations! You are selected for the job.")
    else:
        print("Unfortunately, you are not selected for the job.")


if __name__ == "__main__":
    run_quiz()
