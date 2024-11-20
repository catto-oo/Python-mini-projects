import os
import time

filename = r"Quiz Game\questions.txt"
questions = []
condition = False # just for my while loop

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
        print("Questions loaded."); time.sleep(2)
    
    else:
        print(f"Couldn't find {filename}.")

def ask_questions(question):
    pass


def run_quiz():
    load_questions()
    if not questions: # empty questions list
        print("There are no questions available, come back later.")
    else:
        score = 0
        for question in questions: # 'question' is a dictionary
            score += ask_questions(question)

    print(f"The quiz is over! Your total score is: {score}/{len(questions)}"); time.sleep(2)

    temp = input("Would you like to play again? (Yes/No): ").strip().lower()
    if temp[0] != "y": # to accept any input such as "yes, yea, yup, yeah..."
        condition == False
        print("Hope you had fun! Goodbye!"); time.sleep(2)
    else:
        print("Let's go for another round!"); time.sleep(2)


temp = input("Would you like to play a quiz game? (Yes/No): ").strip().lower()

if temp[0] == "y":
    while condition == True:
        run_quiz()

else:
    print("Free will reigns...")