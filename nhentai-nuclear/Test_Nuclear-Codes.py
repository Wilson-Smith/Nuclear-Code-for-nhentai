# Libraries are here
from tkinter import *
import random
import requests
import os

def CodeCreation(code):
    # Creation of the code
    for i in range(6):
        code += str(random.randint(0, 9))
    return code

def Url(CodeHentai):
    # Creation of the link
    url = 'https://nhentai.to/g/' + str(CodeHentai) + '/'
    return url

def UrlStatus(link):
    # Status of the Link    
    r = requests.get(link)
    return r

def button():
    while True:
        code = ""
        CodeHentai = CodeCreation(code)
        link = Url(CodeHentai)
        r = UrlStatus(link)
        # Launching Chrome in Incognito if there is a real hentai
        if r.status_code != 404:
            os.system('start chrome --incognito '+'"' + link + '"')
            break

# Create object
root = Tk()

# Adjust window size
root.geometry("500x500")
root.configure(width=500, height=500)

# Set window center
root.eval('tk::PlaceWindow . center')

# Add image file
bg = PhotoImage(file="backgroundhentai.png")

# Add icon file
root.iconbitmap('iconhentai.ico')

# Title window
root.title("Nhentai Randomizer Shit")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

label2 = Label(root, text="Nuke")
label2.pack(pady=50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=20)

#Creating The Button
button1 = Button(root, text="NUKE EVERYTHING", command=button)
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
