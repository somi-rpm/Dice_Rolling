from tkinter import *
import random

mainwindow = Tk(className="Dice Rolling")
mainwindow.geometry("600x400")
mainwindow.configure(bg='yellow')

text_1 = Label(mainwindow, font=("arial", 300))


def roll_the_dice():
    numbers = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    numbers1 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d1 = random.choice(numbers)
    d2 = random.choice(numbers1)
    text_1.config(text=f'{d1}{d2}')
    text_1.pack()


b1 = Button(mainwindow, text="Roll the Dice!", bg='red', foreground='white', command=roll_the_dice)
b1.place(x=250, y=0)
b1.pack()

mainwindow.mainloop()
