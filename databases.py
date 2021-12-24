import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
#from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Address Information Database")
root.geometry("400x350")

#fileMenu = OptionMenu(root, Variable,"Hello World")

#Create a database or connect to one
conn = sqlite3.connect('address_book.db')
#Create a cursor
c = conn.cursor()

#create table
'''
c.execute("""CREATE TABLE Addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zip integer)
""")
'''

def submitEntry():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
    first_name = :first_name,
    last_name = :last_name,
    address = :address,
    city = :city,
    state = :state,
    zip = :zip

    WHERE oid = :oid""", 
    {
        "first_name":f_name_edit.get(), 
        "last_name":l_name_edit.get(), 
        "address":address_edit.get(), 
        "city":city_edit.get(), 
        "state":state_edit.get(), 
        "zip":zip_edit.get(), 
        "oid":record_id
    })

    #Commit Changes
    conn.commit()

    #close connection
    conn.close()
    editor.destroy()

#Create edit function to update database
def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("380x200")

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()

    c.execute("SELECT * FROM addresses WHERE oid = " + delete_box.get())
    records = c.fetchone()

    global f_name_edit,l_name_edit,address_edit,city_edit,state_edit,zip_edit

    #create Text boxes
    f_name_edit = Entry(editor,width=30)
    f_name_edit.insert(0,records[0])
    f_name_edit.grid(row=0,column=1,padx=20)
    l_name_edit = Entry(editor,width=30)
    l_name_edit.insert(0,records[1])
    l_name_edit.grid(row=1,column=1,padx=20)
    address_edit = Entry(editor,width=30)
    address_edit.insert(0,records[2])
    address_edit.grid(row=2,column=1,padx=20)
    city_edit = Entry(editor, width=30)
    city_edit.insert(0,records[3])
    city_edit.grid(row=3,column=1,padx=20)
    state_edit = Entry(editor, width=30)
    state_edit.insert(0,records[4])
    state_edit.grid(row=4,column=1,padx=20)
    zip_edit = Entry(editor, width=30)
    zip_edit.insert(0,records[5])
    zip_edit.grid(row=5,column=1,padx=20)

    #Create Text Box Labels
    f_name_label = Label(editor, text = "First Name").grid(row=0,column=0)
    l_name_label = Label(editor, text = "Last Name").grid(row=1,column=0)
    address_label = Label(editor, text = "Address").grid(row=2,column=0)
    city_label = Label(editor, text = "City").grid(row=3,column=0)
    state_label = Label(editor, text = "State").grid(row=4,column=0)
    zip_label = Label(editor, text = "Zip").grid(row=5,column=0)

    submit_button = Button(editor, text="Update Record in Database",command=submitEntry).grid(row=6,column=0,columnspan=2,pady=20,padx=10,ipadx=100)

    #Commit Changes
    conn.commit()
    #close connection
    conn.close()

#delete functionality for database
def delete():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()

    c.execute("DELETE From addresses WHERE oid = "+ delete_box.get())
    delete_box.delete(0,END)

    #Commit Changes
    conn.commit()

    #close connection
    conn.close()

#create submit function database
def submit():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()


    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zip)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zip':zip.get()
    }
    )

   
    if(c.rowcount == 1):
        added = Label(root, text = f_name.get()+" "+l_name.get()+" Was added to the database").grid(row=15,column=0,columnspan=2,pady=10)

    #Commit Changes
    conn.commit()

    #close connection
    conn.close()

    #clear the textboxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip.delete(0,END)

def query():
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()

    c.execute("SELECT oid,* FROM addresses")
    records = c.fetchall()

    print_records = ""
    for record in  records:
        print_records += str(record)+"\n"

    query_label = Label(root, text = print_records).grid(row=8,column=0,columnspan=2)

    #close connection
    conn.close()

global delete_box

#create Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root, width=30)
address.grid(row=2,column=1,padx=20)
city= Entry(root, width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root, width=30)
state.grid(row=4,column=1,padx=20)
zip = Entry(root, width=30)
zip.grid(row=5,column=1,padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9,column=1)

#Create Text Box Labels
f_name_label = Label(root, text = "First Name").grid(row=0,column=0)
l_name_label = Label(root, text = "Last Name").grid(row=1,column=0)
address_label = Label(root, text = "Address").grid(row=2,column=0)
city_label = Label(root, text = "City").grid(row=3,column=0)
state_label = Label(root, text = "State").grid(row=4,column=0)
zip_label = Label(root, text = "Zip").grid(row=5,column=0)
delete_box_label = Label(root,text="Id Number").grid(row=9,column=0)

#Create Submit Button
submit_button = Button(root, text="Add Record to Database",command=submit).grid(row=6,column=0,columnspan=2,pady=20,padx=10,ipadx=100)

query_btn = Button(root, text = "Show Records", command=query).grid(row=7,column=0,columnspan=2,pady=5,padx=10,ipadx=125)

#Create a delete button
delete_btn = Button(root, text="Delete Record",command=delete)
delete_btn.grid(row=11,column=0,columnspan=2,padx=10,ipadx=125)

#Create a Select Button
edit_btn = Button(root,text = "Edit Record",command=edit)
edit_btn.grid(row=12,column=0,columnspan=2,padx=10,ipadx=132,pady=5)

#Commit Changes
conn.commit()

#close connection
conn.close()

root.mainloop()