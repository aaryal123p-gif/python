# QUESTION 1 — __init__, object attributes, and changing data
# Topic:
# - Creating objects using __init__
# - Giving each object its own attributes
# - Changing an attribute of only one object
# - Adding numeric attributes
#
# TASK: Guess the output of all three print() statements.
#
# Expected output:
# Write your answer here:
# 1.
# 2.
# 3.


# def question_1():
#     class Mobile:
#         def __init__(self, brand, price):
#             self.brand = brand
#             self.price = price
#             self.battery = 100

#     m1 = Mobile("Samsung", 30000)
#     m2 = Mobile("Redmi", 18000)

#     m1.battery = 40

#     print(m1.brand, m1.battery)
#     print(m2.brand, m2.battery)
#     print(m1.price + m2.price)


# ANSWER 1 
# Explanation:
# Every Mobile object starts with battery = 100.
# Only m1.battery is changed to 40. The battery of m2 remains 100.
# The two prices are added: 30000 + 18000 = 48000.
#
# Correct output:
# Samsung 40
# Redmi 100
# 48000


def answer_1():
    class Mobile:
        def __init__(self, brand, price):
            self.brand = brand
            self.price = price
            self.battery = 100

    m1 = Mobile("Samsung", 30000)
    m2 = Mobile("Redmi", 18000)

    m1.battery = 40

    print(m1.brand, m1.battery)       # Samsung 40
    print(m2.brand, m2.battery)       # Redmi 100
    print(m1.price + m2.price)        # 48000
answer_1()



# QUESTION 2 — Methods, lists, and separate objects
# Topic:
# - Methods inside a class
# - Using self
# - Adding items to a list with append()
# - Counting list items with len()
# - Each object gets its own list
#
# TASK: Guess the output of all three print() statements.
#
# Expected output:
# Write your answer here:
# 1.
# 2.
# 3.


# def question_2():
#     class Cart:
#         def __init__(self, owner):
#             self.owner = owner
#             self.items = []

#         def add(self, item):
#             self.items.append(item)

#         def count(self):
#             return len(self.items)

#     c1 = Cart("Ram")
#     c2 = Cart("Sita")

#     c1.add("momo")
#     c1.add("tea")
#     c2.add("chowmein")

#     print(c1.count())
#     print(c2.items)
#     print(f"{c1.owner} has {c1.count()} items")


# ANSWER 2 
# Explanation:
# c1 receives two items: momo and tea, so c1.count() is 2.
# c2 receives only chowmein, so c2.items contains ['chowmein'].
# Each Cart object creates its own empty list in __init__.
#
# Correct output:
# 2
# ['chowmein']
# Ram has 2 items


def answer_2():
    class Cart:
        def __init__(self, owner):
            self.owner = owner
            self.items = []

        def add(self, item):
            self.items.append(item)

        def count(self):
            return len(self.items)

    c1 = Cart("Ram")
    c2 = Cart("Sita")

    c1.add("momo")
    c1.add("tea")
    c2.add("chowmein")

    print(c1.count())                         # 2
    print(c2.items)                           # ['chowmein']
    print(f"{c1.owner} has {c1.count()} items")  # Ram has 2 items
answer_2()


# BONUS QUESTION 3 — Student marks and average

# Topic:
# - A class with a list attribute
# - A method that changes the list
# - A method that returns a value
# - One method calling another method using self
#
# TASK: Guess what is printed by s1.report().


# def question_3():
#     class Student:
#         def __init__(self, name):
#             self.name = name
#             self.marks = []

#         def add_mark(self, mark):
#             self.marks.append(mark)

#         def average(self):
#             return sum(self.marks) / len(self.marks)

#         def report(self):
#             avg = self.average()
#             if avg >= 40:
#                 print(f"{self.name}: {avg} Pass")
#             else:
#                 print(f"{self.name}: {avg} Fail")

#     s1 = Student("Ram")
#     s1.add_mark(80)
#     s1.add_mark(70)
#     s1.report()


# ANSWER 3 
# Explanation:
# The average is (80 + 70) / 2 = 75.0.
# Since 75.0 is greater than or equal to 40, the result is Pass.
#
# Correct output:
# Ram: 75.0 Pass


def answer_3():
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
    s1.report()  # Ram: 75.0 Pass
answer_3()


# HOW TO RUN
# To practise a question, remove the # from ONE call below.
# Example: question_1()
#
# To see its solution, run the matching answer function.
# Example: answer_1()
#
# Run one at a time so the output is easy to understand.


if __name__ == "__main__":
    # Uncomment ONE line to practise:
    # question_1()
    # question_2()
    # question_3()

    # Uncomment ONE line to see an answer:
    # answer_1()
    # answer_2()
    # answer_3()
    pass
