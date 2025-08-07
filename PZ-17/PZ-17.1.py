from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Форма заявки') #заголовок
root.geometry('800x600')

def button_clicked():
    print("Клик")

def close():
    root.destroy()
    root.quit()

button = ttk.Button(root,
    text="Press Me",
    command=button_clicked)
button.pack(fill=BOTH)

root.protocol('WM_DELETE_WINDOW', close)



root.mainloop() #отображение окна