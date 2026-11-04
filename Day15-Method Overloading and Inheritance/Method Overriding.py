# 3. Method Overriding
# Meaning: When a child class creates a method with the same name as the parent class, the child's method is used.
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


class Fish(Animal):
    pass


Dog().sound()     # Woof!
Cat().sound()     # Meow!
Fish().sound()    # Some sound


# Polymorphism example
# Same method call, different outputs.
animals = [Dog(), Cat(), Fish()]

for a in animals:
    a.sound()