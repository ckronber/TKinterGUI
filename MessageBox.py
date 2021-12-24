import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Message Box")
root.minsize(height=300,width=300)

def popup():
    #messagebox.showinfo("This is my Popup!", "Hello World!")
    #messagebox.showwarning("ERROR", message="WTF ARE YOU DOING?")
    #messagebox.showerror("ERROR", message="WTF ARE YOU DOING?")
    #response = messagebox.askquestion("Question", message="Are you sure?")
    #response = messagebox.askokcancel("Question","OK to cancel?")
    response = messagebox.askyesno("Question","OK to cancel?")
    #Label(root, text=response).pack()
    print(response)

    if response == TRUE:
        Label(root,text="Yes").pack()
    else:
        Label(root,text="No").pack()
   
Button(root, text="Popup", command=popup).pack()

root.mainloop()