tasks = []

while True:

    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")  
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")
    if choice == '1':
        task = input("\nEnter a task: ")
        tasks.append(task)
        print("\nTask added successfully.")
    
    elif choice == '2':
        if tasks:
            print("\nYour To-Do List:")
            for t in tasks:
                print("#", t)
        else:
            print("\nYour To-Do List is empty.\n")
    
    elif choice == '3':
        print("\nExiting the To-Do List App. Goodbye!\n")
        break

    else:
        print("\nInvalid choice.Please enter 1, 2, or 3.\n")