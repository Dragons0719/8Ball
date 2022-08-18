# Magic 8 Ball in Tkinter v2.0
# August 18
# Created by Elijah Rothenberger

from tkinter import *
import random as r
from tkinter import Label


def answer():
    label1.config(text=f"{r.choice(answers)}")


def clear():
    label1.config(text="")


root = Tk()
root.geometry('1900x1000')
root.title('Magic 8 Ball')
root.config(bg='light green')
img = PhotoImage(file='C:\\Users\\ebrotenberger\\Downloads\\8-Ball_Pool.jpg')
root.tk.call('wm', 'iconphoto', root._w, img)
message = Label(font=('Goudy Old Style', 30), text='Ask the Magic 8 Ball a yes/no question'
                                                   '\n in the space below!', bg='light green')
message.place(x=650, y=15)
user_entry = Entry(font=('Goudy Old Style', 30), bg='black', fg='light green')
user_entry.place(x=760, y=200)
button1 = Button(font=('Goudy Old Style', 20), text='        Enter        ', bg='black', fg='white', command=answer)
button1.place(x=865, y=300)
button2 = Button(font=('Goudy Old Style', 20), text='        Clear        ', bg='black', fg='white', command=clear)
button2.place(x=865, y=400)
label1 = Label(font=('Goudy Old Style', 25), text="", bg='light green')
label1.place(x=886, y=500)
answers = ["   Possibly", "  Ask Again", "     Yes", "Definitely Not", "   Idk bro", "      No", "¯\_(ツ)_/¯"]
rand_value = int(r.random() * len(answers))
root.mainloop()
