note = input("Enter your notes here: ")

with open('new.text', 'a') as n:
    n.write('\n'+ note)
