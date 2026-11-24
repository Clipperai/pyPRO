# Day 7 - Guess the Number (Level 3): guessing loop with an attempts counter
import random

secret = random.randint(1,10)
attempts = 0

while True:
    try:
        guess = int(input("Guess (1-10): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    attempts +=1    

    if guess == secret:
        print("Correct!")
        print("Attempts: ", attempts)
        break

    else:
        print("Wrong! Try Again.")
