import random

secret = random.randint(1,10)

while True:
    guess = int(input("Guess(1-10): "))

    if guess == secret:
        print("Correct! You Won.")
        break

    else:
        print("Wrong! Try Again")
