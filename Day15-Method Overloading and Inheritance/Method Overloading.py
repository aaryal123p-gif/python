# Method Overloading
# Meaning: One method name can work with different numbers or types of inputs.

# Python does not support traditional method overloading directly. We use default arguments or *args.

# A. Using default arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(2, 3))       # 5
print(calc.add(2, 3, 4))    # 9

# B. Using if/else
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self, time=""):
        if time == "":
            print(f"Hi, I am {self.name}")
        else:
            print(f"Good {time}, I am {self.name}")


s1 = Student("Ram")

s1.greet()
s1.greet("morning")

# C. Using *args
# *args allows a method to accept any number of arguments. It collects them into a tuple.
class Calculator:
    def add(self, *numbers):
        return sum(numbers)


calc = Calculator()

print(calc.add(5))               # 5
print(calc.add(5, 10))           # 15
print(calc.add(5, 10, 15, 20))   # 50

# D. Real-life example
class MomoShop:
    def order(self, item="buff momo", plates=1):
        price = 150 * plates
        print(f"{plates} plate {item}: Rs. {price}")


shop = MomoShop()

shop.order()
shop.order("chicken momo")
shop.order("veg momo", 3)
