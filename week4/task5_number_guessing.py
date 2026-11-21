# Task 5: Number Guessing Game

import random

MAX_ATTEMPTS = 7
secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")
print(f"You have {MAX_ATTEMPTS} attempts.")

while attempts < MAX_ATTEMPTS:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < 1 or guess > 100:
        print("Out of range! Guess between 1 and 100. (Not counted)")
        continue

    attempts += 1

    if guess == secret:
        if attempts == 1:
            print("PERFECT SCORE! You guessed it on the first try!")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret:
        print("Higher!")
    else:
        print("Lower!")
else:
    print(f"Out of attempts! The secret number was {secret}.")
