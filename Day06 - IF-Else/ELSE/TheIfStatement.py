# #if statement
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")  
# print("Thank you for using the voting eligibility checker.")


# num = int(input("enter a number: "))
# if num >100:
#     print("the number is greater than 100")
# print("success")

# num = float(input("enter a number: "))
# if num >100:
#     print("the number is greater than 100")
# print("success")


# #IF / ELSE statement
# age = int(input("enter your age:"))
# if age >=18:
#     print("you are eligibe for vote")
#     print("please proceed to the voting booth")
# else:
#     print("you are not eligible for vote")
#     print("please wait until you are 18 years old")
# print("thank you for using the voting eligibility checker")


# #if / elif / else statement
# marks = float(input("enter your marks:"))
# if marks >=90:
#     print("grade A")
# elif marks>=80:
#     print("grade B")
# elif marks>=70:
#     print("grade C")
# elif marks>=60:
#     print("grade D")
# else:
#     print("grade F (bring your parents to school)")
# print("thank you for using the grading system")



# temp = 18
# if temp > 30:
#     print("it's a hot day")
# elif temp > 20:
#     print("it's a nice day")
# elif temp > 10:
#     print("it's a bit cold")
# else:
#     print("it's cold")
# print("thank you for using the weather checker")



# Logic (AND, OR, NOT)
# age = int(input("Enter your age: "))
# has_id = True
# if age>= 18 and has_id:
#     print("You are eligible to vote.")
# elif age >=18 and has_id == False:
#     print("You are not eligible to vote. Please bring your ID.")
# elif age < 18 and has_id:
#     print("You are not eligible to vote. You must be at least 18 years old.")
# else:
#     print("You are not eligible to vote. You must be at least 18 years old and bring your ID.")
# print("Thank you for using the voting eligibility checker.")


# cart=["apple", "banana", "orange"]
# if "apple" in cart:
#     print("Apple is in the cart.")
# else:
#     print("Apple is not in the cart.")
# print()


# prices={"apple": 1.5, "banana": 0.8, "orange": 2.0}
# item = "banana"
# if item in prices:  
#     print(f"The price of {item} is ${prices[item]}.")       
# else:
#     print(f"{item} is not available in the store.")
# print()

# anser = input("Do you want to continue? (yes/no): ")
# if anser.lower() == "yes":
#     print("You chose to continue.") 
# else:
#     print("You chose not to continue.")
# print("Thank you for using the program.")


# #if inside if
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin":
#     if password == "password123":
#         print("Login successful. Welcome, admin!")
#     else:
#         print("Incorrect password. Access denied.")
# else:
#     print("Invalid username. Access denied.")
# print("Thank you for using the login system.")

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# role = input("Enter your role (admin/user): ")
# if username == "admin" and role == "admin":
#     if password == "password123":
#         print("Login successful. Welcome, admin!")
#         if role == "admin":
#             print("You have administrative privileges.")
#         elif role == "user":
#             print("You have user privileges.")
#         else:
#             print("Invalid role. Access denied.")
#     else:
#         print("Incorrect password. Access denied.")
# else:
#     print("Invalid username or role. Access denied.")
# print("Thank you for using the login system.")


num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 1. If num is more than 100, print "Big number"
if num > 100:
    print("Big number")

# 2. If num is from 1 to 10, print "Small number"
if num >= 1 and num <= 10:
    print("Small number")
