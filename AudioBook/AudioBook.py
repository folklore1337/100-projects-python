import pyttsx3
import PyPDF4

book = open('AudioBook/the-story-of-doctor-dolittle.pdf', 'rb')
bookPDF = PyPDF4.PdfFileReader(book)
totalPage = bookPDF.getNumPages()
getPage = bookPDF.getPage(1)
getText = getPage.extractText()
speaker = pyttsx3.init()
speaker.say(getText)
speaker.runAndWait()