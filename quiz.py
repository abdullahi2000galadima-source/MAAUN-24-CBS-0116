# CLI Quiz Application

# Setup: List of questions (3 new dictionaries)
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "correct_answer": "C"
    },
    {
        "question": "What is the output of 5 + 3 * 2?",
        "options": ["A. 16", "B. 11", "C. 13", "D. 10"],
        "correct_answer": "B"
    },
    {
        "question": "Which loop is used when the number of iterations is known?",
        "options": ["A. while loop", "B. do-while loop", "C. for loop", "D. infinite loop"],
        "correct_answer": "C"
    }
]

def calculate_percentage(score, total):
    return (score / total) * 100

def run_quiz():
    score = 0
    
    print("Welcome to the CLI Quiz!\n")
    
    for index, q in enumerate(questions, start=1):
        print(f"Question {index}: {q['question']}")
        
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['correct_answer']}.\n")
    
    percentage = calculate_percentage(score, len(questions))
    
    print("Quiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.2f}%")
    
    if percentage >= 50:
        print("Result: PASS ")
    else:
        print("Result: FAIL ")