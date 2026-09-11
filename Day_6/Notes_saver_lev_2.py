print("\n\nWelcome to Our Notes Saver:\n")

while True:
    print("\n1.Add Note")
    print("\n2.View Note")
    print("\n3.Exit\n")

    choice = input("choose: ")

    if choice == '1':
        note = input("\nEnter your note: ")
        with open("notes.txt", 'a') as v:
         v.write(note + "\n")
    
    elif choice == '2':
       with open("notes.txt", 'r') as v:
          print("\nYour Notes:\n ")
          print(v.read())

    elif choice == '3':
       print("\nExiting...\n")
       break

    else:
       print("Invalid Choice")
              