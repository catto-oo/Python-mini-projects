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

def view_tasks():
    print("Your to-do list:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. Task Name: {task["name"]}\n   Description: {task["desc"]}\n   Status: {task["status"]}\n")

load_tasks()
view_tasks()