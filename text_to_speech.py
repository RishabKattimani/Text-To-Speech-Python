# ------------------------------------------------------------------------------
# Imports
import pyttsx3

# ------------------------------------------------------------------------------
# Variable Text
# text = "This is an automated message"
# ------------------------------------------------------------------------------
# Input Text
input = input("Type your text here : ")

# ------------------------------------------------------------------------------
# Speech
speaker = pyttsx3.init()

speaker.say(input)
speaker.runAndWait()
