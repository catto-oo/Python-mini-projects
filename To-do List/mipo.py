import os

tasks = []
filename = r"To-do List\todo list.txt"

def load_tasks():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                # the lines will be in the format "taskName,taskDesc,completion"
                data = line.strip().split(',')
                taskName = data[0].strip().capitalize()
                taskDesc = data[1].strip()
                completion = data[2].strip()

                # each dictionary in the list tasks has the necessary info for each task
                tasks.append({
                    "name": taskName,
                    "desc": taskDesc,
                    "status": completion
                })

def save_tasks():
    with open(filename, 'w') as file:
        for task in tasks: # task is a dict
            file.write(f"{task["name"]},{task["desc"]},{task["status"]}\n")
        print("\nYour list has been saved successfully!")

def view_tasks():
    print("Your to-do list:")
    for idx, task in enumerate(tasks, start=1):
        if task["desc"] == "": # if we have no description, don't show it
            print(f"{idx}. Task Name: {task["name"]}\n   Status: {task["status"]}\n")
        else: # otherwise show desc
            print(f"{idx}. Task Name: {task["name"]}\n   Description: {task["desc"]}\n   Status: {task["status"]}\n")

def mark_as_done():
    name = input("Enter the name of the task to mark as done: ").capitalize()
    for task in tasks:
        if task["name"] == name: # checking if the current task is the same as the one we wanna mark as done
            if task["status"] == "[Completed]":
                print(f"Task '{name}' is already marked as done!")
                return
            else:
                task["status"] = "[Completed]"
                print(f"Task '{name}' marked as done!")
                return # quits loop, otherwise we print the next line
    print(f"Task '{name}' not found in this list. Check your spelling.")

def delete_task():
    name = input("Enter the name of the task to delete: ").capitalize()
    for idx, task in enumerate(tasks): # I need the task index to pop() it
        if task["name"] == name:
            tasks.pop(idx)
            print(f"Task '{name}' deleted successfully!")
            return
    print(f"Task '{name}' not found in this list. Check your spelling.")

def add_task():
    print("Enter the information related to your task.")
    name = input("Task Name: ").strip().capitalize()
    desc = input("Description (Leave empty if none): ").strip()
    tasks.append({
        "name": name,
        "desc": desc,
        "status": "[Not Completed]" # the task added shouldn't be completed
    })
    print(f"Task '{name}' added successfuly!")

def main():
    global tasks
    load_tasks()
    print("Welcome to your To-do List!")

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task As Done")
        print("4. View Tasks")
        print("5. Clear Tasks")
        print("6. Save Changes")
        print("7. Exit")
        print("-------------------")
        q = input("Choose an option: ")
        
        if q == '1':
            add_task()

        elif q == '2':
            if not tasks:
                print("Your to-do list is empty!")
            else:
                delete_task()

        elif q == '3':
            if not tasks:
                print("Your to-do list is empty!")
            else:
                mark_as_done()
        
        elif q == '4':
            if not tasks:
                print("Your to-do list is empty!")
            else:
                view_tasks()
        
        elif q == '5':
            while True:
                answer = input("Are you sure you want to clear your to-do list? This action can't be reversed. (Yes/No): ").strip().lower()
                if answer[0] == 'y':
                    tasks = []
                    print("To-do List successfuly cleared.")
                    save_tasks()
                    break
                elif answer[0] == 'n': # I like to assume that the user can't be that stupid (at least I give him the possiblity to type variations of yes and no)
                    print("\nNo changes were made.")
                    break
                else:
                    print("Invalid input! Please enter 'Yes' or 'No'.")
        
        elif q == '6':
            save_tasks()
        
        elif q == '7':
            while True:
                answer = input("Would you like to save before exiting? (Yes/No): ").strip().lower()
                if answer[0] == 'y':
                    save_tasks()
                    print("Exiting...")
                    break
                elif answer[0] == 'n':
                    print("\nExiting...")
                    break
                else:
                    print("Invalid input! Please enter 'Yes' or 'No'.")
            break
                    
        else:
            print("Invalid input! Please enter a valid number.")

main()