import os
import time

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
        print("Loading questions..."); time.sleep(2)
    
    else:
        print(f"Couldn't find {filename}.")


def ask_questions(idx, question):
    quest = question["question"]
    choices = question["choices"]
    correct = question["correct answer"]

    print(f"\nQuestion {idx}:\n{quest}");time.sleep(1)

    for choice in choices:
        print("  ", choice)

    possible_choices = [choice[0] for choice in choices]

    
    while True:
        answer = input("\nEnter the letter of your answer: ").strip().upper()
        if answer in possible_choices:
            correct_index = possible_choices.index(correct) # getting the index of the correct answer
            correct_choice = choices[correct_index] # getting the correct choice based on that correct index

            if answer == correct_choice[0]: # if the answer (one letter) is the same as the first letter of the correct choice (A, B, C...)
                print("Correct!")
                return 1 # score + 1
            else:
                print(f"Incorrect! The correct answer was {correct}.")
                return 0 # score + 0
            
        else:
            print("Invalid input. Please enter a letter corresponding to an answer.")


def run_quiz():
    load_questions()
    score = 0
    
    if not questions: # empty questions list
        print("There are no questions available, come back later.")
    else:
        for idx, question in enumerate(questions, start=1): # 'question' is a dictionary
            score += ask_questions(idx, question); time.sleep(2) # I also got the index cuz I wanna use it to customize text
    
    print("-"*30)
    print(f"The quiz is over! Your total score is: {score}/{len(questions)}")
    print("-"*30); time.sleep(2)

    temp = input("\nWould you like to play again? (Yes/No): ").strip().lower()

    if temp[0] != "y": # to accept any input such as "yes, yea, yup, yeah..."
        print("Hope you had fun! Goodbye!"); time.sleep(2)
        return False
    else:
        questions.clear()
        print("Let's go for another round!"); time.sleep(2)
        return True



def main():
    temp = input("Would you like to play a quiz game? (Yes/No): ").strip().lower()
    if temp[0] == "y":
        condition = True
        while condition:
            condition = run_quiz() # the function returns false or true based on if the player wants to play again or not
    else:
        print("Free will reigns...")

main()