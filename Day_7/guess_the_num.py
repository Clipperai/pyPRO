import random

secret = random.randint(1,10)

guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("You won! ")

else:
    print("Wrong! Number was: ", secret)
    