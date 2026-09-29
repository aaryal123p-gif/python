#How dictionary looks 
#Three pairs. Each pair is a key, a colon, and a value.
#student = {"name": "Ram", "age": 20, "city": "Pokhara"}
#Key "name" = "Ram
# Key "age" = 20
# Key "city" = "Pokhara"

#Creating a dictionary
student = {"name": "Ram", "age": 20}
empty = {}                    
print(type(empty))             

d1 = dict(name="Sita", age=19)
print(d1)                     

d2 = dict([("a", 1), ("b", 2)])
print(d2)                      

print(len(student))  

#Rules for keys
#Keys must be unique, immutable, and hashable.
d = {"a": 1, "b": 2, "a": 99}
print(d)             # {'a': 99, 'b': 2}   last one wins

ok = {1: "one", "two": 2, (3, 4): "tuple key"}

#bad = {[1, 2]: "list key"}
# TypeError: unhashable type: 'list'

info = {"marks": [70, 80], "pass": True}   # any value

print({"a": 1, "b": 2} == {"b": 2, "a": 1})   # True

#Reading a value
student = {"name": "Ram", "age": 20}
print(student["name"])         
#print(student["phone"])         # KeyError: 'phone'
print(student.get("name"))    
print(student.get("phone"))     # None   no error
print(student.get("phone", "N/A"))   # N/A   default

#print(student[0])               # KeyError: 0


#Adding and changing
student = {"name": "Ram"}

student["age"] = 20          # new key: added
student["name"] = "Hari"     # old key: changed
print(student)               

student.update({"city": "Pokhara", "age": 21})
print(student)


#Removing items
s = {"name": "Ram", "age": 20, "city": "Pokhara", "grade": "A"}

age = s.pop("age")       # remove, and get the value
print(age)               # 20
print(s.pop("phone", "not found"))   # not found

last = s.popitem()       # remove the last pair
print(last)              # ('grade', 'A')

del s["city"]            # delete one key
print(s)                 # {'name': 'Ram'}
s.clear()                # empty it: {}
del s                    # delete the whole dictionary


d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10
print(d)                
print(len(d))
print(d.get("z", 0))
print(d.pop("b"))
print(d)

#print(d["z"])  # key error



