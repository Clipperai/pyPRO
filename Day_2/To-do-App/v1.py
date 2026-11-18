# Day 2 - To-Do App v1: a simple to-do list (enter tasks, print the list)

tasks = []

no_of_tasks = int(input("\nHow many tasks you have today?: "))
for task in range(no_of_tasks):
    task = input(f"Enter task {task + 1}: ")
    tasks.append(task)

print("\nYour To-Do List:")
print("", tasks, "\n")
