# Project 01 · Calculator 
# Build a menu-driven calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation:")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")
choice = input("Enter your choice (1-4): ")
match choice:
    case "1":
        result = num1 + num2
        print(f"Result: {result:.2f}")
    case "2":
        result = num1 - num2
        print(f"Result: {result:.2f}")
    case "3":
        result = num1 * num2
        print(f"Result: {result:.2f}")
    case "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {result:.2f}")
    case _:
        print("Invalid choice. Please select 1, 2, 3, or 4.")


# Project 02 · Receipt Generator
# Build a shopping receipt
item_name = input("Enter the item name: ")
price = float(input("Enter the price per item: "))
quantity = int(input("Enter the quantity bought: "))
subtotal = price * quantity
vat = subtotal * 0.13
total = subtotal + vat
print("\n" + "=" * 36)
print(f"{'RECEIPT':^36}")
print("=" * 36)
print(f"Item:       {item_name}")
print(f"Price:      Rs. {price:.2f}")
print(f"Quantity:   {quantity}")
print("-" * 36)
print(f"Subtotal:   Rs. {subtotal:.2f}")
print(f"VAT (13%):  Rs. {vat:.2f}")
print("=" * 36)
print(f"Final total: Rs. {total:.2f}")
print("=" * 36)


# Project 03 · Capstone
# Build a profile card generator
full_name = input("Enter your full name: ")
birth_year = int(input("Enter your birth year: "))
clean_name = full_name.strip().title()
current_year = 2026
age = current_year - birth_year
name_is_long = len(clean_name.replace(" ", "")) > 10
print("\n" + "=" * 36)
print(f"{'PROFILE CARD':^36}")
print("=" * 36)
print(f"Name:       {clean_name.upper()}")
print(f"Age:        {age}")
print(f"Long name:  {'Yes' if name_is_long else 'No'}")
print("=" * 36)
