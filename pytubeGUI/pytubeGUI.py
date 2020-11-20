from tkinter import *
from pytube import YouTube
import pytube
import sys

# Placing the yt variable,that will eventually represent the YouTube object, 
# in the namespace
yt = None 

# Create tkinter window
root = Tk()
root.title("Python YouTube Downloader")
root.geometry("500x500")

def relaunchProgram():
    #Still figuring out how to relaunch the window
    root.destroy()
    

def downloadVideo():
    # selects 720 and downloads video to cwd
    stream = yt.streams.filter(progressive=True).first()
    stream.download()
    
    # lets user know that video is downloading
    downloadMessage= Label(
        downloadingFrame, 
        text=yt.title + (" is downloading to your current directory. Thank you"),
        font=("Arial", 16) 
        )
    downloadMessage.pack()


# Create function that verifies if user wants to download video selected
def verifyDownload():
    # Ask user if they want to download the video
    downloadVerfication = Label(
        download, 
        text="Would you like to download this video to your device?"
    )
    downloadVerfication.pack()

    downloadYes= Button(
        download, 
        text="Yes",
        padx=5, 
        pady=3, 
        font=("Arial", 16), 
        command=downloadVideo
    )

    downloadNo= Button(
        download, 
        text="No",
        padx=5, 
        pady=3, 
        font=("Arial", 16), 
        command=relaunchProgram
    )

    downloadYes.pack(side="left")
    downloadNo.pack(side="right")

    

# Create function to take a search for user input
def submitURL(url):

    try:
        # Create youtube object with user URL
        global yt
        yt =YouTube(url)
        showYTTitle =  yt.title
        
        youTubeTitle = Label(initialWindow, 
        text=showYTTitle, 
        font =("Arial", 16)
        )
        youTubeTitle.pack()

            # break out of the while loop if title is real
    except pytube.exceptions.RegexMatchError:
            # Create error message in window so user knows what went wrong
        titleError = Label(initialWindow, 
        text="Please enter correct URL from YouTube.com "
        )
        titleError.pack()

        
    
    # now create verification text and buttons
    verificationMessage = Label(
    verificationWindow, 
    text="Is this the correct video?", 
    font=("Arial", 16)
    )
    verificationMessage.pack()

    verificationYesButton = Button(
        verificationWindow, 
        text="Yes",
        padx=5, 
        pady=3, 
        font=("Arial", 16), 
        command=verifyDownload 
        )
    verificationNoButton = Button(
        verificationWindow, 
        text="No",
        padx=5, 
        pady=3, 
        font=("Arial", 16), 
        command=relaunchProgram 
        )

    verificationYesButton.pack(side="left")
    verificationNoButton.pack(side="right")
    
    

# Create and place Frame to hold initial widgets in program
initialWindow= LabelFrame(root, bd=0)
initialWindow.pack()

# Create Frame to hold, correct message, yes/no buttons
verificationWindow= LabelFrame(root, bd=0)
verificationWindow.pack()

#Download frame, holds download verify message
download = LabelFrame(root, bd=0)
download.pack()

# last frame for verification, let it be known that video is downloading 
downloadingFrame = LabelFrame(root, bd=0)
downloadingFrame.pack()

# Create title, instructions, entry bar, submit buttion widgets that belong in initial window frame for 
title = Label(
    initialWindow, 
    text="Welcome to The Python YouTube Downloader", 
    font=("Arial", 20)
    )
instructions = Label(
    initialWindow, 
    text="Enter URL of Youtube video you want to download", 
    font=("Arial", 16)
    )
searchBar = Entry(initialWindow, bd=3)

submitButton = Button(
    initialWindow, 
    text="Submit URL", 
    padx=3, 
    pady=3, 
    font=("Arial", 16), 
    command=lambda:submitURL(searchBar.get())
    )

# Place title, instructions, searchBar, and submitButton widgets in initialWindow
title.pack()
instructions.pack()
searchBar.pack()
submitButton.pack()


root.mainloop()
