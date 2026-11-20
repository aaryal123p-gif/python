# Project 01 · Basics
# Number checker
# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is positive, negative or zero
if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")

else:
    print("The number is zero.")

# Check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")

else:
    print("The number is odd.")


# Project 02 · Dictionary + if
# Login system

# Store usernames and passwords in a dictionary
users = {
    "ram": "1234",
    "sita": "abcd",
    "hari": "5678"
}

# Ask the user to log in
username = input("Enter your username: ")

# Clean the username
username = username.strip().lower()

password = input("Enter your password: ")

# Check if username exists
if username in users:

    # Check if password is correct
    if users[username] == password:
        print("\nLogin successful!")
        print(f"Welcome, {username}!")

    else:
        print("\nIncorrect password!")

else:
    print("\nUsername not found!")


# Project 03 · Capston
# Tea shop with discount

# 03_tea_shop.py

# Create menu dictionary
menu = {
    "milk tea": 30,
    "black tea": 20,
    "lemon tea": 25,
    "coffee": 50,
    "green tea": 40
}

# Display the menu
print("===== TEA SHOP MENU =====")

for item, price in menu.items():
    print(f"{item}: Rs. {price}")

print("=========================")

# Ask customer for an item
choice = input("\nWhat would you like to order? ")
choice = choice.strip().lower()

# Check if item is available
if choice in menu:

    quantity = int(input("How many would you like? "))

    price = menu[choice]
    total = price * quantity

    print("\n===== YOUR BILL =====")
    print(f"Item: {choice}")
    print(f"Price: Rs. {price}")
    print(f"Quantity: {quantity}")
    print(f"Original total: Rs. {total}")

    # Calculate discount
    if total >= 500:
        discount = total * 0.20
        print("Discount: 20%")

    elif total >= 300:
        discount = total * 0.10
        print("Discount: 10%")

    else:
        discount = 0
        print("Discount: 0%")

    # Calculate final bill
    final_total = total - discount

    print(f"Discount amount: Rs. {discount:.2f}")
    print(f"Final bill: Rs. {final_total:.2f}")

else:
    print("\nSorry, that item is not available!")

print("\nThank you for visiting our tea shop!")
