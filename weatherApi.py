import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox, filedialog
#from PIL import ImageTk, Image
import sqlite3
import json,requests,sqlite3

from requests import api

root = Tk()
root.title("Address Information Database")
root.geometry("400x350")

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=46205&distance=25&API_KEY=D086A2F4-9F3E-4AC4-8491-BE808D183182")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error: "+ str(e)

my_label = Label(root, text=api[0]).pack()
root.mainloop()