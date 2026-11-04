def profile(**info):
    print(info)
    print(type(info))

profile(name="Ram", age=21, city="Pokhara")

#Important points:
#- **kwargs collects values into a dictionary.
#- Keys are argument names.
#- Values are the values assigned to those names.
#- You can loop through them using .items().


def profile(**info):
    for key, value in info.items():
        print(key, ":", value)

profile(name="Sita", age=22, city="Kathmandu")


# Normal Parameters with **kwargs
def student(name, **marks):
    print("Student:", name)

    for subject, mark in marks.items():
        print(subject, ":", mark)

student("Gita", math=88, science=76, english=91)


# Using Both Together
def demo(a, *args, **kwargs):
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

demo(1, 2, 3, x=10, y=20)