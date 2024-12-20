import random

def main():
    quiz = {
        "What is the main difference between a tuple and a list in Python?":
        (["A) Tuples are mutable, while lists are immutable", "B) Lists are mutable, while tuples are immutable", "C) Both are mutable",
          "D) Both are immutable"], "B"),

        "Which of the following is a valid way to define a tuple in Python?":
        (["A) t = (1, 2, 3)", "B) t = [1, 2, 3]", "C) t = {1, 2, 3}", "D) t = 1, 2, 3"], "A"),

        "Which of the following methods is used to add an item to the end of a list in Python?":
        (["A) append()", "B) insert()", "C) add()", "D) push()"], "A"),

        "Which of the following data types is immutable in Python?":
        (["A) List", "B) Dictionary", "C) Set", "D) Tuple"], "D"),
    }

    questions = list(quiz.keys())
    random.shuffle(questions)

    score = 0

    for question in questions:
        print(question)
        options, correct_answer = quiz[question]
        for option in options:
            print(option)

        answer = input("Your answer (A, B, C, D): ").strip().upper()

        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.\n")

    print(f"Your final score is: {score}/{len(quiz)}")

if __name__ == "__main__":
    main()

