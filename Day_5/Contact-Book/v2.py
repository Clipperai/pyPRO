contacts = {}

while True:
    print("\n1. Add Contacts")
    print("\n2. View Contacts")
    print("\n3. Search Contacts")
    print("\n4. Exit\n")

    choice = input("\nChoose: ")
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contacts[name] = phone

    elif choice == '2':       
      if contacts:
        print("\nSaved Contacts: ")
        for n,p in contacts.items():
            print(n, ":", p)
      
      else:
         print("\nNot any Contacts here yet. ")
          

    elif choice == '3':       
        name = input("Enter name to search: ")
        if name in contacts:
            print("Number:" , contacts[name])
        
        else:
            print("Contact not found")
        
    elif choice == '4':  
           print("Exiting....")     
           break
    
    else:
        print("Invalid choice")
    
             
             

    