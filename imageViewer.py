import os,os.path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("C:\\Users\ckron\Desktop\TKinter GUI\Images\pic1.jpg"),size = .5)
my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\ckron\Desktop\TKinter GUI\Images\pic2.jpg"),size = .5)
my_img3 = ImageTk.PhotoImage(Image.open("C:\\Users\ckron\Desktop\TKinter GUI\Images\pic3.jpg"),size = .5)
my_img4 = ImageTk.PhotoImage(Image.open("C:\\Users\ckron\Desktop\TKinter GUI\Images\pic4.jpg"),size = .5)
my_img5 = ImageTk.PhotoImage(Image.open("C:\\Users\ckron\Desktop\TKinter GUI\Images\pic6.jpg"),size = .5)

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

num = 0
text_label = Label (text = "Image " + str(num+1)+ " of " + str(len(image_list)),bd=1, relief = SUNKEN)
text_label.grid(row=0,column=0,columnspan=3,sticky=W+E)
my_label = Label(image=my_img1)

def forward():
    global my_label
    global text_label
    global button_forward
    global button_back
    global num

    num +=1
    text_label.grid_forget()
    text_label = Label (text = "Image " + str(1+(num%5)) + " of " + str(len(image_list)),bd=1, relief = SUNKEN)
    text_label.grid(row=0,column=0,columnspan=3,sticky=W+E)
    my_label.grid_forget()
    my_label = Label(image = image_list[num%5])
    my_label.grid(row=1,column=0,columnspan=3)

def back():
    global num
    global text_label
    global my_label
    global button_forward
    global button_back

    num -=1
    text_label.grid_forget()
    text_label = Label(text = "Image " + str(1+(num%5)) + " of " + str(len(image_list)),bd=1, relief = SUNKEN)
    text_label.grid(row=0,column=0,columnspan=3,sticky=W+E) 
    my_label.grid_forget()
    my_label = Label(image = image_list[num%5])
    my_label.grid(row=1,column=0,columnspan=3)
    if(num == 0):
        num == 5
        

button_back = Button(root, text = "<<",command = back)
button_exit = Button(root, text = "Exit", command = root.quit)
button_forward = Button(root, text = ">>",command = forward)

button_back.grid(row=2,column=0)
button_exit.grid(row=2,column=1)
button_forward.grid(row=2,column=2,pady=10)
my_label.grid(row=1,column=0,columnspan=3)

#Event Loop
root.mainloop()