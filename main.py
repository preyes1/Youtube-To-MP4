import tkinter
from tkinter import filedialog
import customtkinter #makes UI nicer
from pytube import YouTube
from PIL import Image
import os

#allows the user to choose the path to download
def getPath():
    global dir
    dir = filedialog.askdirectory()
    if dir:
        pathLabel.configure(text=dir)

def convertMP4():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download(dir)
        titleLabel.configure(text=ytObject.title)
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Failed", text_color="red")

def convertMP3():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        mp3 = ytObject.streams.get_audio_only()
        mp3.download(dir)
        titleLabel.configure(text=ytObject.title)
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Failed", text_color="red")
    
    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("500x500")
app.resizable(False, False)
app.title("Youtube Downloader")
image = customtkinter.CTkImage(light_image=Image.open('backgroundanime.png'),
                                dark_image=Image.open('backgroundanime.png'),
                                size=(220,310))
mylabel = customtkinter.CTkLabel(app, text="", image=image)
mylabel.place(x=280,y=200)


#adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack()

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Download mp4 Button
download4 = customtkinter.CTkButton(app, text="Download MP4", command=convertMP4)
download4.place(x=60, y=100)
#Download mp3 Button
download3 = customtkinter.CTkButton(app, text="Download MP3", command=convertMP3)
download3.place(x=300, y=100)

titleLabel = customtkinter.CTkLabel(app, text="")
titleLabel.pack(pady=10)

dir = os.getcwd()

pathButton = customtkinter.CTkButton(app, text="Change Path", command=getPath)
pathButton.pack()

pathLabel = customtkinter.CTkLabel(app, text=dir)
pathLabel.pack()





app.mainloop()