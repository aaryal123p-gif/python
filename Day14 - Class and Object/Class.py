#Why Classes?
#When data and actions belong together.

#Storing many students
# Student 1
from symtable import Class

from sympy import Add


name1 = "Ram"
age1 = 20
marks1 = 85

# Student 2
name2 = "Sita"
age2 = 21
marks2 = 92

# 50 students = 150 variables!

#One class, many objects
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
class1 = Student("Ram", 20, 85)
class2 = Student("Sita", 21, 92)
class1.display()
class2.display()


#Your First Class
#Write the blueprint, then make objects from it.

#The smallest class
#An empty blueprint. It still works!

#class starts a class, like def starts a function. pass means "nothing here yet".

#Student() with brackets builds a new object. __main__ just means "made in this file".
class Student:
    pass              # empty for now

s1 = Student()        # make an object
s2 = Student()        # make another object

print(type(s1))       # <class '__main__.Student'>

#Add data — Give the object some data
s1.name = "Ram"
s1.age = 20
s1.marks = 85

s2.name = "Sita"
s2.age = 21
s2.marks = 92

print("Student 1:")
print("Name:", s1.name)
print("Age:", s1.age)
print("Marks:", s1.marks)

print("Student 2:")
print("Name:", s2.name)
print("Age:", s2.age)
print("Marks:", s2.marks)

#The problem — Too much typing
# SUBTITLE: Easy to forget one line.
# COPY: We have to set every attribute by hand, for every object. Forget one, and Python gives an AttributeError.Better idea: give the values while making the object, like Student("Hari", 19). For that, we need __init__.
# CODE EXAMPLE 8
#s3 = Student()
#s3.name = "Hari"
# oops, forgot s3.age!

#print(s3.age)
# AttributeError: 'Student' object has no attribute 'age'


##__init__ and self
#Fill in each object's data the moment it is made.
# CODE EXAMPLE 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

print(s1.name, s1.age)     # Ram 20
print(s2.name, s2.age)     # Sita 21


#self — What is self?
#self means "this object". Think of the word "my".

#self is just a name. You could use another word, but everyone uses self, so you should too.
# CODE EXAMPLE 10
class Student:
    def __init__(self, name, age):
        self.name = name     # 3. save "Ram"
        self.age = age       # 4. save 20

s1 = Student("Ram", 20)

print(s1.name)    # Ram
print(s1.age)     # 20

#Starting values and changing data
class Student:
    def __init__(self, name, age):
        self.name = name     # from the input
        self.age = age       # from the input
        self.marks = 0       # same start for everyone

s1 = Student("Ram", 20)
print(s1.marks)     # 0

s1.marks = 85       # change it
print(s1.marks)     # 85


#Each object has its own data
s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

s1.age = 25         # change only s1

print(s1.age)       # 25
print(s2.age)       # 21   (no change)

#Methods
#Functions that live inside a class. They are the object's actions.
# Your first method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}")

s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

s1.greet()      # Hi, I am Ram
s2.greet()      # Hi, I am Sita

# Methods with inputs: a bank account
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Added Rs. {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - amount
            print(f"Took Rs. {amount}")

acc = BankAccount("Ram")
acc.deposit(1000)      # Added Rs. 1000
acc.withdraw(300)      # Took Rs. 300
acc.withdraw(5000)     # Not enough money!
print(acc.balance)     # 700


# A method that returns a value
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def is_square(self):
        return self.length == self.width

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

print(r1.area())         # 15
print(r2.area())         # 16
print(r1.is_square())    # False
print(r2.is_square())    # True


# Put It Together
# Student report card
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks)

    def report(self):
        avg = self.average()
        if avg >= 40:
            print(f"{self.name}: {avg} Pass")
        else:
            print(f"{self.name}: {avg} Fail")

s1 = Student("Ram")
s1.add_mark(80)
s1.add_mark(70)
s1.report()       # Ram: 75.0 Pass

