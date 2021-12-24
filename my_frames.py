import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("frame and radio buttons")

frame = LabelFrame(root, text="This is my Frame...", padx=20, pady=20) #pads inside the frame
frame.pack(padx=100, pady=10) #pads outside the frame

b = Button(frame, text = "Don't push me!")
b.grid(row=0,column=0)
b2 = Button(frame, text = "Don't You Dare!")
b2.grid(row=1,column=0)
#Event Loop

frame2 = LabelFrame(root,text = "Radio Frame",padx =20, pady=20)
frame2.pack(padx=100, pady=10)

r = IntVar() #makes sure r is an integer
r.set(2) #sets default value

Toppings=[("Pepperoni","Pepperoni"),("Cheese","Cheese"),("Mushroom","Mushroom"),("Onion","Onion")]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in Toppings:
    Radiobutton(root, text = text, variable = pizza, value = topping).pack()

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

Radiobutton(frame2, text="Option 1", variable=r, value=1, command = lambda: clicked(r.get())).pack()
Radiobutton(frame2, text="Option 2", variable=r, value=2, command = lambda: clicked(r.get())).pack()

myLabel = Label(root, text = r.get())
myLabel.pack()

myButton = Button(root, text = "Add Pizza Topping", command = lambda:clicked(pizza.get())).pack()

myButton2 = Button(root, text = "Add options", command = lambda:clicked(r.get())).pack()

root.mainloop()