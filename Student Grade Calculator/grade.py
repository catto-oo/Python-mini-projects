import os

filename = r"Student Grade Calculator\grades.txt"

subjects = ["Math", "Physics", "English", "French", "History"]

def load_grades():
    if not os.path.exists(filename):
        return {} # empty dict cuz no file means no students
    
    with open(filename, "r") as file:
        students = {}
        for line in file:
            if not line.strip(): # if a line is empty we skip it
                continue

            name, grades = line.strip().split(":")
            grades = list(map(float, grades.split(","))) # turning the grades into a float using map(), then turning that into a list
            students[name] = grades

        return students

def save_grades(students):
    with open(filename, "w") as file:
        for name, grades in students.items():
            file.write(f"{name}:{','.join(map(str, grades))}\n") # so we can write as "name:18,9,15.5,13.25,17"

def add_student(students):
    name = input("Enter the student's name: ")
    if name in students:
        print(f"The student '{name}' already exists.")
        return
    
    grades = []
    print("\nEnter the grades for Math, Physics, English, French, and History.")
    
    for subject in ["Math", "Physics", "English", "French", "History"]:
        while True:
            try:
                grade = float(input(f"{subject}: "))
                if 0 <= grade <= 20:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade between 0 and 20.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    students[name] = grades
    save_grades(students)
    print(f"{name}'s grades have been saved successfully.")

def student_average(students):
    if not students:
        print("\nThere are no students.")
        return
    
    name = input("Enter the student's name to calculate their average grade: ")
    found = None # to check if student is found or not

    for student in students:
        if student.lower() == name.lower():
            found = student
            break
        
    if not found:
        print(f"Student '{name}' doesn't exist.")
        return
    
    grades = students[found]
    average = sum(grades) / len(grades)
    print(f"\n{found}'s average grade: {average:.2f}") # 2 decimal places because division

def class_average(students):
    if not students:
        print("\nThere are no students.")
        return
    
    # to calculate average for each subject, then average of everything
    subject_averages = [0] * 5 # 5 subjects
    total_students = len(students)
    
    for grades in students.values():
        for i in range(5): # range 5 cuz 5 subjects
            subject_averages[i] += grades[i] # accumulating grades into the averages list
    
    print("\nClass averages.")
    for i in range(5):
        print(f"{subjects[i]} average: {subject_averages[i] / total_students:.2f}") # total grades for subject / students
    
    overall_average = sum(subject_averages) / (total_students * 5) # times 5 cuz 5 subjects
    print(f"\nOverall class average: {overall_average:.2f}")

def view_grades(students):
    if not students:
        print("\nThere are no students.")
        return
    
    name = input("Enter the student's name to view their grades: ")
    found = None # to check if student is found or not

    for student in students:
        if student.lower() == name.lower():
            found = student
            break
        
    if not found:
        print(f"Student '{name}' doesn't exist.")
        return
    
    grades = students[found]
    print(f"\n{found}'s grades.")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {grades[i]}")

def view_students(students):
    if not students:
        print("\nThere are no students.")
        return
    
    print("\nStudents:")
    for name in students:
        print(f"- {name}")

def main():
    print("\n-----------------------")
    print("Student Grade Manager")
    print("-----------------------")

    students = load_grades()

    while True:
        print("\n1. Add a new student")
        print("2. View a student's grades")
        print("3. Calculate a student's average")
        print("4. View class averages")
        print("5. View Students")
        print("6. Exit")
        
        q = input("Choose an option: ")
        
        if q == "1":
            add_student(students)
        elif q == "2":
            view_grades(students)
        elif q == "3":
            student_average(students)
        elif q == "4":
            class_average(students)
        elif q == "5":
            view_students(students)
        elif q == "6":
            print("\nGoodbye, Mr. Teacher.")
            break
        else:
            print("Enter a valid number pleaaaaaaase.")

main()