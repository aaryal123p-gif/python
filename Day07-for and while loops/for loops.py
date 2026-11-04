# 1. FOR LOOP
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4


# 2. RANGE()
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(range(2, 11, 2)))    # [2, 4, 6, 8, 10]
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]



# 3. LOOP THROUGH A LIST
fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)

# 4. LOOP THROUGH A STRING
word = "Nepal"
for letter in word:
    print(letter)

# 5. LOOP THROUGH A DICTIONARY
prices = {"tea": 20, "coffee": 50, "momo": 150}
for item, price in prices.items():
    print(f"{item}: Rs. {price}")

# 6. ADD NUMBERS USING A LOOP
total = 0
for number in range(1, 6):
    total += number
print("Total:", total)  # 15

# 7. LOOP WITH IF / ELSE
marks = [45, 80, 32, 67, 25]
for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

# 8. WHILE LOOP
count = 1
while count <= 5:
    print(count)
    count += 1

# 9. BREAK - STOP THE LOOP
for number in range(1, 10):
    if number == 5:
        break
    print(number)

# 10. CONTINUE - SKIP ONE ROUND
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# 11. NESTED LOOP
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}")
