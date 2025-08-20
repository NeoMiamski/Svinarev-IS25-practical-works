import tkinter as tk
from msvcrt import locking
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pickle

def open_file():
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )

root = tk.Tk()
root.title('Форма заявки') #заголовок
root.geometry('800x600')

form = Label(
   root,
   text="Форма заявки"
)

conditions = Label(
   root,
   text="Допустимые типы вложений: zip, rar, txt, doc, jpg, png, odt, xml\nМакс. размер каждого файла: 1024kb,\nМакс. общий размер файла: 2048kb."
)

name = Label(
   root,
   text="Ваше имя:"
)

email = Label(
   root,
   text="Ваше Email:"
)

theme = Label(
   root,
   text="Тема письма:"
)

file1 = Label(
   root,
   text="Прикрепить файл:"
)

file2 = Label(
   root,
   text="Прикрепить файл:"
)

file3 = Label(
   root,
   text="Прикрепить файл:"
)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root)
e5 = tk.Entry(root)

form.grid(row=0)
conditions.grid(row=1)
name.grid(row=2, column=0)
email.grid(row=3, column=0)
theme.grid(row=4, column=0)
file1.grid(row=5, column=0)
file2.grid(row=6, column=0)
file3.grid(row=7, column=0)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)

open_button = tk.Button(root, text="Открыть файл", command=open_file)
open_button.pack(pady=10)

text_area = tk.Text(root)
text_area.pack(padx=10, pady=10)

root.mainloop() #отображение окна