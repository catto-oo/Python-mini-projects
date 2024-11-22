import os
fileAccounts = r"Bank Account System\accounts.txt"
fileLog = r"Bank Account System\log.txt"
accounts = []

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def check_password(self, password):
        return self.password == password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


if os.path.exists(fileAccounts): # loading account names and passwords into a dict
    with open(fileAccounts, 'r') as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0].strip()
            password = data[1].strip()
            try:
                balance = int(data[2])
            except ValueError:
                print(f"Invalid balance for user {name}, resetting to 0.")
                balance = 0
            accounts.append(BankAccount(name,password,balance))

else:
    print("Directory for accounts.txt doesn't exist. Please create it.")

def sign_up():
    print("\nAccount Creation")
    while True:
        name = input("\nEnter your username: ")

        if not any(account.username.lower() == name.strip().lower() for account in accounts): # checking if there are any objects with that name
            while True:
                password = input("Enter your password: ")

                if len(password) < 8:  # password length
                    print("Password is too short. Please enter a password with at least 8 characters.")
                    continue

                test = input("Reenter your password: ")
                if password == test:
                    accounts.append(BankAccount(name, password, 0))  # create a new account with 0 balance
                    print(f"Account successfully created. Welcome, {name}")

                    with open(fileAccounts, 'a') as file: # updating the accounts.txt with the new account
                        file.write(f"{name},{password},0\n")
                    
                    return True
                    
                else:
                    print("The passwords don't match.")
            break
        else:
            print("This username is taken. Pick a different one.")

def sign_in():
    name = input("\nEnter your username: ").strip().lower()

    account = None # intializing as none
    for acc in accounts:
        if acc.username.lower() == name:
            account = acc # if it finds the name, account becomes that object
            break


    if account is None:
        print("This username doesn't exist.")
    else:
        trial = 0
        while trial < 3:
            test = input("Enter your password: ")
            if account.check_password(test): # check_password method returns True if passwords match
                print(f"Sign in successful. Welcome, {name}.")
                return True # using this to start the program
            else:
                print("Wrong password.")
                trial += 1
        if trial == 3:
            print("Too many failed attempts. Access denied.")
            return False
        
def main():
    while True:
        print("Bank!!!!")
        action = input("Do you already have an account? (Yes/No): ").strip().lower()
        if action == "no":
            if sign_up(): # if it returns true we break the loop and continue the program
                break
        elif action == "yes":
            if sign_in(): # if it returns true we break the loop and continue the program
                break
        else:
            print("Please enter 'Yes' or 'No' specifically. This is a bank, come on dude.")

main()