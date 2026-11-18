# Day 2 - Loops: collecting marks in a list with a for loop

marks = []

sub = int(input("Enter number of subjects: "))

for m in range(sub):
    m = int(input(f"Enter marks {m + 1}: "))

    marks.append(m)

print(marks)
