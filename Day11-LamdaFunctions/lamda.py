# 1. WHAT IS A LAMBDA FUNCTION?
# A lambda function is a small anonymous function.
# It can have multiple arguments but only one expression.
#
# Syntax:
# lambda arguments: expression

square = lambda x: x * x
print(square(5))  # 25


# 2. LAMBDA VS NORMAL FUNCTION

# Normal function
def add(a, b):
    return a + b

print(add(10, 20))

# Lambda function
addition = lambda a, b: a + b
print(addition(10, 20))


# 3. LAMBDA WITH MULTIPLE ARGUMENTS

multiply = lambda a, b: a * b
print(multiply(5, 4))  # 20

divide = lambda a, b: a / b
print(divide(10, 2))  # 5.0


# 4. LAMBDA WITH IF-ELSE

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))


# 5. USING LAMBDA WITH sorted()

numbers = [5, 2, 9, 1, 7]

result = sorted(numbers)
print(result)

# Sort in descending order
result = sorted(numbers, reverse=True)
print(result)


# 6. SORTING USING LAMBDA

students = [
    ("Ram", 85),
    ("Shyam", 70),
    ("Hari", 95),
    ("Sita", 80)
]

# Sort according to marks
result = sorted(students, key=lambda x: x[1])
print(result)


# 7. SORTING A LIST OF DICTIONARIES

students = [
    {"name": "Ram", "age": 22},
    {"name": "Shyam", "age": 19},
    {"name": "Hari", "age": 25}
]

result = sorted(students, key=lambda x: x["age"])
print(result)


# 8. USING LAMBDA WITH max()

numbers = [10, 25, 5, 40, 15]

largest = max(numbers)
print(largest)


# 9. USING LAMBDA WITH min()

smallest = min(numbers)
print(smallest)


# 10. SORTING DICTIONARY ITEMS

marks = {
    "Ram": 85,
    "Shyam": 70,
    "Hari": 95
}

result = sorted(marks.items(), key=lambda x: x[1])
print(result)


# 11. USING map() WITH LAMBDA

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))
print(result)

# Output: [2, 4, 6, 8, 10]


# 12. USING filter() WITH LAMBDA

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# Output: [2, 4, 6]


# 13. COMBINING map() AND filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(
    map(
        lambda x: x * 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)

# First, filter even numbers.
# Then, multiply each selected number by 2.


# 14. WHY DO WE USE list()?

# map() and filter() return iterator objects.
# list() converts their results into a list.

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)
print(list(result))


# 15. COMMON MISTAKES

# A lambda expression contains one expression, not multiple statements.
# Incorrect example (do not uncomment):
# lambda x: result = x + 2

# Correct:
result = lambda x: x + 2
print(result(5))

# Incorrect syntax (do not uncomment):
# lambda x x * 2

# Correct:
result = lambda x: x * 2
print(result(5))


# 16. WHEN TO USE LAMBDA?

# Use lambda for short, simple expressions.
# Use def for more complex functions or multiple statements.

# Lambda example
double = lambda x: x * 2
print(double(5))

# Normal function example
def calculate_total(a, b, c):
    total = a + b + c
    return total

print(calculate_total(10, 20, 30))