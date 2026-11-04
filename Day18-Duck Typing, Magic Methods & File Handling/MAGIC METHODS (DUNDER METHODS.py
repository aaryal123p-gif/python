# 2. MAGIC METHODS (DUNDER METHODS)
# Magic methods start and end with double
# underscores. Python calls them automatically.


# __init__() METHOD

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Ram", 80)

print(s1.name)
print(s1.marks)



# __str__() METHOD


# Used to represent an object as a string.
# Called automatically by print() and str().

class StudentInfo:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} - {self.marks} marks"


s1 = StudentInfo("Ram", 80)
s2 = StudentInfo("Sita", 92)

print(s1)
print(s2)



#  __len__() METHOD


# Makes len() work with our own objects.

class Basket:
    def __init__(self, fruits):
        self.fruits = fruits

    def __len__(self):
        return len(self.fruits)


b = Basket(["apple", "mango", "banana"])

print(len(b))



# __add__() METHOD


# Makes + operator work with objects.

class Wallet:
    def __init__(self, money):
        self.money = money

    def __add__(self, other):
        return Wallet(self.money + other.money)

    def __str__(self):
        return f"Rs. {self.money}"


w1 = Wallet(500)
w2 = Wallet(300)

w3 = w1 + w2

print(w3)



#  __eq__() AND __lt__() METHODS

# __eq__ = ==
# __lt__ = <

class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks


ram = StudentMarks("Ram", 80)
sita = StudentMarks("Sita", 92)
hari = StudentMarks("Hari", 80)

print(ram == hari)
print(ram == sita)
print(ram < sita)
print(sita < ram)

