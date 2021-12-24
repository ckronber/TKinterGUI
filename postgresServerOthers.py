import os,os.path
import tkinter as tk
from tkinter import *
from tkinter import filedialog

fileLocation = NONE

# First the window layout in 2 columns
def getFolder():
	fileLocation = filedialog.askdirectory()
	return fileLocation

def initData():
	getFolder()
	os.system("pg_ctl init[mydb] -D "+ fileLocation)
	myLabel = Label(root,text = "Server Started at "+ fileLocation)
	myLabel.pack()

def getStatus():
	if(fileLocation != NONE):
		status = os.system("pg_ctl status -D " + fileLocation)
		myLabel = Label(root,text = status)
	else:
		myLabel = Label(root,text = "Server Not Started!")
	myLabel.pack()

def myStart():
	getFolder()
	if(fileLocation != NONE):
		os.system("pg_ctl start -D "+ fileLocation)
		myLabel = Label(root,text = "Server Started at "+ fileLocation)
	myLabel.pack()

def myStop():
	os.system("pg_ctl stop -D "+ fileLocation)
	if(fileLocation != NONE):
		print(fileLocation)
		myLabel = Label(root,text = "Server Stopped at "+ fileLocation)
	else:
		myLabel = Label(root,text = "Server Not Started!")
	myLabel.pack()

def restartServ():
	if(fileLocation != NONE):
		os.system("pg_ctl restart -D "+ fileLocation)
		myLabel = Label(root,text = "Server Restarted at: "+ fileLocation)
	else:
		myLabel = Label(root,text = "Server Not Started!")
	myLabel.pack()

root = Tk()

#creating title
root.title("Postgres SQL Server GUI")

#creating label widget
#myLabel = Label(root,text = "Hello World!").grid(row=0,column=0)
#creating label widget
#myLabel1 = Label(root,text = "Chris Kronberg").grid(row=1,column=0)

#e = Entry(root,width=50)
#e.pack()

startServer= Button(root, text = "Initialize Database", command=initData,height=2,width=10)
startServer.pack()

startServer= Button(root, text = "Status", command=getStatus,height=2,width=10)
startServer.pack()

startServer= Button(root, text = "Start Server", command=myStart,height=2,width=10)
startServer.pack()

stopServer = Button(root, text = "Stop Server", command=myStop,height=2,width=10)
stopServer.pack()

stopServer = Button(root, text = "Restart Server", command=restartServ,height=2,width=10)
stopServer.pack()

#Event Loop
root.mainloop()

'''
try:
	filePath = tk.filedialog.askopenfilename()
except:
	print("ERROR occured!")

os.system("postgres -D "+ filepath)
'''