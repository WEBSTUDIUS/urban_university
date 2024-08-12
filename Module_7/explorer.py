import tkinter
import os
import subprocess, sys
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='.', title='Choose a file', filetypes=(
        ('Text', '.txt'), ('All files', '.*')))

    os.system(f'open {filename}') # doesnt open files with spaces


window = tkinter.Tk()

window.title('Explorer')
window.geometry('400x400')
window.resizable(False, False)

text = tkinter.Label(window, text='File', height=5, width=20, background='gray')
text.grid(row=1, column=1)

button = tkinter.Button(window, width=20, height=5, text='Choose any file', background='gray', foreground='blue',
                        command=file_select)
button.grid(row=2, column=1, pady=5)

window.mainloop()
