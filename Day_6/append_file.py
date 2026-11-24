# Day 6 - Appending to a file: open in append mode and add a line
file = open("notes.txt", 'a')
file.write("\nSecond line.")
file.close()
