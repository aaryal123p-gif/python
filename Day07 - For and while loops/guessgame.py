# Number guessing game
secret = 7
tries = 0

while True:
    guess = int(input("Guess the number (1 to 10): "))
    tries += 1

    if guess == secret:
        print(f"Correct! You took {tries} tries.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")