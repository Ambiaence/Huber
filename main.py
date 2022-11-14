#External imports
from tkinter import *
import tkinter as tk 
import time
import statistics
from tkinter.filedialog import askopenfilename

import ffmpy
import os
import platform

import config #This is the standard way to share globals
from sungio import Sungio
from audio_overview import AudioOverview
from audio_workspace import AudioWorkspace
from navigation_frame import NavigationFrame

def openFile():
    filename = askopenfilename()
    print("You have selected : %s" % filename)
    try:
        os.remove("sungioTemp.wav") 	
    except:
        print("There was no leftover garbage from the last excecution")
    opsys = platform.system()
    print(opsys)
    if opsys == "Windows":
        print("Using Windows")
        ff = ffmpy.FFmpeg(executable = "ffmpeg/ffmpeg.exe", inputs={filename: None}, outputs={'sungioTemp.wav': '-acodec pcm_u8 -ac 1'})
        input()
    elif opsys == "Linux":
        print("Using Linux")
        ff = ffmpy.FFmpeg(inputs={filename: None}, outputs={'sungioTemp.wav': '-acodec pcm_u8 -ac 1'})

    #Quck test
    startMenuFrame.pack_forget()
    config.sungio = Sungio('sungioTemp.wav')
    audioPhase()

def audioPhase(): #All frames are in column  except back and next buttons
	navigationFrame = NavigationFrame(config.root)
	audioOverview = AudioOverview(config.root)
	audioWorkpspace = AudioWorkspace(root = config.root, sungio = config.sungio)

config.root = tk.Tk()
config.root.title("Huber")
config.root.configure(bg="#6A66A3")
print("Test")

startMenuFrame = Frame(config.root, bg = "#84A9c0");
startMenuFrame.pack(side=TOP)
new = tk.Button(startMenuFrame, text = "Open New Sungio From Audio File", command = openFile)

restore = tk.Button(startMenuFrame, text = "Restore Old Sungio From Project Files", command = openFile)
restore.pack()

# Starting the Application
config.root.mainloop()
