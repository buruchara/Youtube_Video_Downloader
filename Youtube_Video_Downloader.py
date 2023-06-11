#Import Libraries needed
from tkinter import *
from pytube import YouTube
import threading

# Create an API window or Frame
root = Tk()
root.geometry("600x350")  # Width x height dimensions
root.resizable(0, 0)  # False
root.config(bg="lightblue")
root.title("YouTube Video Downloader App")

# Create the text and link the entry widgets.
Label(root, text="Download any Youtube videos Here", font='Arial 14 bold').place(x=100, y=20)
Label(root, text="Paste your link here", font='Arial 14', bg='greenyellow', fg='black').place(x=120, y=50)

# Entry widget
videoLink = StringVar()
Entry(root, width=80, textvariable=videoLink).place(x=35, y=85)

# Create A Download Function
def download_video():
    url = YouTube(str(videoLink.get()))
    video_stream = url.streams.first()
    video_stream.download("C:\\Users\\USER\\Desktop\\Downloads")
    Label(root, text="Download Completed Successfully", font='Arial 14 bold', bg='green', fg='white').place(x=120, y=180)

def download():
    # Create a new thread to run the download function
    thread = threading.Thread(target=download_video)
    thread.start()

# Create A Download Button
Button(root, text="Download Now", font='Arial 16 bold', bg='red', padx=2, command=download).place(x=180, y=120)

root.mainloop()
