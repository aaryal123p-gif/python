# Count vowels in a sentence
text = input("Type a sentence: ").lower()
vowels = 0

for letter in text:
    if letter in "aeiou":
        vowels += 1

print("Vowels:", vowels)