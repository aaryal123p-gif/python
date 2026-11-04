# 1. What is polymorphism?
# Polymorphism means one name, many forms.
# - Poly = Many
# - Morph = Forms
# - The same method name performs different tasks for different objects.
# Example:
# - Dog → Woof
# - Cat → Meow
# - Cow → Moo


# 2. Built-in polymorphism
# Python already provides polymorphism through functions and operators.
# len() works with different data types

print(len("Nepal"))          # 5
print(len([10, 20, 30]))     # 3
print(len({"a": 1, "b": 2})) # 2


# + operator works differently

print(5 + 3)                 # 8
print("Ram" + "Hari")        # RamHari
print([1, 2] + [3, 4])       # [1, 2, 3, 4]


# 2. Built-in polymorphism
# Python already provides polymorphism through functions and operators.
# len() works with different data types

print(len("Nepal"))          # 5
print(len([10, 20, 30]))     # 3
print(len({"a": 1, "b": 2})) # 2


# + operator works differently

print(5 + 3)                 # 8
print("Ram" + "Hari")        # RamHari
print([1, 2] + [3, 4])       # [1, 2, 3, 4]


# 3. Polymorphism with different classes
# Different classes can have the same method name but different implementations.
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

# 4. Polymorphism using a function
# One function can work with different objects if they have the required method.
class Car:
    def move(self):
        print("Car drives on the road")


class Plane:
    def move(self):
        print("Plane flies in the sky")


def start_trip(vehicle):
    print("Trip started!")
    vehicle.move()


start_trip(Car())
start_trip(Plane())



# 5. Polymorphism with inheritance (Method Overriding)
# Method overriding: When a child class provides its own implementation of a method already defined in the parent class.
class Bird:
    def fly(self):
        print("Bird flies high")


class Sparrow(Bird):
    pass


class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly, it swims")


class Kiwi(Bird):
    def fly(self):
        print("Kiwi cannot fly, it runs")


birds = [Sparrow(), Penguin(), Kiwi()]

for bird in birds:
    bird.fly()

# 6. Polymorphism with abstract classes
# An abstract class ensures that every child class implements its required abstract methods.
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Esewa(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with eSewa")


class Khalti(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with Khalti")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with Card")


def checkout(method, amount):
    method.pay(amount)


checkout(Esewa(), 500)
checkout(Khalti(), 200)
checkout(Card(), 1000)