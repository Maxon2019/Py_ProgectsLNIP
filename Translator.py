import tkinter as tk
from googletrans import translator

win = tk.Tk()
win.title('Translator')
win.geometry('200*70')

#Function

def translation():
    word = entry.get()
    translator = Translator(service_urls = ['translate.google.com '])
    translation1 = translator.translate(word,dest ='ru')
    labe1 = tk.label(win, text=f"Translated in russian : {translation1.text}",bg = "yellow")
    label1.grid(row =2, column = 0)

label = tk.label(win, text = 'Enter word : ')
label.grid(row = 0, column = 0, sticky = 'W')

entry = tk.Entry(win)
entry.grid(row = 0, column = 0)
button = tk.Button(win, text = "Translate: ", command = translation)
button.grid(row = 1, column = 2)

win.mainloop()