# Day 4 - Password Generator v2: choose the length, symbols included

import random
import string

length = int(input("Enter password length: "))

if length <= 0:
    print("Password length must be at least 1.")
else:
    chars = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Strong Password: ", password)
