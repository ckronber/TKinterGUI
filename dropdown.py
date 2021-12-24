import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Click Button to See Image")
root.geometry("300x200")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

#used as a list instead of using in Optionsmenu
options = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday"]

clicked = StringVar(value="Monday")
drop = OptionMenu(root, clicked, *options).pack()

myButton = Button(root,text="Show Selection",command = show).pack()

root.mainloop()