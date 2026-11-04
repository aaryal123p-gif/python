#Sorting, reversing, counting
# scores = [88, 45, 72, 90, 60]

# scores.sort()                    # [45, 60, 72, 88, 90]
# scores.sort(reverse=True)        # highest first

# names = ["Maya", "abel", "Zoe"]
# names.sort(key=str.lower)        # ignore case when sorting

# scores.count(90)   # how many times 90 appears
# scores.index(72)   # position of the first 72

scores = [88, 45, 72, 90, 60]
print(scores)
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)

names = ["Maya", "abel", "Zoe"]
names.sort(key=str.lower)
print(names)

scores = [88, 45, 72, 90, 60]
print(scores.count(90))
print(scores.index(72))


#Looping through a list
#for visits every item, one at a time, in order.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


#Nested lists — a list inside a list
#A grid, table, or seating chart is just a list of lists.
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[0])        
print(grid[1][2])     
for row in grid:
    print(row)        


#Lists and strings — split() and join()
#Text turns into a list, and a list turns back into text.
line = "apple,banana,cherry"

fruits = line.split(",")
print(fruits)       

words = "hello world".split()   
print(words)        

joined = ", ".join(fruits)
print(joined) 


#Copying a list — the trap that gets everyone
#new_list = old_list doesn't make a copy — it makes a second name for the same list.

old_list = [1, 2, 3]
new_list = old_list  
new_list.append(4)
print(old_list) 
new_list = old_list[:] 
new_list.append(5)
print(new_list)


