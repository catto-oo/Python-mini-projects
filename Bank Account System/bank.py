import os
accountsFile = r"Bank Account System\accounts.txt"
logFile = r"Bank Account System\log.txt"
accounts = {}

def load_accounts():
    if os.path.exists(accountsFile):
        with open(accountsFile, 'r') as file:
            for line in file:
                name, password = line.strip().split(",")
                accounts[name] = password

load_accounts()