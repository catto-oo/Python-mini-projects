import os
import time

filename = r"Contacts Book\contacts.txt"
contacts = {} # dictionary to store {"name": number}

if os.path.exists(filename):
    with open(filename, 'r') as file: # getting the names and numbers from the file
        for line in file:
            name, number = line.strip().split(",")
            contacts[name] = number

while True:
    print("\nMain menu: ")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Exit")
    print("=" * 30)

    pick = input("Choose from the options above: ")

    if pick == "1":
        name = input("Enter the contact's name: ")
        if name in contacts:
            print(f'The name "{name}" is already in your contact list!'); time.sleep(2)
        else:
            number = input("Enter the contact's phone number: ")
            contacts[name] = number

            with open(filename, 'w') as file: # resetting the file while adding the new contact
                for name, number in contacts.items():
                    file.write(f"{name},{number}\n")
            print(f'Contact "{name}" added!'); time.sleep(2)

    elif pick == "2":
        if not contacts: # pre-checking if there are any contacts to delete
            print("Your contacts list is empty!"); time.sleep(2)
        else:
            name = input("Enter the contact name to delete: ")
            
            if name in contacts:
                print(f'Contact "{name}" deleted!'); time.sleep(2)
                del contacts[name]

                with open(filename, 'w') as file: # again resetting the file now without the deleted contact
                    for name, number in contacts.items():
                        file.write(f'{name},{number}\n')
            else:
                print(f"Contact {name} not found."); time.sleep(2)


    elif pick == "3":
        if not contacts:
            print("Your contacts list is empty!"); time.sleep(2)
        else:
            print("\nName:             | Phone:")
            print("-"* 36)
            for name, number in contacts.items():
                print(f"{name:<17} | {number}") # just learnt this thing, it does like spaces or somehting run it to understand
            print("-"* 36); time.sleep(2)

    elif pick == "4":
        print("\nSaving changes...")
        time.sleep(2)
        print("Exiting...")
        time.sleep(1)
        print("Goodbye!")
        break

    else:
        print(f'"{pick}" is not a valid option.')
        time.sleep(2)