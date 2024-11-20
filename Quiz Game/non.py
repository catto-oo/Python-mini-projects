import os

filename = r"Quiz Game\questions.txt"
questions = []

def load_questions():
    
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(",")
                quest = data[0].strip()
                choices = data[1:-1]
                for i in range(len(choices)): # just cleaning the choices from spaces
                    choices[i] = choices[i].strip()
                corr_ans = data[-1].strip()

                # questions is a list containing dicts where there are key-value pairs for questions, choices, and answers
                questions.append({
                    "question": quest,
                    "choices": choices,
                    "correct answer": corr_ans
                })
    
    else:
        print(f"Couldn't find {filename}.")

def ask_questions(question):
    pass


def run_quiz():
    load_questions()
    if not questions:
        print("There are no questions available, come back later.")
    else:
        score = 0
        for question in questions:
            score += ask_questions(question)

    print(f"The quiz is over! Your final score is: {score}/{len(questions)}")