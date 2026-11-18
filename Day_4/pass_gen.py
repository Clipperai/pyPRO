# Day 4 - Password Generator v1: a random 8-character password (letters + digits)

import random
import string

chars = string.ascii_letters + string.digits
password = ""

for i in range(8):
    password += random.choice(chars)

print("Generated Password: ", password)

# string.ascii_letters = A-Z,a-z
# string.digits = 0-9
# random.choice = picks random characters
