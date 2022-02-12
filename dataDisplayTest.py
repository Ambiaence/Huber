from tkinter import *
import time 
from tkinter import ttk
import statistics

width = 1500
height = 125

import sungio
Sungio = sungio.Sungio

#portion = portion 150
#255 = = 150	255

#def drawMap(event)

#def savePosn():
#	global inst
#	step = Sungio.frameNumber//width
#	
#	#print("yup")
#	#deck.create_line(750, 0, 750, 9, width = 3, fill = "red")
#
#	for i in range(0, width):
#		mean = statistics.mean(Sungio.data.readframes(step))
#		meanM = mean*(height/255)
#		print(int(meanM)+1)
##		deck.create_line(i, height -  int(meanM)+1, i, height-1, fill = "red", width = 1)

keypointLocation = 0.005

def drawWindow(sungioWindow):
	sampleWidth = 2**(4*sungioWindow.data.getsampwidth())
	#print(sampleWidth)
	sungioWindow.data.setpos(sungioWindow.frameStart)
	for i in range(0, sungioWindow.width):
		mean = statistics.mean(sungioWindow.data.readframes(sungioWindow.step))
		meanM = mean*(height/sampleWidth)
		#print(int(meanM)+1)
		deck.create_line(i, height -  int(meanM)+1, i, height-1, fill = "red", width = 1)
	
def drawKeypoint():
	if keypointLocation < mainWindow.idealEnd and keypointLocation > mainWindow.idealStart
		print(spot)
		deck.create_line(spot, 0, spot, 125)

#Tkinter Setup
canvasColumn = 3

inst = Sungio("test.wav")
mainWindow = sungio.Window()
	
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)

frame1 = Frame(root)
frame1.grid(column = 0, row=0)

openInterval = Entry(frame1)
openInterval.grid(column = 0, row = 1)

play = Button(frame1, text = "Play")
play.grid(column = 0,row =0)

push = Button(frame1, text = "Push")
push.grid(column = 1,row =0)

keypoint = Button(frame1, text = "Keypoint", command = drawKeypoint)
keypoint.grid(column = 2,row =0)

subWindow = Button(frame1, text = "Pull")
subWindow.grid(column = 3, row =0)

deck = Canvas(root, bd = 4,height= 125, width=1500,relief = "ridge")
deck.grid(column=canvasColumn, row=0, sticky=(N))
deck.create_rectangle(0, 0, 1500, 125, fill = "#fff")

ledge = Canvas(root, height= 125, width=1500)
ledge.grid(column=canvasColumn, row=1, sticky=(N))
ledge.create_rectangle(0, 0, 1500, 125, fill = "#fff")

mainWindow.setInterval(0.0, 0.01)
print(keypointLocation)
drawWindow(mainWindow)

root.mainloop()

