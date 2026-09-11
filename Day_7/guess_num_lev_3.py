import random

secret = random.randint(1,10)
attempts = 0

while True:
    guess = int(input("Guess (1-10): "))
    attempts +=1    

    if guess == secret:
        print("Correct!")
        print("Attempts: ", attempts)
        break

    else:
        print("Wrong! Try Again.")
