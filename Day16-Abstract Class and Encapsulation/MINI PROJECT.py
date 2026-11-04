# 1. Create an abstract class Animal
# Question: Create an abstract class Animal with an abstract method sound(). Create a child class Dog that implements it.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()

# 2. Create an abstract class Shape
# Question: Create an abstract class with an area() method. Implement it in Rectangle.
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


r = Rectangle(10, 5)

print("Area:", r.area())

# 3. Implement multiple child classes
# Question: Create an abstract class Payment with an abstract method pay(). Create Esewa and Khalti child classes.
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class Esewa(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Esewa")


class Khalti(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Khalti")


e = Esewa()
k = Khalti()

e.pay(500)
k.pay(1000)

# 4. Demonstrate public, protected and private attributes
# Question: Create a class Student with public, protected and private attributes.
class Student:

    def __init__(self):
        self.name = "Ram"          # Public
        self._age = 20             # Protected
        self.__marks = 85          # Private


s = Student()

print(s.name)
print(s._age)
print(s._Student__marks)


# 5. Use getter and setter methods
# Question: Create a class Employee with a private salary. Use getter and setter methods to access and update it.
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")


e = Employee(30000)

print("Old Salary:", e.get_salary())

e.set_salary(40000)

print("New Salary:", e.get_salary())


# 6. Bank Account – Encapsulation
# Question: Create a BankAccount class with a private balance. Add deposit and withdraw methods.
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)

print("Balance:", account.get_balance())


# 7. Student marks validation
# Question: Create a class Student with private marks. Allow marks only between 0 and 100.
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated")
        else:
            print("Invalid marks")


s = Student(75)

print(s.get_marks())

s.set_marks(90)

print(s.get_marks())

s.set_marks(150)


