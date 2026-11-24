# Day 5 - Contact Book v1: add one contact and print saved contacts
contacts = {}

name = input("Enter name: ")
phone = input("Enter phone: ")

contacts[name] = phone

print("\nSaved Contacts: ")

for n,p in contacts.items():
    print(n, ":", p)
