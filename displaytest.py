fom tkinter import *
from tkinter import ttk

def savePosn(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y
	print("Save:lastx", lastx)
	print("Save:lasty", lasty)

	def addLine(event):
	canvas.create_line((lastx, lasty, event.x, event.y))
	savePosn(event)
	print("Add:Lastx", lastx)
	print("Add:Lasty", lasty)

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))


root.mainloop()
