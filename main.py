#External imports
from tkinter import *
import tkinter as tk 
import time
import statistics
from tkinter.filedialog import askopenfilename

import ffmpy
import os



# My stuff
import config #This is the standard way to share globals
from sungio import Sungio
from audio_overview import AudioOverview
from audio_workspace import AudioWorkspace
from navigation_frame import NavigationFrame

# defining open_file_chooser function

def openFile():
	filename = askopenfilename()
	print("You have selected : %s" % filename)
	try:
		os.remove("sungioTemp.wav")
	except:
		print("There was no leftover garbage from the last excecution")

	ff = ffmpy.FFmpeg(inputs={filename: None}, outputs={'sungioTemp.wav': None})
	ff.run();
	#Quck test
	startMenuFrame.pack_forget()
	config.sungio = Sungio('sungioTemp.wav')
	audioPhase()

def audioPhase(): #All frames are in column  except back and next buttons
	navigationFrame = NavigationFrame()
	audioOverview = AudioOverview()
	audioWorkpsace = AudioWorkspace()
#def restoreSungio(): # Too be continued
#	filename = askopenfilename()
#	print("You have selected : %s" % filename)
#	ff = ffmpy.FFmpeg(inputs={filename: ["-y"]}, outputs={'sungioTemp.wav': ["-y"]})
#	ff.run();


print(config.root)

config.root = tk.Tk()
config.root.title("Sungio")
config.root.configure(bg="#6A66A3")

startMenuFrame = Frame(config.root, bg = "#84A9c0");
startMenuFrame.pack(side=TOP)
new = tk.Button(startMenuFrame, text = "Open New Sungio From Audio File", command = openFile)
new.pack()

restore = tk.Button(startMenuFrame, text = "Restore Old Sungio From Project Files", command = openFile)
restore.pack()

# Starting the Application
config.root.mainloop()
