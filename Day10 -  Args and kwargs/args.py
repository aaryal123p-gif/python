def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(2, 3))          # 5
print(add(2, 3, 4))       # 9
print(add(10, 20, 30))    # 60
print(add())              # 0


#Important points:
#- *args collects values into a tuple.
#- You can use loops to access its values.
#- You can use sum(), max(), min() and len() directly.

def report(*marks):
    print("Count:", len(marks))
    print("Total:", sum(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

report(67, 45, 92, 78)


#. Normal Parameters with *args
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Namaste", "Ram", "Sita", "Hari")