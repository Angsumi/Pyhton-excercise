import pyttsx3
import PyPDF2

Pdf = open('cartilage.pdf', 'rb') # Path to your pdf file(book)
pages = PyPDF2.PdfFileReader(Pdf)
page = pages.getPage(2)
print(page)

speak = pyttsx3.init()
speak.say(page)
speak.runAndWait()