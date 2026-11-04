# Important Built-in Functions
from collections.abc import Collection
from inspect import Parameter
from pyclbr import Function


print("Hello")
name = input("Enter name: ")
age = int(input("Enter age: "))
price = float(input("Enter price: "))

print(type(age))
print(isinstance(age, int))
print(str(age))
print(bool(1))

# 3. Print Function
print("Hello", "World", sep="-")
print("Hello", end=" ")
print("Python")
#sep: Separates multiple values.
#end: Controls what is printed at the end.


# Mathematical Functions
print(abs(-5))  # Absolute value
print(max(3, 7, 2))  # Maximum value
print(min(3, 7, 2))  # Minimum value
print(round(3.14159, 2))  # Round to 2 decimal places


# Collection Functions
numbers = [5, 2, 8, 1]

print(len(numbers))
print(sorted(numbers))
print(list(reversed(numbers)))
print(list(enumerate(numbers)))

#Other important functions:
- zip()
- any()
- all()

# Using the Key Parameter
names = ["Ram", "Alexander", "Hari"]
print(sorted(names, key=len))

# Help and Dir Functions
help(print)
print(dir(str))


