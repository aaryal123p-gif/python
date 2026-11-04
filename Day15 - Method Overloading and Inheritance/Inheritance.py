# 2. Inheritance
# Meaning: Inheritance allows a child class to receive properties and methods from a parent class.
# - Parent class = Base class / Super class
# - Child class = Derived class / Sub class


# A. Basic inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    pass


d1 = Dog("Tommy")

d1.eat()
print(d1.name)


# B. Child class adding its own methods
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")


d1 = Dog("Tommy")
c1 = Cat("Kitty")

d1.eat()
d1.bark()

c1.eat()
c1.meow()

# C. isinstance()
# Checks whether an object belongs to a particular class or its parent class.
class Animal:
    pass


class Dog(Animal):
    pass


d1 = Dog()
a1 = Animal()

print(isinstance(d1, Dog))       # True
print(isinstance(d1, Animal))   # True
print(isinstance(a1, Dog))       # False



