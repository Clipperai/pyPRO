# Day 7 - Guess the Number (Level 2): keep guessing until correct
import random

secret = random.randint(1,10)

while True:
    try:
        guess = int(input("Guess(1-10): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret:
        print("Correct! You Won.")
        break

    else:
        print("Wrong! Try Again")
