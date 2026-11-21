# Task 4: Password Authentication System

USERNAME = "student"
PASSWORD = "uni@2026"
MAX_ATTEMPTS = 3

attempts_left = MAX_ATTEMPTS

while attempts_left > 0:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == "" or password == "":
        print("Username and password cannot be empty.")
    elif username == USERNAME and password == PASSWORD:
        print(f"Login successful! Welcome, {username}.")
        break
    else:
        print("Incorrect username or password.")

    attempts_left -= 1
    if attempts_left > 0:
        print(f"Attempts remaining: {attempts_left}")
else:
    # Runs only if the loop ended without a successful login (no break)
    print("Too many failed attempts. Your account has been locked.")
