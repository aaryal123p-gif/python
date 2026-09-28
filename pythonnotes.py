#Numbers in Python
#int and float — how Python does math.


"""
PYTHON NOTES: input() and numbers

1. input() ALWAYS gives you text (string).

   age = input("Enter your age: ")

   Even if the user enters 15,
   Python stores it as "15", not 15.

2. This causes an error:

   age + 10

   Because Python cannot add a string and an integer.

3. This works, but joins the text:

   age + "10"

   "15" + "10" = "1510"

4. FIX:
   Convert the input to an integer using int():

   age = int(input("Enter your age: "))
"""

age = int(input("Enter your age: "))
print(age + 10)


#What is a string?
#Any text between quote marks.
#Strings hold names, messages, addresses — anything you'd read as words rather than do math on.