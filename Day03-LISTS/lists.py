#Creating a list & reading items
# fruits = ["apple", "banana", "cherry"]

# print(fruits)        # ['apple', 'banana', 'cherry']
# print(fruits[0])     # "apple"   — first item
# print(fruits[-1])    # "cherry"  — last item
# print(len(fruits))   # 3

# empty = []           # a list can start empty to



#Slicing — grabbing a chunk
# nums = [10, 20, 30, 40, 50, 60]

# nums[1:4]     # [20, 30, 40]
# nums[:3]      # [10, 20, 30]  — from the start
# nums[3:]      # [40, 50, 60]  — to the end
# nums[::2]     # [10, 30, 50]  — every 2nd item
# nums[1:6:2]   # [20, 40, 60]  — start, stop, AND step together
# nums[::-1]    # [60, 50, 40, 30, 20, 10]  — reversed!

nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[::2])
print(nums[1:6:2])
print(nums[::-1])   


#Lists are mutable — change any item
fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"
print(fruits)    

fruits[0:2] = ["kiwi", "grape"]
print(fruits)    


#Adding & removing items
# cart = ["bread", "milk"]

# cart.append("eggs")          # ['bread', 'milk', 'eggs']
# cart.insert(0, "butter")     # add at the front
# cart.remove("milk")          # delete by value
# last = cart.pop()            # removes & returns last item
# cart.pop(0)                  # removes item at index 0
# cart.clear()                 # empty the whole list

cart=["bread", "milk"]
cart.append("eggs")
print(cart)
cart.insert(0, "butter")
print(cart)
cart.remove("milk")
print(cart)
cart.pop()
print(cart)
cart.pop(0)
print(cart)
cart.clear()
print(cart)



#Checking a list — built-ins & membership
# scores = [88, 45, 72, 90, 60]

# len(scores)     # 5     — how many items
# sum(scores)     # 355   — add them all up
# max(scores)     # 90    — highest value
# min(scores)     # 45    — lowest value

# "eggs" in cart      # True or False
# 90 in scores        # True — 90 is in the list
scores = [88, 45, 72, 90, 60]
print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))
print("eggs" in cart)
print(90 in scores)



