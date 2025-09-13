def get_student_info():
    name = input("Enter your name: ")
    subject = input("What subject do you want to study today? (e.g., Math, Science): ")
    return name, subject

def quiz(subject):
    questions = {
        "Math": [
            ("What is 5 + 7?", "12"),
            ("What is 9 * 3?", "27"),
            ("What is 15 / 3?", "5")
        ],
        "Science": [
            ("What planet is known as the Red Planet?", "Mars"),
            ("What gas do plants absorb from the atmosphere?", "Carbon dioxide"),
            ("What is H2O commonly known as?", "Water")
        ]
    }
    
    score = 0
    if subject not in questions:
        print(f"Sorry, I don't have questions for {subject}. Let's try Math instead!")
        subject = "Math"
    
    print(f"\nStarting quiz on {subject}!\n")
    for q, a in questions[subject]:
        answer = input(q + " ")
        if answer.strip().lower() == a.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Oops! The correct answer is {a}.\n")
    return score, len(questions[subject])

def give_feedback(name, score, total):
    print(f"{name}, you scored {score} out of {total}!")
    percentage = (score / total) * 100
    
    if percentage == 100:
        print("Excellent work! You mastered the material.")
    elif percentage >= 70:
        print("Good job! Keep practicing to improve even more.")
    else:
        print("Don't worry! Review the material and try again.")

def main():
    name, subject = get_student_info()
    score, total = quiz(subject)
    give_feedback(name, score, total)

if __name__ == "__main__":
    main()
