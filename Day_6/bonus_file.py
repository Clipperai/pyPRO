# Day 6 - Bonus file handling: appending with the with statement
with open('notes.txt', 'a') as f:
    f.write("\n New line")
    f.close()
