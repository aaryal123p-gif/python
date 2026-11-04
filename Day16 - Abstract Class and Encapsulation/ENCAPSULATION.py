# Definition:
# Encapsulation means keeping data inside a class
# and controlling access through methods.
#
# It helps protect data from unwanted changes.
# Example:
# Bank account balance should not be changed
# directly without checking the amount.

# THREE TYPES OF ACCESS MODIFIERS

# A. PUBLIC
# No underscore (_)
# Accessible from outside the class.

class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Ram")

print(s1.name)       # Ram
s1.name = "Hari"
print(s1.name)       # Hari


# B. PROTECTED
# One underscore (_)
# Conventionally used inside class and child classes.
# Python does not strictly prevent outside access.

class Employee:

    def __init__(self, salary):
        self._salary = salary


emp = Employee(30000)

print(emp._salary)   # 30000
# It works, but accessing it outside is discouraged.


# C. PRIVATE
# Two underscores (__)
# Hidden from normal direct access outside the class.
# Python uses name mangling.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def show(self):
        print(self.__balance)


acc = BankAccount(1000)

acc.show()           # 1000

# print(acc.__balance)
# AttributeError

#  GETTER AND SETTER METHODS
# Getter:
# Used to retrieve private data.
#
# Setter:
# Used to update private data after validation.

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Added Rs. {amount}")

        else:
            print("Amount must be more than 0")


acc = BankAccount("Ram", 1000)

acc.deposit(500)
acc.deposit(-200)

print(acc.get_balance())


#  VALIDATION USING SETTER
class Student:

    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if marks >= 0 and marks <= 100:
            self.__marks = marks

        else:
            print("Marks must be between 0 and 100")


s1 = Student("Sita")

s1.set_marks(85)
s1.set_marks(500)

print(s1.get_marks())