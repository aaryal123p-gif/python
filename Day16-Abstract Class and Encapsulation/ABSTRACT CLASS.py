# Definition:
# An abstract class is a blueprint or plan for child classes.
# We cannot create an object directly from an abstract class.
# Child classes MUST implement its abstract methods.

# Import ABC and abstractmethod
from abc import ABC, abstractmethod


# Basic Syntax:

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child class must implement the abstract method.

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Creating child objects
s1 = Square(4)
c1 = Circle(2)

print(s1.area())  # 16
print(c1.area())  # 12.56

#   ABSTRACT CLASS EXAMPLE: PAYMENT SYSTEM
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Esewa(Payment):

    def pay(self, amount):
        print(f"Paid Rs. {amount} using eSewa")


class Khalti(Payment):

    def pay(self, amount):
        print(f"Paid Rs. {amount} using Khalti")


e = Esewa()
k = Khalti()

e.pay(500)
k.pay(200)
