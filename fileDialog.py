import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Click Button to See Image")
root.minsize(height=100,width=300)

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir= "C:/Users/ckron/Desktop/TKinterGUI/Images", title = "Select a File", filetypes=(("jpg files","*.jpg"),("All Files","*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_button = Button(root, text = "Open File", command = open).pack()


root.mainloop()