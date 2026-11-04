#  VOWEL COUNTER
def count_vowels(text):
    count = 0

    for letter in text.lower():
        if letter in "aeiou":
            count += 1

    return count

print("Vowels:", count_vowels("I love Nepal"))
