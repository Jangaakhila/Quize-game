# Simple Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Shark"],
        "answer": "B"
    }
]

score = 0

print("Welcome to the Quiz Game!")
print("-" * 30)

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q['question']}")
    for choice in q["choices"]:
        print(choice)
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")

print("-" * 30)
print(f"Quiz Completed! Your Score: {score}/{len(questions)}")