# Import necessary libraries:
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
# Read the file in binary mode:
#book = open('testing.pdf', 'rb')
print("book :", book)

# Create a PdfFileReader object:
pdfReader = PyPDF2.PdfFileReader(book)
print("pdfReader :", pdfReader)

# Determine total number of pages int the PDF File:
pages = pdfReader.numPages
print("pages :", pages)

# Speaker initialization
speaker = pyttsx3.init()
print("speaker :", speaker)

# Access voice property for speaker
voices = speaker.getProperty('voices')
print("voices :", voices)
# Set speaker gender 0 -> male, 1-> female
speaker.setProperty('voice', voices[1].id)
print("speaker set :", speaker)

for n in range(0, pages):
    # read current page index:
    page = pdfReader.getPage(n)
    print("page :", page, ', number :', n)
    # extract the text present in current page
    text = page.extractText()
    # takes a string as the parameter and then queues the same to be converted from text-to-speech
    speaker.say(text)

# To save the audio output as a MP3 file, within this project:
# Make use of any MP3 player to access this recording whenever required
speaker.save_to_file(text, 'audio.mp3')
print("text :", text)
print("speaker :", speaker)
speaker.runAndWait()