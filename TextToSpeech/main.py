import pyttsx3

# Initialization
engine = pyttsx3.init() 

# Read the text from input.txt
with open('input.txt', 'r') as file:
    text = file.read()

# Write the text on the terminal
# text = input("What you want me to say? ")

# Make the engine say what's in the text
engine.say(text) 
engine.runAndWait()