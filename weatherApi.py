import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
#from PIL import ImageTk, Image
import sqlite3
import json,requests,sqlite3
from requests import api

root = Tk()
root.title("Air Quality Information from airnow.org")
root.geometry("400x350")

zip_label = Label(root,text = "Enter Zip Code")
zip_label.pack()
my_zip = Entry(root,width = 20,borderwidth=2)
my_zip.pack()

global myFrame


def get_weather_data():
    myFrame = Frame(root)
    myFrame.pack()

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+str(my_zip.get())+"&distance=25&API_KEY=D086A2F4-9F3E-4AC4-8491-BE808D183182")
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error: "+ str(e)

    myText = []
    #my_label = Label(myFrame,text=api)
    #my_label.pack()

    locText = "Location: "+ api[0]['ReportingArea'] + " |  Date: " + api[0]['DateObserved']
    my_label1 = Label(root, text=locText).pack()

    for num in range(len(api)):
        myText.append(api[num]['ParameterName'] + ": " +api[num]['Category']['Name'] + " | AQI: " + str(api[num]['AQI']))
        my_label = Label(root, text=myText[num]).pack()

    return my_label

zip_button = Button(root,text = "Submit", command = get_weather_data).pack()

root.mainloop()