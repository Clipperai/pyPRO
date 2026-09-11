contacts = {}

name = input("Enter name: ")
phone = input("Enter phone: ")

contacts[name] = phone

print("\nSaved Contacts: ")

for n,p in contacts.items():
    print(n, ":", p)