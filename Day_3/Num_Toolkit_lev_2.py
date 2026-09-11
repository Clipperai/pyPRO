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


while True:
    print("\n1. Square")
    print("2. Cube")
    print("3. Even/Odd")
    print("4. factorial")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "5":
        print("Exiting...")
        break

    num = int(input("Enter number: "))

    if choice == "1":
        print("Square:", square(num))

    elif choice == "2":
        print("Cube:", cube(num))

    elif choice == "3":
        if is_even(num):
            print("Even")
        else:
            print("Odd")
    
    elif choice == "4":
          print("Factorial:", factorial(num))

    else:
        print("Invalid choice")