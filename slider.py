import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Click Button to See Image")
root.geometry("300x200")

vertical = Scale(root, from_=500, to = 100)
vertical.pack()

def setVol():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+ str(vertical.get()))

horizontal = Scale(root, from_=100, to = 500,orient="horizontal")
horizontal.pack()

my_button = Button(root, text ="Set Volume",command=setVol).pack()

root.mainloop()