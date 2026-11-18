# Day 1 - Calculator v1.5: menu calculator with functions (square, cube, factorial, even/odd)

def square(n):
    return n * n

def cube(n):
    return n * n * n

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def add(n):
    s = int(input("Enter another number: "))
    return n + s


while True:
    n = int(input("Enter a number: "))
    choice = input("Choose an operation \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Square \n6.Cube \n7.factorial \n8. Even/Odd Checker \n9.Exit: ")

    if choice == '1':
        print("Addition:", add(n))

    elif choice == '2':
        s = int(input("Enter another number: "))
        print(n - s)

    elif choice == '3':
        s = int(input("Enter another number: "))
        print(n * s)

    elif choice == '4':
        s = int(input("Enter another number: "))
        if s == 0:
            print("Can't divide by zero")
        else:
            print(n / s)

    elif choice == "5":
        print("Square:", square(n))

    elif choice == "6":
        print("Cube:", cube(n))

    elif choice == "7":
        print("Factorial:", factorial(n))

    elif choice == "8":
        if is_even(n):
            print("Even")
        else:
            print("Odd")

    elif choice == '9':
        print("Exiting...")
        break

    else:
        print("Invalid operation.")
