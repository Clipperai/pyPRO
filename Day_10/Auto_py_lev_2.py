# Day 10 - Website Opener (Level 2): looping version - open more than one website
import webbrowser

def website_opener(command):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
    
    elif "google" in command:
        webbrowser.open("https://www.google.com")
    
    elif "github" in command:
        webbrowser.open("https://www.github.com")

    elif "brave" in command:
        webbrowser.open("https://brave.com")
    
    else: 
        print("Website not Programmed yet!")

while True:

    print("\nWelcome to the Website Opener!")
    print("\nYou can open the following websites: YouTube, Google, GitHub, Brave")

    command = input("\nEnter the website you want to open: ").lower()
    website_opener(command)

    if command in ["youtube", "google", "github", "brave"]:

        print(command,"opened Successfully!\n")
    else: 
        print("Failed to open", command, "\n")

    choice = input("Do you want to open another website? (yes/no): ")
    
    if choice.lower() == "no":
        print("Exiting the program. Goodbye!")
        break
    else:
        continue
