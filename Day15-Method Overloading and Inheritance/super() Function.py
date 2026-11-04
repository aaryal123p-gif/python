# 4. super() Function
# Meaning: super() allows a child class to access methods from its parent class.

# A. Using super().init()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school


s1 = Student("Ram", 20, "Skill Shikshya")

print(s1.name)
print(s1.age)
print(s1.school)

# B. Using super() with methods
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}")


t1 = Teacher("Shikhar", "Python")

t1.introduce()

# C. Overriding parent properties
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4

    def info(self):
        print(f"{self.brand} has {self.wheels} wheels")


class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.wheels = 2


car = Vehicle("Toyota")
bike = Bike("Honda")

car.info()
bike.info()
