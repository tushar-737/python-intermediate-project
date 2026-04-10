contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added!")

    elif choice == "2":
        if contacts:
            for name, number in contacts.items():
                print(name, ":", number)
        else:
            print("No contacts found")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")