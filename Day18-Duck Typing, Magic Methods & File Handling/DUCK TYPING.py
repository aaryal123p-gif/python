# 1. DUCK TYPING

# Python checks what an object can do,
# not what type of object it is.

class Duck:
    def quack(self):
        print("Quack quack!")


class Person:
    def quack(self):
        print("I am saying quack!")


class Toy:
    def quack(self):
        print("Squeak quack!")


def make_it_quack(thing):
    thing.quack()


make_it_quack(Duck())
make_it_quack(Person())
make_it_quack(Toy())


# Duck typing with error handling

class Stone:
    def roll(self):
        print("Stone rolls")


def make_it_quack_safe(thing):
    try:
        thing.quack()
    except AttributeError:
        print("This thing cannot quack")


make_it_quack_safe(Duck())
make_it_quack_safe(Stone())

