# Libraries are here
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import webbrowser
import os
import urllib
import requests
from bs4 import BeautifulSoup


# Create object
root = Tk()


# Creating the function for the button
def button():

    # Generate a random number with 6 digits
    def Generate_Code():
        code = ''
        for i in range(6):
            code += str(random.randint(0,9))
        return code
    Generate_Code()
    # Attach the generated number to the link and validate it
    
    def valid_url():
        valid = False
        # Validation of the link
        while valid == False:
            url = 'https://nhentai.net/g/'+Generate_Code()+'/'
            r = requests.get(url)
            if r.status_code != 404:
                valid = True
        return url
    valid_url()

    generate = True

    # If the link is valid, open it in chrome, in incognito mode
    def btn1():
        url = valid_url()
        os.system('start chrome --incognito '+'"'+url+'"')
    btn1()


# Adjust window size
root.geometry("500x500")
root.configure(width=500, height=500)

# Set window center
root.eval('tk::PlaceWindow . center')

# Add image file
bg = PhotoImage(file = "backgroundhentai.png")

# Add icon file
root.iconbitmap('iconhentai.ico')

# Title window
root.title("Nhentai Randomizer Shit")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

label2 = Label( root, text = "Nuke")
label2.pack(pady = 50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )

#Creating The Button
button1 =  Button(root, text="NUKE EVERYTHING", command=button)
#put on screen
button1.pack()

# move window center
winWidth = root.winfo_reqwidth()
winwHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
root.geometry("+{}+{}".format(posRight, posDown))

# Execute tkinter
root.mainloop()

