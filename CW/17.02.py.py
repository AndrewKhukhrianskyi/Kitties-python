from tkinter import *

import tkinter.messagebox as mb

def crypt():
    text = text_field.get(0.0, END).strip().upper().split()
    number = int(number_field.get(0.0, END).strip())
    cipher = ''
    dictionary = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    mb.showinfo(title = 'Инфо',
                message = "Данные зашифрованы!")
    for index in range(len(text)):
        for index_2 in range(len(dictionary)):
            if 0 <= index_2 + number < len(dictionary) and text[index] == number:
                cipher += dictionary[index_2 + number]
            elif index_2 + number >= len(dictionary) and text[index] == dictionary[index_2]:
                cipher +=(dictionary[(1 - index_2 - number) % (len(dictionary) - 1)])
            elif index_2 + number < 0 and text[index] == dictionary[index_2]:
                cipher +=(dictionary[(index_2 + number) % len(dictionary)])


    file = open('crypt_message.txt' ,'w')
    file.write(cipher)
    file.close()

    mb.showinfo(title = 'Инфо',
                message ='Шифротекст сохранился в файле!')

def decrypt():
    pass

window = Tk()

window.geometry('500x550')
window.resizable(False,False)

label = Label(width = 20,
              text = 'Введите текст ниже:')
text_field = Text(width = 50,
                  height = 10)
label_2 = Label(width = 20,
              text = 'Сдвиг:')
number_field = Text(width = 5,
                    height = 1)
crypt_button = Button(width = 8,
                      height = 2,
                      text = 'Crypt!',
                      command = crypt)
decrypt_button = Button(width = 8,
                        height = 2,
                        text = 'Decrypt!')

widgets = [label, text_field, label_2, number_field,
           crypt_button, decrypt_button]
for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()
