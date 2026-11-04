# "w" creates a file or overwrites existing content.

with open("notes.txt", "w") as f:
    f.write("Hello Nepal\n")
    f.write("Python is fun\n")

print("File saved successfully!")



# 8. WRITELINES() METHOD


# Writes multiple strings from a list.
# It does not automatically add newline characters.

fruits = ["apple\n", "mango\n", "banana\n"]

with open("fruits.txt", "w") as f:
    f.writelines(fruits)



# 9. READING A FILE - read()


# Reads the entire file.

with open("notes.txt", "r") as f:
    text = f.read()

print(text)



# 10. readline() METHOD


# Reads one line at a time.

with open("notes.txt", "r") as f:
    first = f.readline()
    second = f.readline()

print(first.strip())
print(second.strip())



# 11. readlines() METHOD

# Reads all lines and returns a list.

with open("notes.txt", "r") as f:
    lines = f.readlines()

print(lines)



# 12. READING USING FOR LOOP


with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())


# 13. APPEND MODE


# "a" adds new content without deleting old content.

with open("notes.txt", "a") as f:
    f.write("Learning Python\n")
    f.write("File handling is easy\n")



# 14. FILE HANDLING WITH TRY-EXCEPT


# Handles missing file errors.

try:
    with open("marks.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File not found. Check the name!")



# 15. DELETING A FILE


import os

if os.path.exists("fruits.txt"):
    os.remove("fruits.txt")
    print("File deleted successfully!")
else:
    print("File not found!")


# 16. SAVE AND READ STUDENT MARKS

students = {
    "Ram": 80,
    "Sita": 92,
    "Hari": 75
}

# Saving student marks

with open("marks.txt", "w") as f:
    for name, marks in students.items():
        f.write(f"{name},{marks}\n")


# Reading student marks

total = 0

with open("marks.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")

        print(name, "got", marks)

        total += int(marks)

print("Total:", total)



# 17. CONTACT BOOK - COMBINED EXAMPLE


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


contacts = [
    Contact("Ram", "9841000001"),
    Contact("Sita", "9851000002")
]

# Save contacts

with open("contacts.txt", "w") as f:
    for c in contacts:
        f.write(str(c) + "\n")


# Append another contact

with open("contacts.txt", "a") as f:
    f.write(str(Contact("Hari", "9861000003")) + "\n")


# Read contacts

with open("contacts.txt", "r") as f:
    for line in f:
        print(line.strip())