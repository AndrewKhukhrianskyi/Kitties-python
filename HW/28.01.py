from tkinter import *

def save_text():
    text = text_field.get(0.0, END)
    file = open('saved_text.txt', 'w')
    file.write(text)
    file.close()

root = Tk()

root.geometry('200x200')

text_field = Text(width = 50,
                  height = 5)
button = Button(width = 8,
                 height = 2,
                 text = 'Save text!',
                 command = save_text)

widgets = [text_field, button]

for widget in widgets:
    widget.pack(anchor='n')

root.mainloop()