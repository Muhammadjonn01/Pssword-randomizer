import random
from tkinter import *

letters = 'qwertyuiopasdfghjklzxcvbnm'
symbols = ':;!@#$%^&*()_+-={[]}'

root = Tk()
root.geometry('400x500')
root.title('Password Randomizer')
root.config(background='black')

add_letters = False
add_symbols = False
passwords = []

def letters_add():
    global add_letters
    add_letters = True
    label.config(text='')

def symbols_add():
    global add_symbols
    add_symbols = True
    label.config(text='')

def pass_ran():
    global add_letters, add_symbols

    password = ''

    all_chars = ''

    if add_letters:
        all_chars += letters
    if add_symbols:
        all_chars += symbols
        
    all_chars += '1234567890'

    if not all_chars:
        label.config(text="Please add letters or symbols")
        return

    for i in range(8):
        password += random.choice(all_chars)

    passwords.append(password)
    label.config(text=password)

def reset():
    global add_letters, add_symbols, passwords
    add_letters = False
    add_symbols = False
    passwords = []
    label.config(text='')

label = Label(text='Password Randomizer', font='Times 20', fg='white', background='black')
label.place(x=75, y=70)

label = Label(text='', font='Times 20', fg='black', height=1, width=16)
label.place(x=75, y=150)

letters_button = Button(text='ADD LETTERS', fg='black', height=2, width=11, background='white', command=letters_add)
letters_button.place(x=75, y=250)

symbols_button = Button(text='ADD SYMBOLS', fg='black', height=2, width=11, background='white', command=symbols_add)
symbols_button.place(x=230, y=250)

gen = Button(text='GENERATE', fg='black', height=2, width=11, background='white', font='20', command=pass_ran)
gen.place(x=150, y=350)

reset_button = Button(text='RESET', fg='black', height=2, width=13, background='white', command=reset)
reset_button.place(x=155, y=420)

root.mainloop()