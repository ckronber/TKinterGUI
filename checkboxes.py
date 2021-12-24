import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Click Button to See Image")
root.geometry("300x200")

def is_checked():
    global var
    my_label = Label(root, text=var.get()).pack()

var = StringVar()
#var = IntVar()
c = Checkbutton(root, text = "Check This Box",variable=var,onvalue="ON",offvalue="OFF",command=is_checked)
c.deselect() # used to deselect the checkbox
c.pack()

myButton = Button(root, text="Show Selection", command=is_checked).pack()
root.mainloop()