# ------------------------------------------------------------------------------
# Imports
import pyttsx3
import PyPDF2

# ------------------------------------------------------------------------------
# Reading the PDF
pdf = open("harry-potter-book.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)

pageObj = reader.getPage(2)

# print(pageObj.extractText())
# ------------------------------------------------------------------------------
# Speech

speaker = pyttsx3.init()

speaker.say(pageObj.extractText())
speaker.runAndWait()
