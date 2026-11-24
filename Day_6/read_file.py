# Day 6 - Reading a file: open in read mode and print the contents
file = open("notes.txt", 'r')
content = file.read()
print(content)
file.close()
