#Numbers and Strings
#f-strings — mixing text and numbers
name = "Maya"
age = 15

print(f"{name} is {age} years old")
price = 250
print(f"Total: Rs. {price * 2}")


#Python as a calculator
10 + 3    # 13    add
10 - 3    # 7     subtract
10 * 3    # 30    multiply
10 / 3    # 3.33  divide (always float)
10 // 3   # 3     floor divide
10 % 3    # 1     remainder
2 ** 8    # 256   power


#A real Example
price = 250
quantity = 4
discount = 50
total = price * quantity - discount
print(f"Total: Rs. {total}")  


#Fix it with int() and float()
# The problem
# age = input("Enter your age: ")
# print(age + 10)     # TypeError

# The fix — wrap with int()
age = int(input("Enter your age: "))
print(age + 10)     # 25 — correct!25

# # Decimals need float()
price = float(input("Price: "))
print(price * 1.13)  # price with tax


#Shorthand operators
# Long way
# score = score + 10
# score = score - 5
# score = score * 2

#Short way — same result
# score += 10   # add 10
# score -= 5    # subtract 5
# score *= 2    # multiply by 2

# Real example — running total
total = 0
total += 120   # total = 120
total += 350   # total = 470
print(f"Total: Rs. {total}")

