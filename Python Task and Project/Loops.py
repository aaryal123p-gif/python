# Project 01 · for + range
# Times table

# Ask the user for a number
number = int(input("Enter a number: "))

# Print the times table
print(f"\n===== TIMES TABLE OF {number} =====")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

print("==============================")


# Project 02 · while + if
# Guess the number
# Set the secret number
secret_number = 7

# Start counting tries
tries = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess the secret number between 1 and 20!")

# Keep asking until the user guesses correctly
while True:

    guess = int(input("\nEnter your guess: "))

    # Count each attempt
    tries += 1

    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\nCongratulations! You guessed it!")
        print(f"The secret number was {secret_number}.")
        print(f"You got it in {tries} tries!")
        break

print("Thanks for playing!")


# Project 03 · Capstone
# ATM machine
# Starting account balance
balance = 1000

print("===== WELCOME TO PYTHON ATM =====")

while True:

    # Display ATM menu
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    # Check balance
    if choice == "1":
        print(f"\nYour current balance is Rs. {balance}")

    # Deposit money
    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))

        if amount > 0:
            balance += amount
            print(f"Rs. {amount:.2f} deposited successfully!")
            print(f"New balance: Rs. {balance:.2f}")
        else:
            print("Please enter a valid amount.")

    # Withdraw money
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount <= balance:
            balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully!")
            print(f"Remaining balance: Rs. {balance:.2f}")

        else:
            print("Insufficient balance!")
            print(f"Available balance: Rs. {balance:.2f}")

    # Exit ATM
    elif choice == "4":
        print("\nThank you for using Python ATM!")
        print(f"Final balance: Rs. {balance:.2f}")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select 1, 2, 3 or 4.")
