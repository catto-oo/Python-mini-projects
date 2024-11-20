import os

filename = r"Quiz Game\questions.txt"

def load_questions():
    questions = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(",")
                quest = data[0].strip()
                choices = data[1:-1]
                for i in range(len(choices)): # just cleaning the choices from spaces
                    choices[i] = choices[i].strip()
                corr_ans = data[-1].strip()

        questions.append({
            "question": quest,
            "choices": choices,
            "correct answer": corr_ans
        })

    print(questions)

load_questions()