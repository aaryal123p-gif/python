# Project 01 · Tuples
# Student ID card
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

person = (name, age, city)

name, age, city = person

# Print ID card
print("\n========================")
print("       ID CARD")
print("========================")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
print("========================")

marks = (85, 92, 78)

print("\n===== MARKS =====")
print("Marks:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Total marks:", sum(marks))


person_list = list(person)

new_city = input("\nEnter your new city: ")
person_list[2] = new_city

person = tuple(person_list)

print("\n===== UPDATED ID CARD =====")
name, age, city = person

print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
print("===========================")


# Project 02 · Sets
# Party guest lis

# Get guest lists from two friends
friend1_input = input("Friend 1 guest list (names separated by commas): ")
friend2_input = input("Friend 2 guest list (names separated by commas): ")

# Convert inputs into sets
friend1 = set(friend1_input.split(","))
friend2 = set(friend2_input.split(","))

# Guests on both lists
common_guests = friend1.intersection(friend2)

# All guests from both lists
all_guests = friend1.union(friend2)

# Print results
print("\n===== GUEST LIST RESULTS =====")

print("Guests on both lists:", common_guests)
print("All guests:", all_guests)
print("Total number of guests:", len(all_guests))

# Add a new guest
new_guest = input("\nEnter a new guest to add: ")
all_guests.add(new_guest)

print("\nAfter adding a guest:")
print(all_guests)
print("Total guests:", len(all_guests))

# Remove a guest safely
remove_guest = input("\nEnter a guest to remove: ")
all_guests.discard(remove_guest)

print("\nAfter removing a guest:")
print(all_guests)
print("Final number of guests:", len(all_guests))


# Project 03 · Capstone
# Common words finder

# Ask for two sentences
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

# Split sentences into sets of words
words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

# Find common words
common_words = words1.intersection(words2)

# Find all unique words from both sentences
all_words = words1.union(words2)

# Count common and unique words
common_count = len(common_words)
unique_count = len(all_words)

# Store counts in a tuple
counts = (common_count, unique_count)

# Unpack the tuple
common, unique = counts

# Print results
print("\n===== WORD ANALYSIS =====")

print("Common words:", common_words)
print("All unique words:", all_words)

print("\n===== WORD COUNTS =====")
print("Common words count:", common)
print("Total unique words count:", unique)

print("========================")
