# Day 7 - Guess the Number v1: one guess at a random number
import random

secret = random.randint(1,10)

try:
    guess = int(input("Guess the number (1-10): "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if guess == secret:
    print("You won! ")

else:
    print("Wrong! Number was: ", secret)
    
