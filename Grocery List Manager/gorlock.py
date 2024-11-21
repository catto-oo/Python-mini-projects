import os

groceries = {}
filename = r"Grocery List Manager\list.txt"

def load_items():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                item, amount = line.strip().split(',')
                groceries[item] = int(amount)

def save_items():
    with open(filename, 'w') as file:
        for item, amount in groceries.items():
            file.write(f"{item},{amount}\n")

def get_valid_amount(): # to get a valid amount of items to add/delete
    while True:
        try:
            amount = int(input("How many of it? "))
            if amount <= 0:
                print("Invalid input! Please enter a positive number.")
            else:
                return amount
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    load_items()
    print("Welcome to your Grocery List Manager!")

    while True:
        print("\n1. Add Items")
        print("2. Remove Items")
        print("3. View List")
        print("4. Save & Exit")

        q = input("Choose an option: ")

        if q == '1':
            item = input("What item would you like to add? ").capitalize()
            amount = get_valid_amount()

            if item not in groceries:
                groceries[item] = amount
                print(f"'{item}' successfully added to your list!")
            else:
                print(f"'{item}' is already in your list, {amount} has been added to its amount.")
                groceries[item] += amount

        elif q == '2':
            if not groceries:
                print("There are no items to remove.")
            else:
                item = input("Which item would you like to remove? ").capitalize()
                if item in groceries:

                    amount = get_valid_amount()
                    if amount >= groceries[item]:
                        print(f"'{item}' has been completely removed from your list.")
                        groceries.pop(item)
                    else:
                        print(f"{amount} of '{item}' have been removed from your list")
                        groceries[item] -= amount

        elif q == '3':
            if not groceries:
                print("Your grocery list is empty.")
            else:
                print("Your grocery list contains:")
                for item, amount in groceries.items():
                    print(f"- {item}: {amount}")

        elif q == '4':
            save_items()
            print("Saving...\n...\n\nGoodbye!")
            break

        else:
            print("Invalid input! Please enter a valid number.")

main()