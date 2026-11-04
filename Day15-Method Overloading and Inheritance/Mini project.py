# 1. Calculator – Multiply using default arguments
# Question: Create a Calculator class with a multiply() method. The third argument should have a default value of 1.
# Question 1: Calculator

class Calculator:
    def multiply(self, a, b, c=1):
        return a * b * c


calc = Calculator()

print(calc.multiply(5, 2))
print(calc.multiply(5, 2, 3))

# 2. Shop – Calculate total using *args
# Question: Create a Shop class with a total() method that accepts multiple prices using *args.
# Question 2: Shop

class Shop:
    def total(self, *prices):
        return sum(prices)


shop = Shop()

print("Total:", shop.total(100, 200, 300))
print("Total:", shop.total(50, 75, 100, 125))

# 3. Shape – Method overriding
# Question: Create a Shape class with an area() method. Override it in Square and Circle classes
# Question 3: Method Overriding

import math


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


square = Square(5)
circle = Circle(7)

print("Square Area:", square.area())
print("Circle Area:", circle.area())

# 4. Employee – Inheritance using super()
# Question: Create an Employee class that inherits from Person. Use super() to initialize the parent class.
# Question 4: Inheritance and super()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_details(self):
        self.introduce()
        print("Salary:", self.salary)


emp = Employee("Ram", 25, 30000)

emp.show_details()


# 5. Vehicle – Multilevel inheritance
# Question: Create a multilevel inheritance structure: Vehicle → Car → ElectricCar.
# Question 5: Multilevel Inheritance

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


tesla = ElectricCar()

tesla.start()
tesla.drive()
tesla.charge()


# 6. Polymorphism – Square and Circle
# Question: Create a list containing Square and Circle objects. Iterate through the list and print their areas.
# Question 6: Polymorphism

import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


shapes = [
    Square(5),
    Circle(7),
    Square(4),
    Circle(3)
]


for shape in shapes:
    print("Area:", shape.area())
