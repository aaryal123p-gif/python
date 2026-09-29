#A bag of unique items: no duplicates, no order.
#Creting a set
nums = {1, 2, 2, 3, 3, 3}
print(nums)            # {1, 2, 3}   duplicates gone
print(set([1, 1, 2]))  # {1, 2}   list to set
print(set("aab"))      # {'a', 'b'}  any order

empty = set()          # the right way
wrong = {}
print(type(wrong))     # <class 'dict'>   not a set!


#Set rules: no order, no index
colors = {"red", "blue", "green"}
print(colors)       # order may be different!

#print(colors[0])
# TypeError: 'set' object is not subscriptable

#ok  = {1, "hi", (2, 3)}    # numbers, strings, tuples
#bad = {1, [2, 3]}
# TypeError: unhashable type: 'list'


#Adding and removing items
colors.add("yellow")
print(colors)

colors.remove("blue")
print(colors)

colors.discard("green")
print(colors)


#Checking a set
#in, len, max, min, sum and sorted all work.
nums = {4, 9, 1, 7}

print(9 in nums)     
print(5 not in nums) 
print(len(nums))     
print(max(nums))     
print(min(nums))     
print(sum(nums))     
print(sorted(nums))  



#Set operations in code
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b)    # {1, 2, 3, 4, 5}   a.union(b)
print(a & b)    # {3, 4}            a.intersection(b)
print(a - b)    # {1, 2}            a.difference(b)
print(b - a)    # {5}
print(a ^ b)    # {1, 2, 5}         a.symmetric_difference()

a |= b          # a is changed now
print(a)        # {1, 2, 3, 4, 5}



#Comparing sets
small = {1, 2}
big   = {1, 2, 3, 4}

print(small <= big)            
print(small.issubset(big)) 
print(big >= small)          
print(big.issuperset(small))   

print({1, 2}.isdisjoint({5, 6}))   
print({1, 2} == {2, 1})      


#copy() and frozenset
a = {1, 2}
b = a            # same set, two names
c = a.copy()     # a real copy
a.add(3)
print(b)         
print(c) 
print(a is b)     
print(a is c)    

# f = frozenset([1, 2])
# f.add(3)         # AttributeError: can't change


# Best trick: remove duplicates
votes = ["tea", "coffee", "tea", "tea", "milk"]

unique = set(votes)
print(unique)           # {'tea', 'coffee', 'milk'}
print(len(unique))      # 3
print(sorted(unique))   # ['coffee', 'milk', 'tea']

print(len(votes) != len(unique))   # True: had duplicates


s = {3, 1, 3, 2, 1}
print(len(s))
s.add(4)
print(sorted(s))

print({1, 2} & {2, 3})
print({1, 2} | {2, 3})