# Method overloading
# Method overloading: One method name can work with different numbers of arguments.

# Python does not support traditional method overloading by defining multiple methods with the same name. We can achieve similar behavior using default arguments or *args.

# A. Using default arguments
class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(2, 3))
print(calc.add(2, 3, 4))

# B. Using *args?
class Calculator:

    def total(self, *args):
        return sum(args)


calc = Calculator()

print(calc.total(1, 2))
print(calc.total(1, 2, 3, 4, 5))

# Momo shop bill
from abc import ABC, abstractmethod


class Food(ABC):

    def __init__(self, plates):
        self.plates = plates

    @abstractmethod
    def price(self):
        pass


class Momo(Food):
    def price(self):
        return self.plates * 150


class Chowmein(Food):
    def price(self):
        return self.plates * 120


class Pizza(Food):
    def price(self):
        return self.plates * 500


order = [Momo(2), Chowmein(1), Pizza(1)]

total = 0

for food in order:
    total += food.price()

print("Total bill: Rs.", total)