from tkinter import *

ALPHABETS = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7,
             'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
             'M' : 15, 'O' : 16, 'P' : 17, 'Q' : 18, 'R' : 19, 'S' : 20, 'T' : 21,
             'U' : 22, 'V' : 23, 'W' : 24, 'X' : 25, 'Y' : 26, 'Z' : 27}
def crypt_decrypt():
    text_string = text.get(0.0, END).upper().strip()
    cypher_text = ''
    decrypt_text = ''
    if int_var.get() == 1:
        for symbol in text_string:
            cypher_text += str(ALPHABETS[symbol]) + ','
        print(cypher_text)
    elif int_var.get() == 2:
        new_text = text_string.strip().split(',')
        decrypt_dict = dict(zip(ALPHABETS.values(), ALPHABETS.keys()))
        for number in new_text:
            try:
                decrypt_text += decrypt_dict[int(number)]
            except:
                print(decrypt_text)


window = Tk()
window.geometry('300x200')
window.resizable(False, False)

text = Text(width=20,
            height=1)
int_var = IntVar() # Это поле нужно для подключения радиокнопок
button = Button(text = 'Click!',
                width = 8,
                height = 1,
                command = crypt_decrypt)
rb_1 = Radiobutton(variable = int_var,
                   value = 1,
                   text = 'Crypt')
rb_2 = Radiobutton(variable = int_var,
                   value = 2,
                   text = 'Decrypt')
widgets = [text, button, rb_1, rb_2]

for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()
