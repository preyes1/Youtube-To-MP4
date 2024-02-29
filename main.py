import tkinter
import customtkinter #makes UI nicer
from pytube import YouTube


def convertMP4():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        titleLabel.configure(text=ytObject.title)
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Failed", text_color="red")
    
    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("500x500")
app.title("Youtube Downloader")

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

#Download Button
download = customtkinter.CTkButton(app, text="Download", command=convertMP4)
download.pack(pady=10)

titleLabel = customtkinter.CTkLabel(app, text="")
titleLabel.pack(pady=10)






app.mainloop()