def Addition(a, b):
    print(a+b)

def Substraction(a, b):
    print(a-b)

def Multiplication(a, b):
    result = a*b
    if result.is_integer(): # converting result to int without .0 if it's an int
        result = int(result)
    print(round(result, 2))

def Division(a, b):
    if b == 0:
        print("Error: You cannot divide by zero!")
    else:
        print(round(a / b, 2))

def Repeat(): # if user wants to use the calculator again
    while True:
        inp = input("Would you like to leave? (Yes/No): ").strip().lower()
        if inp[0] == 'y':
            return False
        elif inp[0] == 'n':
            return True
        else:
            print("Invalid Input! Please enter 'Yes' or 'No'.")

def main():
    while True:
        nums = input("\nEnter two numbers, a and b respectively, separated by a space: ").split()
        if len(nums) != 2:
            print("You must enter exactly two numbers!")
            continue

        try:
            a, b= float(nums[0]), float(nums[1])
            a = int(a) if a.is_integer() else a # if a=5.0 turn it into a=5 so it looks good
            b = int(b) if b.is_integer() else b 

        except ValueError:
            print("A value error has occured! Please enter valid numbers.")
            continue
        
        while True:
            print("\nChoose the number of your desired operation:")
            q = input(f"1. Addition ({a} + {b})\n2. Substraction ({a} - {b})\n3. Multiplication ({a} * {b})\n4. Division ({a} / {b})\n")

            if q == '1':
                print(f"\n=> {a} + {b} = ", end="")
                Addition(a, b)
                break

            elif q == '2':
                print(f"\n=> {a} - {b} = ", end="")
                Substraction(a, b)
                break

            elif q == '3':
                print(f"\n=> {a} * {b} = ", end="")
                Multiplication(a, b)
                break
            
            elif q == '4':
                print(f"\n=> {a} / {b} = ", end="")
                Division(a, b)
                break

            else:
                print("Invalid input! Please enter a valid number.")
        
        if Repeat() == False:
            print("Farewell.")
            break


main()