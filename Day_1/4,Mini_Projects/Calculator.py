num = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter {i + 1} number: "))
    num.append(element)


choice = input("Choose an operation \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division : ")
if choice == '1':
    print(sum(num))

elif choice == '2':
    result = num[0]
    for i in range(1, len(num)):
        result -= num[i]
    print(result)

elif choice == '3':
    result = 1
    for i in range(len(num)):
        result *= num[i]
    print(result)

elif choice == '4':
    if num[0] != 0:
        result = num[0]
        for i in range(1, len(num)):
            if num[i] == 0:
                print("Cannot divide by zero.")
                break
            else:
              print(result)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operation.")   
