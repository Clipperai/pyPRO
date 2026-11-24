# Day 6 - Notes Saver v1: take a note and append it to notes.txt
note = input("Enter your notes here: ")

with open('notes.txt', 'a') as n:
    n.write('\n'+ note)
