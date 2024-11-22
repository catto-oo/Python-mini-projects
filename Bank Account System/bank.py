import os
from datetime import datetime # used in logging the transactions for fun

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
    
    def log_action(self, text): # tracks withdrawals and deposits

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # uhhh idk i just copied this

        if not os.path.exists(fileLog):
            with open(fileLog, 'w') as file:  # create the log file if it doesn't exist
                file.write(f"Log file created.\n")

        with open(fileLog, 'a') as file:
            file.write(f"[{time}] {self.username}: {text}\n")

    def show_balance(self):
        print(f"Your current balance is: {self.balance} MAD")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            text = f"Deposited {amount} MAD. New balance: {self.balance} MAD"
            print(text)
            self.log_action(text)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            text = f"Withdrew {amount} MAD. New balance: {self.balance} MAD" 
            print(text)
            self.log_action(text)
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
                    account = BankAccount(name, password, 0)
                    accounts.append(account)  # create a new account with 0 balance
                    print(f"Account successfully created. Welcome, {name}")

                    with open(fileAccounts, 'a') as file: # updating the accounts.txt with the new account
                        file.write(f"{name},{password},0\n")
                    
                    return account
                    
                else:
                    print("The passwords don't match.")
            break
        else:
            print("This username is taken. Pick a different one.")

def sign_in():
    name = input("\nEnter your username: ")

    account = None # intializing as none
    for acc in accounts:
        if acc.username.lower() == name.strip().lower():
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
                return account # using this in main()
            else:
                print("Wrong password.")
                trial += 1
        if trial == 3:
            print("Too many failed attempts. Access denied.")
            return None
        
def main():
    while True:
        print("\nBank!")
        action = input("Do you already have an account? (Yes/No): ").strip().lower()
        if action == "no":
            account = sign_up() # this should be either None or an object
            if account:
                break
        elif action == "yes":
            account = sign_in() # this should be either None or an object
            if account: # if it isn't None and is an object
                break
        else:
            print("Please enter 'Yes' or 'No' specifically. This is a bank, come on dude.")

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Sign Out")

        q = input("Choose an option: ")
        
        if q == '1':
            amount = int(input("How much would you like to deposit? (MAD): "))
            account.deposit(amount)

        elif q == '2':
            amount = int(input("How much would you like to withdraw? (MAD): "))
            account.withdraw(amount)

        elif q == '3':
            account.show_balance()

        elif q == '4':
            with open(fileAccounts, 'w') as file:
                for account in accounts: # task is a dict
                    file.write(f"{account.username},{account.password},{account.balance}\n")

            print("You have been signed out.")
            break

        else:
            print("Invalid input! Please enter a valid number.")

main()