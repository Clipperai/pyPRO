import webbrowser
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 190)

def speak(text):
    print("Bot said:", text)
    engine.say(text)
    engine.runAndWait()

sites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://www.gmail.com"
}

def open_web(command):
    if command in sites:
        webbrowser.open(sites[command])

    else:
        print("Not Found")
        
while(True):
    speak("Welcome")
    command= input("Enter web u want to open: ").lower()
    print(f"Opening {command}...")

    open_web(command)
    
    choice = input("Do you want to open more websites? (yes/no): ").lower()

    if choice == "yes":
        continue

    elif choice == "no":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
        break
