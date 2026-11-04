# Simple ATM machine
balance = 1000

while True:
    print("\\n1. Balance  2. Deposit  3. Withdraw  4. Exit")
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        print(f"Balance: Rs. {balance}")
    elif choice == "2":
        amount = int(input("Amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"New balance: Rs. {balance}")
        else:
            print("Enter an amount greater than 0.")
    elif choice == "3":
        amount = int(input("Amount to withdraw: "))
        if amount <= 0:
            print("Enter an amount greater than 0.")
        elif amount > balance:
            print("Not enough money.")
        else:
            balance -= amount
            print(f"New balance: Rs. {balance}")
    elif choice == "4":
        print("Thank you! Bye.")
        break
    else:
        print("Please choose 1 to 4.")