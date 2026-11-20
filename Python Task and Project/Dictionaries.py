# Project 01 · Basics
# Phone book

# Start with two contacts
phonebook = {
    "Alex": "9841234567",
    "John": "9801234567"
}

# Ask for a new contact
new_name = input("Enter a new contact name: ")
new_number = input("Enter phone number: ")

# Add the new contact
phonebook[new_name] = new_number

# Print all contacts
print("\n===== PHONEBOOK =====")

for name, number in phonebook.items():
    print(f"{name}: {number}")

# Print total contacts
print("\nTotal contacts:", len(phonebook))

# Search for a contact
search_name = input("\nEnter a name to search: ")

# Use get() to safely search
result = phonebook.get(search_name, "Not found")

print(f"Phone number: {result}")

print("=====================")


# Project 02 · Methods
# Tea shop bill
# Create a menu dictionary
menu = {
    "burger": 250,
    "pizza": 500,
    "momo": 150,
    "coffee": 100,
    "sandwich": 200
}

# Display the menu
print("===== SHOP MENU =====")

for item, price in menu.items():
    print(f"{item}: Rs. {price}")

# Ask customer for their order
choice = input("\nWhat would you like to order? ").lower()
quantity = int(input("How many would you like? "))

# Find the price using get()
price = menu.get(choice, 0)

# Calculate and print the bill
if choice in menu:
    total = price * quantity

    print("\n===== YOUR BILL =====")
    print(f"Item: {choice}")
    print(f"Price: Rs. {price}")
    print(f"Quantity: {quantity}")
    print(f"Total bill: Rs. {total}")
else:
    print("\nSorry, item not found in the menu!")

# Add a new item to the menu
menu["juice"] = 120

# Print menu facts
print("\n===== MENU FACTS =====")
print("Total menu items:", len(menu))
print("All menu items:", list(menu.keys()))
print("All prices:", list(menu.values()))
print("Updated menu:", menu)


# Project 03 · Capstone
# Report card

# Ask for student's name
name = input("Enter student name: ")

# Define subjects
subjects = ["Math", "Science", "English"]

# Ask for three marks
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Use zip() to build marks dictionary
marks_dict = dict(zip(subjects, marks))

# Create report dictionary
report = {
    "name": name,
    "marks": marks_dict
}

# Calculate total and average
total = sum(report["marks"].values())
average = total / len(report["marks"])

# Find best subject
best_subject = max(report["marks"], key=report["marks"].get)
best_mark = report["marks"][best_subject]

# Print report card
print("\n==============================")
print("         REPORT CARD")
print("==============================")

print("Student Name:", report["name"])

for subject, mark in report["marks"].items():
    print(f"{subject}: {mark}")

print("------------------------------")
print("Total Marks:", total)
print(f"Average Marks: {average:.2f}")
print(f"Best Subject: {best_subject} ({best_mark})")

print("==============================")