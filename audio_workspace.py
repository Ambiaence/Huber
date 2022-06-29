import config 
import tkinter as tk

class AudioWorkspace:
	def __init__(self, root, sungio):
		self.__root = root
		self.__sungio = sungio
		self.audioWindowsFrame = tk.Frame(self.__root, bg= config.colorOne, height = 855, width = 1920)
		self.audioWindowsFrame.grid(column=0, row=1, sticky = 'e')
		self.globalButtonsFrame = tk.Frame(self.__root, bg= "#B3CBC9", height = 75, width = 1920)
		self.globalButtonsFrame.grid(column=0, row=2, sticky = 'e')
		self.pack
		self.action = "place"
		self.windows = []
		self.markers = []
		self.highestWindowIndex = 0;
		self.windows.append(Window(sungio = self.__sungio, workspace = self))
		self.new = tk.Button(self.globalButtonsFrame, text = "Add", command = lambda: self.addWindow())
		self.new.pack()
		self.old = tk.Button(self.globalButtonsFrame, text = "Kill", command = lambda: self.killWindow())
		self.old.pack()
		self.actionText = tk.StringVar()
		self.actionButton = tk.Button(self.globalButtonsFrame, textvariable = self.actionText, command = lambda: self.actionButtonFunc())
		self.actionText.set("Place")
		self.actionButton.pack()

	def pack(self):
		self.audioWindowsFrame.pack()
		self.globalButtonsFrame.pack()

	def redraw(self):
		print("redraw")

	def actionButtonFunc(self):
		if(self.action == "place"):
			print("place")
			self.action = "remove"
			self.actionText.set("Remove")
		elif(self.action == "remove"):
			print("remove")
			self.action = "place"
			self.actionText.set("Place")
	
	def addWindow(self):
		if self.highestWindowIndex < 3:
			self.windows.append(Window(workspace = self, order = self.highestWindowIndex+1, start = self.windows[self.highestWindowIndex].start, end = self.windows[self.highestWindowIndex].end, sungio = self.__sungio))
			self.highestWindowIndex = self.highestWindowIndex + 1;
	
	def killWindow(self):
		if self.highestWindowIndex != 0: # Always have at least one window open
			self.windows[self.highestWindowIndex].frame.destroy()
			self.windows.pop(-1)
			self.highestWindowIndex = self.highestWindowIndex - 1;

	def render(self):
		for mark in self.__sungio.keypoints: 
			for window in self.windows:
				if mark.pos > window.start and mark.pos < window.end:
					if mark.meaning == "switch":
						window.visual.drawMark((mark.pos - window.start)/(window.end - window.start) * config.audioCanvasWidth, "blue")
				
class Marker:
	def __init__(self, pos, meaning, rank):
		self.pos = pos 
		self.meaning = meaning
		self.rank = rank

	def print(self):
		print(self.pos)
		print(self.meaning)
		
class Window:
	def __init__(self, workspace, sungio, order=0, start = 0, end=1): 
		self.__sungio = sungio
		self.__workspace = workspace
		self.start = start
		self.end = end
		self.order = order
		self.frame = tk.Frame(self.__workspace.audioWindowsFrame, bg = "#B3CBC0", height = 213, width = 1900);
		self.frame.grid(column=0, row = order)
		self.visual = Visual(self.frame)
		self.visual.canvas.bind('<Button-1>', self.pressMouseLeft)
		self.visual.canvas.bind('<ButtonRelease-1>', self.releaseMouseLeft)
		self.openMarker = 0.0
		self.closeMarker = 1.0

	def fractionToFrame(self, time = 1): #takes a point in time of a song as the fraction of the whole song and returns closest frame to that ideal pint.
		return int(self.__sungio.totalFrames*time)

	def pressMouseLeft(self, event):
		print(event.x, event.y, "P:order:", self.order)
		if self.__workspace.action == "place":		
			self.__sungio.keypoints.append(Marker(self.start + (event.x/config.audioCanvasWidth) * (self.end - self.start), "switch", rank = 1))
			self.__sungio.keypoints[-1].print()
			self.__workspace.render()

	def releaseMouseLeft(self, event):
		print(event.x, event.y, "R:order:", self.order)
		
class Visual:
	def __init__(self, frame):
		self.buttonFrame = tk.Frame(frame, height =213, bg = "#B3CBC9", width = 213)
		self.frame = tk.Frame(frame, height =213, bg = "#B3CBC9", width = 213)
		self.canvas = tk.Canvas(frame, height = config.audioCanvasHeight, bg = "#DDD8B8", width = config.audioCanvasWidth)
		self.canvas.grid(row = 0, column = 1)
		self.buttonFrame.grid(row = 0, column = 0)
	
	def drawMark(self, pos, color):
		self.canvas.create_line(pos, 0, pos, config.audioCanvasHeight, fill = color)
		self.canvas.create_rectangle(pos-10, config.audioCanvasHeight - 21, pos+10, config.audioCanvasHeight, fill = color)	
