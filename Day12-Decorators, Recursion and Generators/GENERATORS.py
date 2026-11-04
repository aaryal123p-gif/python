# A generator produces values one at a time when requested.
# It uses yield instead of return and pauses after each yield.
#
# Calling a generator function returns a generator object;
# it does not immediately produce all values.

def get_numbers():
    return [1, 2, 3]


def generate_numbers():
    yield 1
    yield 2
    yield 3


# print(get_numbers())       # [1, 2, 3]
# print(list(generate_numbers()))  # [1, 2, 3]


# Get one value at a time with next().
def number_generator():
    yield 1
    yield 2
    yield 3


# g = number_generator()
# print(next(g))  # 1
# print(next(g))  # 2
# print(next(g))  # 3
# print(next(g))  # StopIteration: no more values


# Most generators use a loop.
def count_up(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1


# for number in count_up(5):
#     print(number)


# Generate even numbers.
def evens(limit):
    for n in range(limit + 1):
        if n % 2 == 0:
            yield n


# print(list(evens(10)))  # [0, 2, 4, 6, 8, 10]


# An endless generator creates a value only when requested.
def token_numbers():
    n = 1
    while True:
        yield n
        n += 1


# tokens = token_numbers()
# print(next(tokens))  # 1
# print(next(tokens))  # 2
# print(next(tokens))  # 3


# Generator expressions:
# [] creates a list; () creates a generator expression.
squares_list = [n * n for n in range(5)]
squares_generator = (n * n for n in range(5))

# print(squares_list)                  # [0, 1, 4, 9, 16]
# print(list(squares_generator))       # [0, 1, 4, 9, 16]
# print(sum(n * n for n in range(5)))  # 30


# Generators can save memory because they produce values
# one at a time instead of storing the complete collection.
# A generator is normally consumed only once. After it is
# exhausted, create a new generator to start again.


