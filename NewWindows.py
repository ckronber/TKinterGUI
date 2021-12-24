import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Click Button to See Image")
root.minsize(height=100,width=300)

def openImage():
    global my_image

    top = Toplevel()
    top.title("Image")
    my_image = ImageTk.PhotoImage(Image.open("C:\\Users\ckron\Desktop\TKinterGUI\Images\pic6.jpg"))
    my_label = Label(top, image = my_image).pack()

my_button = Button(root, text = "Open Image", command = openImage).pack(pady = 50)


root.mainloop()