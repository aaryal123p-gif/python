#String methods — built-in superpowers
# word = "python"

# word.upper()     # "PYTHON"
# word.lower()     # "python"
# word.title()     # "Python"
# len(word)        # 6

name = input("Name: ").strip()
# .strip() removes accidental spaces


# #Checking & replacing text
sentence = "Hello World"
sentence.startswith("Hello")   # True
sentence.endswith("World")     # True
print(sentence.replace("World", "Python"))

# # "Hello Python"
# "hello" in sentence   # False — case-sensitive
# "Hello" in sentence   # True


#Indexing & slicing
word = "Python"
print(word[0])  # "P"
print(word[1])      # "y"
print(word[-1])     # "n"  — last character
print(word[-2])     # "o"  — second to last

# Slicing — grab a chunk
print(word[0:3])    # "Pyt"   (stops before index 3)
print(word[2:5])    # "tho"   (from index 2 to 4)
print(word[2:5])     # "thon"  (2 to the end)

#type() — what kind of data is this?
print(type("Hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>

age = input("Age: ")
print(type(age))       # <class 'str'> — always!