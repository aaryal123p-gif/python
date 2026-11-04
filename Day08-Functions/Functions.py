# 1. BASIC FUNCTION
def say_hello():
    print("Hello!")
    print("Welcome to Python class")

say_hello()


# 2. FUNCTION WITH PARAMETER
def greet(name):
    print(f"Namaste, {name}!")

greet("Ram")
greet("Sita")


# 3. FUNCTION WITH MULTIPLE PARAMETERS
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Hari", 20)


# 4. DEFAULT PARAMETER
def order_tea(name, sugar=1):
    print(f"{name}: Tea with {sugar} sugar")

order_tea("Ram")
order_tea("Sita", 2)


# 5. KEYWORD ARGUMENTS
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Gita")


# 6. RETURN STATEMENT
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# 7. PRINT VS RETURN
def show_total():
    print(100)

def get_total():
    return 100

show_total()
answer = get_total()
print(answer)


# 8. RETURN TRUE OR FALSE
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))


# 9. RETURN MULTIPLE VALUES
def lowest_highest(numbers):
    return min(numbers), max(numbers)

marks = [67, 45, 92, 78]
low, high = lowest_highest(marks)

print("Lowest:", low)
print("Highest:", high)


# 10. FUNCTION WITH A LOOP
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table(5)


# 11. LOCAL VARIABLE
def calculate():
    total = 500
    print("Inside function:", total)

calculate()


# 12. FUNCTION USING ANOTHER FUNCTION
def subtotal(price, quantity):
    return price * quantity

def add_vat(amount):
    return amount + amount * 13 / 100

def bill_total(price, quantity):
    amount = subtotal(price, quantity)
    return add_vat(amount)

print("Final bill:", bill_total(150, 2))
