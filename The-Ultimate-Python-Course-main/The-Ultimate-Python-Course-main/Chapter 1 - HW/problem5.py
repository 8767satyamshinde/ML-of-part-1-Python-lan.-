questions = [
    {"question": "What's the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "What's 2 + 2?", "options": ["3", "4", "5"], "answer": "4"}
]

def ask_question(question):
    print(question['question'])
    for idx, option in enumerate(question['options']):
        print(f"{idx + 1}. {option}")
    answer = input("Your answer: ")
    return answer == question['answer']

score = 0
for q in questions:
    if ask_question(q):
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Your score: {score}/{len(questions)}")
