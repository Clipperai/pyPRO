# Day 3 - Number Toolkit (Level 1): square, cube, even/odd, factorial using functions

def square(num):
    return num * num

def cube(num):
    return num * num * num

def is_even(num):
    return num % 2 == 0

def factorial(num):
    if num < 0:
        return "not defined for negative numbers"
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))

print(f"Square: {square(num)}")
print(f"Cube: {cube(num)}")
print(f"Even: {is_even(num)}")
print(f"Factorial: {factorial(num)}")
