# EXCEPTIONS AND EXCEPTION HANDLING
# Extracted from the uploaded Day-15.html lesson.
# Each section is a separate example. Run one section at a time;
# some examples intentionally raise errors to demonstrate exceptions.




# DAY 15 — PYTHON EXCEPTIONS AND EXCEPTION HANDLING
# Extracted from the uploaded Day-15.html lesson.
# Each section is a separate example. Run one section at a time;
# some examples intentionally raise errors to demonstrate exceptions.


# ================== EXAMPLE 01 ==================

# Day 13: string with a dot into int()
print(int("10.56"))
# ValueError: invalid literal for int() with base 10: '10.56'

# Day 14: recursion with no base case
# RecursionError: maximum recursion depth exceeded

# Day 14: next() on a finished generator
# StopIteration

# Day 14: calling inner() from outside
# NameError: name 'inner' is not defined


# ================== EXAMPLE 02 ==================

age_text = "ten"
age = int(age_text)
print("Done")

# Traceback (most recent call last):
#   File "day-15.py", line 2, in <module>
#     age = int(age_text)
# ValueError: invalid literal for int() with base 10: 'ten'


# ================== EXAMPLE 03 ==================

try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a number!")

print("Program continues...")

# Enter your age: 20
# Next year you will be 21
# Program continues...

# Enter your age: ten
# Please type a number!
# Program continues...


# ================== EXAMPLE 04 ==================

try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Answer:", a / b)
except ValueError:
    print("Please type numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero.")

# First number: 10
# Second number: 0
# You can't divide by zero.

# First number: 10
# Second number: abc
# Please type numbers only.


# ================== EXAMPLE 05 ==================

try:
    num = int("12abc")
except ValueError as e:
    print("Error:", e)
# Error: invalid literal for int() with base 10: '12abc'

# Two errors, one block: use a tuple
try:
    print(10 / 0)
except (ValueError, ZeroDivisionError) as e:
    print("Problem:", e)
# Problem: division by zero


# ================== EXAMPLE 06 ==================

def check_age(text):
    try:
        age = int(text)
    except ValueError:
        print("Not a number!")
    else:
        print("Your age is", age)
    finally:
        print("--- check done ---")

check_age("25")
# Your age is 25
# --- check done ---

check_age("abc")
# Not a number!
# --- check done ---


# ================== EXAMPLE 07 ==================

nums = [10, 20, 30]

try:
    print(nums[1])
    print(nums[5])
    print("A")
except IndexError:
    print("B")
else:
    print("C")
finally:
    print("D")

try:
    print(int("7") + 3)
except ValueError:
    print("E")
else:
    print("F")

print(10 / 0)


# ================== EXAMPLE 08 ==================

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("That's not a number. Try again.")

print("Thanks! Your age is", age)

# Enter your age: twenty
# That's not a number. Try again.
# Enter your age: 2o
# That's not a number. Try again.
# Enter your age: 20
# Thanks! Your age is 20


# ================== EXAMPLE 09 ==================

def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Numbers only, please!")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"

x = get_number("First number: ")
y = get_number("Second number: ")
print(safe_divide(x, y))

# First number: 8
# Second number: zero
# Numbers only, please!
# Second number: 0
# Can't divide by zero


# ================== EXAMPLE 10 ==================

age = -5

if age < 0:
    raise ValueError("Age can't be negative")

print("Age saved")    # never runs

# Traceback (most recent call last):
#   File "day-15.py", line 4, in <module>
#     raise ValueError("Age can't be negative")
# ValueError: Age can't be negative


# ================== EXAMPLE 11 ==================

def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    print("Age saved:", age)

set_age(20)
# Age saved: 20

try:
    set_age(-5)
except ValueError as e:
    print("Error:", e)
# Error: Age can't be negative


# ================== EXAMPLE 12 ==================

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above!")

    print("Access granted!")

except ValueError as e:
    print("Error:", e)

print("Program continues...")

# 20  → Access granted!
# 17  → Error: Age must be 18 or above!
# ten → Error: invalid literal for int() with base 10: 'ten'


# ================== EXAMPLE 13 ==================

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please type a number.")

print("=== Safe Calculator ===")
a = get_number("First number: ")
op = input("Choose + - * / : ")
b = get_number("Second number: ")

try:
    if op == "+":
        print("Answer:", a + b)
    elif op == "-":
        print("Answer:", a - b)
    elif op == "*":
        print("Answer:", a * b)
    elif op == "/":
        print("Answer:", a / b)
    else:
        print("Unknown sign:", op)
except ZeroDivisionError:
    print("You can't divide by zero!")

# === Safe Calculator ===
# First number: ten
# Please type a number.
# First number: 10
# Choose + - * / : /
# Second number: 0
# You can't divide by zero!

# Your job:
# 1. add % (remainder) and ** (power)
# 2. put it all in a while loop and ask
#    "Again? (y/n)" at the end

# ================== EXAMPLE 14 ==================

menu = {"veg momo": 120, "chicken momo": 180, "chowmein": 150}
total = 0

print("=== MOMO HOUSE ===")
for item, price in menu.items():
    print(f"- {item}: Rs. {price}")

while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    try:
        price = menu[item]
        qty = int(input("How many? "))
    except KeyError:
        print("Sorry, we don't have", item)
    except ValueError:
        print("Quantity must be a number.")
    else:
        total += price * qty
        print(f"Added {qty} x {item}")

print("Total bill: Rs.", total)

# Item (or done): pizza
# Sorry, we don't have pizza
# Item (or done): veg momo
# How many? two
# Quantity must be a number.
# Item (or done): veg momo
# How many? 2
# Added 2 x veg momo
# Item (or done): done
# Total bill: Rs. 240

# Your job:
# 1. if qty is 0 or less, raise ValueError("Quantity
#    must be more than 0"), and print e in except
# 2. save each order in a list and print it at the end


# ================== EXAMPLE 15 ==================

def average(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0

def add_mark(marks, text):
    mark = int(text)
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be 0 to 100")
    marks.append(mark)

marks = []
print("Type marks one by one. Type q to finish.")
while True:
    text = input("Mark: ")
    if text == "q":
        break
    try:
        add_mark(marks, text)
    except ValueError as e:
        print("Skipped:", e)

print("Marks:", marks)
print("Average:", round(average(marks), 1))

# Mark: 80
# Mark: abc
# Skipped: invalid literal for int() with base 10: 'abc'
# Mark: 150
# Skipped: Mark must be 0 to 100
# Mark: 70
# Mark: q
# Marks: [80, 70]
# Average: 75.0

# Your job:
# 1. print Pass if average >= 40, else Fail
# 2. print max() and min() of marks. What happens
#    if the list is empty? Catch that error too!