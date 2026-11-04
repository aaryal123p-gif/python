# Recursion happens when a function calls itself.
# Every recursive function needs:
# 1) A BASE CASE: the condition that stops the recursion.
# 2) A SMALLER STEP: each call moves closer to the base case.

def countdown(n):
    if n == 0:              # base case
        print("Go!")
        return
    print(n)
    countdown(n - 1)        # smaller step


# countdown(3)


# Factorial:
# 4! = 4 * 3 * 2 * 1 = 24

def factorial(n):
    if n <= 1:              # base case
        return 1
    return n * factorial(n - 1)


# print(factorial(5))  # 120


# Add numbers from 1 to n.
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)


# print(total(5))  # 15


# Reverse a word using recursion.
def reverse_word(word):
    if word == "":
        return ""
    return reverse_word(word[1:]) + word[0]


# print(reverse_word("momo"))  # "omom"


# Add all values in a list using recursion.
def list_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + list_sum(numbers[1:])


# print(list_sum([4, 5, 6]))  # 15


# Sum the digits of a number.
# % 10 gets the last digit; // 10 removes the last digit.
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


# print(sum_digits(4567))  # 22


# Fibonacci sequence using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# print([fibonacci(i) for i in range(8)])
# [0, 1, 1, 2, 3, 5, 8, 13]


# Recursion warning:
# If there is no base case, or the function never reaches it,
# Python raises RecursionError. The lesson notes a limit of
# about 1000 nested calls (the exact limit can vary).
#
# Loop vs recursion:
# - Loop: repeats with for/while and stops when its condition fails.
# - Recursion: repeats by calling itself and stops at the base case.
# - Use loops for simple counting and list traversal.
# - Recursion can help when a problem contains a smaller version
#   of itself.