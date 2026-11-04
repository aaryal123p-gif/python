# Password checker: at least 8 characters and one number
while True:
    password = input("New password: ")

    has_number = False
    for character in password:
        if character.isdigit():
            has_number = True

    if len(password) < 8:
        print("Too short. Use at least 8 characters.")
    elif not has_number:
        print("Add at least one number.")
    else:
        print("Strong password. Saved!")
        break