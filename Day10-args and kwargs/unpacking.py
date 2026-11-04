#Using * to unpack a list or tuple:
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

print(add(*numbers))  # 60

#Using ** to unpack a dictionary:
def profile(name, age, city):
    print(name, age, city)

person = {
    "name": "Ram",
    "age": 21,
    "city": "Pokhara"
}

profile(**person)


# Important Errors
#def add(a, b):
#    return a + b

#add(1, 2, 3)  # TypeError: add() takes 2 positional arguments but 3 were given

#Too many arguments.
#def profile(**info):
#    print(info)

#profile("Ram")  # TypeError

#**kwargs accepts keyword arguments, not ordinary positional values.
#def area(length, width):
#    return length * width

#area(*[1, 2, 3])  # TypeError