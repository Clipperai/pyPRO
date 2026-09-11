num = []
n = int(input("Enter number of elemnts:"))

for i in range(n):
    item = int(input("Enter numbers: "))
    num.append(item)

print(num)

squares = []

for i in num:
    squares.append(i *i)

print(squares)
