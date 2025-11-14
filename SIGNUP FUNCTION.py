import bcrypt

def sign_up():
    ## load existing user ids
    existing_users = []
    with open("users.csv", "r") as file:
        for line in file:
            line = line.strip()
            if line:                       # skip blank lines
                user = line.split(",")[0]
                existing_users.append(user)

    # gets new user_id
    user_id = input("Enter a username: ")
    while user_id in existing_users:
        print("Username already exists. Try another.")
        user_id = input("Enter a username: ")

    ## password rules
    legal_symbols = "!.@#$%^&*()_[]"

    while True:
        password = input("Enter a password: ")

        # length rule
        if len(password) < 6:
            print("Password must be at least 6 characters.")
            continue

        # uppercase rule
        if not any(c.isupper() for c in password):
            print("Password must contain an uppercase letter.")
            continue

        # lowercase rule
        if not any(c.islower() for c in password):
            print("Password must contain a lowercase letter.")
            continue

        # digit rule
        if not any(c.isdigit() for c in password):
            print("Password must contain a digit.")
            continue

        # symbol rule
        if not any(c in legal_symbols for c in password):
            print("Password must contain a symbol:", legal_symbols)
            continue

        break  # password is valid

    ## hash password
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # append has to csv
    with open("users.csv", "a") as file:
        file.write(f"{user_id},{hashed}\n")

    print("Account created.")
