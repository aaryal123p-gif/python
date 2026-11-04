#keys(), values() and items()
prices = {"tea": 20, "coffee": 50, "milk": 30}

print(prices.keys())
# dict_keys(['tea', 'coffee', 'milk'])
print(prices.values())
# dict_values([20, 50, 30])
print(prices.items())
# dict_items([('tea', 20), ('coffee', 50), ('milk', 30)])

print(list(prices))            # ['tea', 'coffee', 'milk']
print(list(prices.values()))   # [20, 50, 30]



#Checking a dictionary
prices = {"tea": 20, "coffee": 50, "milk": 30}

print("tea" in prices)           # True   it's a key
print(20 in prices)              # False  20 is a value
print(20 in prices.values())     # True

print(len(prices))               # 3
print(sum(prices.values()))      # 100
print(max(prices.values()))      # 50
print(sorted(prices))            # ['coffee', 'milk', 'tea']
print(max(prices, key=prices.get))   # coffee


#Joining two dictionaries
a = {"tea": 20, "milk": 30}
b = {"milk": 35, "juice": 60}

print(a | b)
# {'tea': 20, 'milk': 35, 'juice': 60}   milk from b

print({**a, **b})      # same result, older way

a |= b                 # change a (same as a.update(b))
print(a)


#setdefault() and fromkeys()
c = {"name": "Ram"}

print(c.setdefault("age", 18))      # 18    missing: added
print(c.setdefault("name", "Hari")) # Ram   already there
print(c)          # {'name': 'Ram', 'age': 18}

marks = dict.fromkeys(["math", "science", "english"], 0)
print(marks)
# {'math': 0, 'science': 0, 'english': 0}

print(dict.fromkeys(["a", "b"]))    # {'a': None, 'b': None}


#zip() and converting
names = ["Ram", "Sita", "Hari"]
marks = [85, 92, 78]

result = dict(zip(names, marks))
print(result)    # {'Ram': 85, 'Sita': 92, 'Hari': 78}

print(list(result.items()))
# [('Ram', 85), ('Sita', 92), ('Hari', 78)]
print(tuple(result))   



# The copy trap
a = {"x": 1}
b = a            # same dictionary, two names
c = a.copy()     # a real copy
d = dict(a)      # also a real copy

a["y"] = 2
print(b)         # {'x': 1, 'y': 2}   changed too!
print(c)         # {'x': 1}           safe
print(d)         # {'x': 1}           safe



#A dictionary inside a dictionary
school = {
    "ram":  {"age": 20, "city": "Pokhara"},
    "sita": {"age": 19, "city": "Kathmandu"}
}

print(school["sita"])           # {'age': 19, 'city': 'Kathmandu'}
print(school["sita"]["city"])   # Kathmandu

school["ram"]["age"] = 21       # change inside
school["hari"] = {"age": 22, "city": "Butwal"}   # add one
print(len(school)) 



# Lists and dictionaries together
student = {"name": "Ram", "marks": [70, 85, 90]}

print(student["marks"])        # [70, 85, 90]
print(student["marks"][0])     # 70
student["marks"].append(95)
print(sum(student["marks"]))   # 340
print(max(student["marks"]))   # 95

people = [{"name": "Ram"}, {"name": "Sita"}]
print(people[1]["name"])       # Sita


## More dictionary examples
p = {"pen": 10, "book": 50}
q = {"book": 60, "bag": 500}

print("pen" in p)
print(50 in p)
print(list(p.keys()))
print(p | q)
print(sum(q.values()))

r = p
r["pen"] = 15
print(p["pen"])

#print(p.items()[0])   # TypeError: 'dict_items' object is not subscriptable


