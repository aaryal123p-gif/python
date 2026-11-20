# Project 01 · To-Do List
# Build a command-line to-do list
tasks = []
while True:
    print("\n--- TO-DO LIST ---")
    
    task = input("Enter a task (or type 'quit' to exit): ")

    if task.lower() == "quit":
        print("Goodbye!")
        break

    tasks.append(task)

    print("\nYour tasks:")

    count = 1
    for item in tasks:
        print(count, ".", item)
        count += 1

    remove = input("\nEnter the task number to remove (or press Enter to skip): ")

    if remove:
        number = int(remove)

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print("Removed:", removed_task)
        else:
            print("Invalid task number.")

print("\nFinal task list:")
for item in tasks:
    print(item)


# Project 02 · Shopping Cart
# Build a shopping cart calculator
cart = [
    ["Apple", 0.50, 5],
    ["Bread", 2.00, 2],
    ["Milk", 3.50, 1],
    ["Eggs", 0.25, 12]
]

grand_total = 0

print("===== SHOPPING CART =====")

for item in cart:
    name = item[0]
    price = item[1]
    quantity = item[2]

    line_total = price * quantity

    print(f"{name}: ${price:.2f} x {quantity} = ${line_total:.2f}")

    grand_total += line_total

print("=========================")
print(f"Grand Total: ${grand_total:.2f}")


# Project 03 · Capstone
# Build a classroom seating chart

# Seating Chart

seats = [
    ["Empty", "Empty", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"]
]

name = input("Enter the person's name: ")

row = int(input("Enter row number (1-3): "))
column = int(input("Enter column number (1-4): "))

if 1 <= row <= 3 and 1 <= column <= 4:

    if seats[row - 1][column - 1] == "Empty":
        seats[row - 1][column - 1] = name
        print(f"\n{name} has been seated!")
    else:
        print("Sorry, that seat is already taken.")

else:
    print("Invalid row or column number.")

print("\n===== SEATING CHART =====")

for row in seats:
    print(row)

empty_seats = 0

for row in seats:
    empty_seats += row.count("Empty")

print("=========================")
print(f"Empty seats remaining: {empty_seats}")
