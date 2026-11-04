# A. Single inheritance
# One child inherits from one parent.
class Father:
    def house(self):
        print("I have a house")


class Son(Father):
    def bike(self):
        print("I have a bike")


s = Son()

s.house()
s.bike()

# B. Multilevel inheritance
# A class inherits from a child class, forming a chain.
class Grandfather:
    def land(self):
        print("Land from grandfather")


class Father(Grandfather):
    def house(self):
        print("House from father")


class Son(Father):
    def bike(self):
        print("My own bike")


s = Son()

s.land()
s.house()
s.bike()

# C. Hierarchical inheritance
# Multiple child classes inherit from one parent.
class Person:
    def breathe(self):
        print("Breathing")


class Student(Person):
    def study(self):
        print("Studying")


class Teacher(Person):
    def teach(self):
        print("Teaching")


s = Student()
t = Teacher()

s.breathe()
s.study()

t.breathe()
t.teach()

# D. Multiple inheritance
# One child inherits from multiple parent classes.
class Father:
    def height(self):
        print("Tall like father")


class Mother:
    def eyes(self):
        print("Brown eyes like mother")


class Child(Father, Mother):
    pass


c = Child()

c.height()
c.eyes()


# E. Hybrid inheritance
# Combination of two or more types of inheritance.
class Person:
    def breathe(self):
        print("Breathing")


class Student(Person):
    def study(self):
        print("Studying")


class Worker(Person):
    def work(self):
        print("Working")


class Intern(Student, Worker):
    pass


i = Intern()

i.breathe()
i.study()
i.work()


# 6. Important practical example – Bank Account
# This combines inheritance, constructors, super(), and methods.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Added Rs. {amount}")

    def show(self):
        print(f"{self.owner}: Rs. {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=5):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate / 100
        self.deposit(interest)


acc = SavingsAccount("Ram", 1000)

acc.deposit(500)
acc.add_interest()
acc.show()