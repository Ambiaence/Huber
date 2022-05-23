import config 
import tkinter as tk
class AudioWorkspace:
	def __init__(self):
		self.audioWindowsFrame = tk.Frame(config.root, bg= "#DDD8B8", height = 855, width = 1920)
		self.audioWindowsFrame.grid(column=0, row=1, sticky = 'e')
		self.globalButtonsFrame = tk.Frame(config.root, bg= "#B3CBC9", height = 75, width = 1920)
		self.globalButtonsFrame.grid(column=0, row=2, sticky = 'e')
		self.pack
		self.windows = []
		self.highestWindowIndex = 0;
		self.windows.append(Window(self))

		new = tk.Button(self.globalButtonsFrame, text = "Add", command = lambda: self.addWindow())
		new.pack()
		old = tk.Button(self.globalButtonsFrame, text = "Kill", command = lambda: self.killWindow())
		old.pack()
	
	def pack(self):
		self.audioWindowsFrame.pack()
		self.globalButtonsFrame.pack()

	def redraw(self):
		print("redraw")
	
	def addWindow(self):
		if self.highestWindowIndex < 3:
			self.windows.append(Window(self, order = self.highestWindowIndex+1, start = self.windows[self.highestWindowIndex].start, end = self.windows[self.highestWindowIndex].end))
			self.highestWindowIndex = self.highestWindowIndex + 1;
	
	def killWindow(self):
		if self.highestWindowIndex != 0: # Always have at least one window open
			self.windows[self.highestWindowIndex].frame.destroy()
			self.windows.pop(-1)
			self.highestWindowIndex = self.highestWindowIndex - 1;
		
		
class Window:
	def __init__(self, workspace, order=0, start = 0, end=0): 
		self.workspace = workspace
		self.start = start
		self.end = end
		self.order = order
		self.frame = tk.Frame(workspace.audioWindowsFrame,  bg = "#B3CBC0", height = 213, width = 1900);
		self.frame.grid(column=0, row = order)
		self.visual = Visual(self.frame)
		self.visual.canvas.bind('<Button-1>', self.pressMouseLeft)
		self.visual.canvas.bind('<ButtonRelease-1>', self.releaseMouseLeft)



	def fractionToFrame(self, time = 1): #takes a point in time of a song as the fraction of the whole song and returns closest frame to that ideal pint.
		return int(config.sungio.totalFrames*time)

	def pressMouseLeft(self, event):
		print(event.x, event.y, "P:order:", self.order)

	def releaseMouseLeft(self, event):
		print(event.x, event.y, "R:order:", self.order)

class Visual:
	def __init__(self, frame):
		self.buttonFrame = tk.Frame(frame, height =213, bg = "#B3CBC9", width = 213)
		self.canvas = tk.Canvas(frame, height = 213, bg = "#DDD8B8", width = "1717")
		self.canvas.grid(row = 0, column = 1)
		self.buttonFrame.grid(row = 0, column = 0)
