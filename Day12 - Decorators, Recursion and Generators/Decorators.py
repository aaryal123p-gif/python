 # A decorator is a function that wraps another function to add
# extra work before or after it runs.
#
# @my_decorator is a shortcut for:
# function_name = my_decorator(function_name)

def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@simple_decorator
def greet():
    print("Hello!")


# Calling greet() runs the wrapper and the original function.
# greet()


# Decorators that accept any function arguments:
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function is starting...")
        result = func(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


# print(add(10, 20))


# Example: decorator that doubles the returned result.
def double_result(func):
    def wrapper(n):
        return func(n) * 2
    return wrapper


@double_result
def add_ten(n):
    return n + 10


# print(add_ten(5))  # 30


# Important decorator points:
# - wrapper() contains the extra behavior.
# - *args and **kwargs allow different arguments.
# - return func(*args, **kwargs) keeps the original result.
# - return wrapper (without parentheses) returns the new function.
# - Common uses: logging, timing, and login checks.
