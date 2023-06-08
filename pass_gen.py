from tkinter import *
import random
import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import Tk

root = Tk()
root.title("Генератор пароля")
root.geometry("420x260")

def copy_password():
    password = str1.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена.")   # Окно информации для уведомления

def press():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbol = ['!', "@", '#', '$', '%', '^', '&', '*', '(', ')', '+']
    password = []

    for char in range(1, int(e1.get()) + 1):
        random_choice = random.choice(letters)
        password += random_choice
    for num in range(1, int(e2.get()) + 1):
        random_number_choice = random.choice(number)
        password += random_number_choice
    for num in range(1, int(e3.get()) + 1):
        random_number_choice = random.choice(symbol)
        password += random_number_choice
    random.shuffle(password)
    str1.set(''.join(password))

str1 = tk.StringVar()

lbl2 = Label(root, text="Количество букв:", font=("Arial", 12, "bold"), fg="blue")
lbl2.grid(row=2, column=0, sticky=W)
e1 = Entry(root, width=20)
e1.grid(row=2, column=0, padx=190, pady=5)

lbl2 = Label(root, text="Количество цифр:", font=("Arial", 12, "bold"), fg="orange")
lbl2.grid(row=3, column=0, sticky=W)
e2 = Entry(root, width=20)
e2.grid(row=3, column=0, padx=190, pady=5)

lbl2 = Label(root, text="Количество символов:", font=("Arial", 12, "bold"), fg="red")
lbl2.grid(row=4, column=0, sticky=W)
e3 = Entry(root, width=20)
e3.grid(row=4, column=0, padx=190, pady=5)

BTN = Button(root, text="Сгенерировать пароль", fg="green", command=press, width=20, height=2, font=("Arial", 12, "bold"))
BTN.grid(row=5, column=0, pady=2, sticky='nsew')

copy_button = Button(root, text="Копировать", fg="blue", command=copy_password, width=10, height=2, font=("Arial", 12, "bold"))
copy_button.grid(row=6, column=0, pady=5)

password_label = Label(root, textvariable=str1, font=("Arial", 15, "bold"))
password_label.grid(row=7, column=0)

root.grid_columnconfigure(0, weight=2)  # Expand column 0 to center the buttons

root.mainloop()