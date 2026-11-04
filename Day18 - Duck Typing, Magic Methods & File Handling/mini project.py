#
import os


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


class ContactBook:

    FILE_NAME = "contacts.txt"

    def add_contact(self, contact):
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{contact.name},{contact.phone}\n")

        print("Contact added successfully!")

    def display_contacts(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                contacts = file.readlines()

                if not contacts:
                    print("No contacts found.")
                    return

                print("\n--- Contact List ---")

                for line in contacts:
                    name, phone = line.strip().split(",")
                    print(Contact(name, phone))

        except FileNotFoundError:
            print("Contact file does not exist.")

    def search_contact(self, search_name):
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    name, phone = line.strip().split(",")

                    if name.lower() == search_name.lower():
                        print("Contact Found!")
                        print(Contact(name, phone))
                        return

                print("Contact not found.")

        except FileNotFoundError:
            print("Contact file does not exist.")

    def delete_all_contacts(self):
        if os.path.exists(self.FILE_NAME):
            os.remove(self.FILE_NAME)
            print("All contacts deleted!")
        else:
            print("No contact file found.")


# Main Program

book = ContactBook()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = Contact(name, phone)
        book.add_contact(contact)

    elif choice == "2":
        book.display_contacts()

    elif choice == "3":
        name = input("Enter name to search: ")
        book.search_contact(name)

    elif choice == "4":
        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            book.delete_all_contacts()

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Try again.")
contact()
