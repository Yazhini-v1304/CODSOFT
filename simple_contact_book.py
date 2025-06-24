contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts saved.\n")

    else:
        print("\nContact list:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

def search_contact():
    name = input ("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}\n")
    else:
        print("contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print ("Contact deleted.\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("=== Contact Book ===")
        print("1.Add Contact")
        print("2.View Contacts")
        print("3.Search Contacts")
        print("4.Delete Contact")
        print("5.Exit")

        choice = input("Choose an option (1-5):")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")
menu()
      
    
         
