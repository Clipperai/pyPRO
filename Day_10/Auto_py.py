# Day 10 - Website Opener v1: open a website by name with webbrowser
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
    
    elif "chrome" in command:
        webbrowser.open("https://www.google.com/chrome/")
    
    else: 
        print("Website not Programmed yet!")

print("\nWelcome to the Website Opener!\n")

print("You can open the following Websites: Youtube, Google, Github, Brave and Chrome")
    
command = input("Enter the website you want to open: ").lower()

website_opener(command)
