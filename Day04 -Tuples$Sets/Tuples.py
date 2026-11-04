#Creating a tuple
fruits = ("apple", "banana", "cherry")
info   = ("Ram", 20, True)     
empty  = ()                     

nums = 1, 2, 3                   
print(nums)                      

one = ("apple",)                
not_tuple = ("apple")            

print(tuple([1, 2]))            
print(type(fruits)) 


#Indexing and slicing
days = ("Sun", "Mon", "Tue", "Wed", "Thu")

print(days[0])     
print(days[-1])   
print(len(days))   

print(days[1:3])   
print(days[:2])     
print(days[::-1])   

#print(days[10])     # IndexError!


#You can't change a tuple
#No editing, no append, no remove. But there's a trick.
fruits = ("apple", "banana")

#fruits[0] = "kiwi"        # TypeError! can't change

temp = list(fruits)       # 1. make it a list
temp[0] = "kiwi"          # 2. change it
fruits = tuple(temp)      # 3. make it a tuple again
print(fruits)             # ('kiwi', 'banana')

print(fruits + ("mango",))   # ('kiwi', 'banana', 'mango')
print(("hi",) * 3)           # ('hi', 'hi', 'hi')
del fruits                   # delete the whole tuple

#Tuple methods and functions
marks = (70, 90, 80, 90)

print(marks.count(90))   
print(marks.index(80))   

print(len(marks))        
print(max(marks))        
print(min(marks))        
print(sum(marks))        
print(sorted(marks))     
print(90 in marks)       
print((1, 2) == (2, 1))  


#Packing and unpacking
person = ("Ram", 20, "Pokhara")   # packing

name, age, city = person           # unpacking
print(name)      
print(age)     

a, b = 1, 2
a, b = b, a      # swap values
print(a, b)     

first, *rest = (1, 2, 3, 4)
print(rest)      


#A tuple inside a tuple
student = ("Ram", (2008, 5, 14), ["Math"])
print(student[0])
print(student[1]) 
print(student[1][1])   
print(student[2])
print(student[1][0])
student[2].append("Science")
print(student)

t = (5, 10, 15, 20)

print(t[1])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.index(15))

a, b, c, d = t
print(c)

#t[0] = 1  # TypeError! Tuples are immutable


