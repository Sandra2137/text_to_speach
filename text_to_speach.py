from gtts import gTTS
from tkinter import *
import PyPDF2

BACKGROUND = '#eeeeee'
BLUE = '#9FC9F3'
PURPLE = '#BEADFA'
PINK = '#F07DEA'
FONT_NAME = "Courier"

# FUNCTIONS

def open_pdf():
    file_path = file_entry.get()
    pdf = PyPDF2.PdfReader(open(file_path, 'rb'))
    
    global text

    text = ''
    for page_num in range(len(pdf.pages)):  
        page = pdf.pages[page_num] 
        text += page.extract_text()
        
    doc_file = Toplevel(window)
    doc_file.title("Your PDF file")
    
    text_widget = Text(doc_file, wrap=WORD, width=40, height=10)
    text_widget.pack()
    text_widget.insert("1.0", text)
    text_widget.config(state="disabled")  

    convert_button = Button(doc_file, text="Convert to MP3", fg=PINK, command= convert_pdf)
    convert_button.pack()
    
    doc_file.transient(window)
    doc_file.grab_set()


def convert_text():
    inputValue=text_input.get("1.0","end-1c")
    tts = gTTS(inputValue)
    tts.save('text_to_speach.mp3')

def convert_pdf():
    pdf_tts = gTTS(text)
    pdf_tts.save('text_to_speach_pdf.mp3')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Text to speach converter')
window.config(padx=40, pady=40, bg=BACKGROUND)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
tts_img = PhotoImage(file='./ttss.png')
canvas.create_image(75, 100, image = tts_img)
canvas.grid(column=1, row=0)

title_label = Label(text='Type your text to transform it into speech, \n or upload a PDF file for conversion.', font =(FONT_NAME, 20), fg = BLUE, bg= BACKGROUND)
title_label.grid(column=1, row=1)

text_input = Text(window, height=5, width=40, font=FONT_NAME)
text_input.grid(column=0, row=3, columnspan=2)

text_label = Label(window, text="Text: ", fg=PURPLE)
text_label.grid(column=0, row=3)

text_button = Button(text="Convert", highlightthickness=0, command=convert_text,  fg=PINK)
text_button.grid(column=3, row=3)

file_button = Button(text="Convert pdf", highlightthickness=0, command= open_pdf, fg=PINK)
file_button.grid(column=3, row=4)

file_label = Label(window, text="Paste pdf path:", fg=PURPLE)
file_label.grid(column=0, row=4)

file_entry = Entry(window)
file_entry.grid(column=1, row = 4)


window.mainloop()