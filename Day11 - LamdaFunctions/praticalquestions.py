# 1. Create a lambda function to find the square of a number.
square = lambda x: x * x
print(square(5))


# 2. Create a lambda function to add two numbers.
add = lambda a, b: a + b
print(add(10, 20))


# 3. Check whether a number is even or odd using lambda.
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(7))


# 4. Find the largest number in a list using max().
numbers = [10, 25, 5, 40, 15]
largest = max(numbers)
print(largest)


# 5. Find the smallest number in a list using min().
smallest = min(numbers)
print(smallest)


# 6. Sort a list of numbers using sorted().
numbers = [5, 2, 9, 1, 7]
result = sorted(numbers)
print(result)


# 7. Sort student records according to marks using lambda.
students = [
    ("Ram", 85),
    ("Shyam", 70),
    ("Hari", 95),
    ("Sita", 80)
]
result = sorted(students, key=lambda x: x[1])
print(result)


# 8. Use map() to multiply every number by 3.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 3, numbers))
print(result)


# 9. Use filter() to get only odd numbers.
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)


# 10. Combine map() and filter() in one program.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(map(lambda x: x * 3, filter(lambda x: x % 2 != 0, numbers)))
print(result)
