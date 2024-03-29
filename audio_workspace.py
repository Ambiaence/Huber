import config 
import tkinter as tk

class AudioWorkspace:
	def __init__(self, root, sungio):
		self.root = root
		self.sungio = sungio
		self.audioWindowsFrame = tk.Frame(self.root, bg= config.colorOne, height = 855, width = 1920)
		self.audioWindowsFrame.grid(column=0, row=1, sticky = 'e')

		self.globalButtonsFrame = tk.Frame(self.root, bg= "#B3CBC9", height = 75, width = 1920)
		self.globalButtonsFrame.grid(column=0, row=2, sticky = 'e')
		self.pack
		self.action = "place"
		self.windows = []
		self.markers = []
		self.highestWindowIndex = 0;

		self.windows.append(Window(sungio = self.sungio, workspace = self))
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
			self.action = "move"
			self.actionText.set("Move")
		elif(self.action == "move"):
			print("move")
			self.action = "place"
			self.actionText.set("Place")
	
	def addWindow(self):
		if self.highestWindowIndex < 3:
			self.windows.append(Window(workspace = self, order = self.highestWindowIndex+1, start = self.windows[self.highestWindowIndex].openMarker.pos, end = self.windows[self.highestWindowIndex].closeMarker.pos, sungio = self.sungio))
			self.highestWindowIndex = self.highestWindowIndex + 1;

			for keypoint in self.windows[self.highestWindowIndex-1].keypoints:
				if keypoint.pos > self.windows[self.highestWindowIndex].start and keypoint.pos < self.windows[self.highestWindowIndex].end:
					self.windows[self.highestWindowIndex].keypoints.append(keypoint)
					print(self.highestWindowIndex, "Has a new keypoint")

			self.render()
	
	def killWindow(self):
		if self.highestWindowIndex != 0: # Always have at least one window open
			self.windows[self.highestWindowIndex].frame.destroy()
			self.windows.pop(-1)
			self.highestWindowIndex = self.highestWindowIndex - 1;

	def render(self): #Draw everything
		for window in self.windows: #Draw background
			window.visual.canvas.create_rectangle(0, 0, config.audioCanvasWidth, config.audioCanvasHeight, fill = config.audioCanvasColor)	

		for window in self.windows:
			amplitudes = self.sungio.getAverageAmplitudes(window.start, window.end, config.audioCanvasWidth)
			for pos in range(config.audioCanvasWidth - 1):
				window.visual.drawAmplitude(pos, amplitudes[pos], "black")

		for mark in self.sungio.keypoints: 
			for window in self.windows:
				window.visual.refresh();
				if mark.pos > window.start and mark.pos < window.end:
					if mark.meaning == "switch":
						window.visual.drawMark((mark.pos - window.start)/(window.end - window.start) * config.audioCanvasWidth, "blue")

		for window in self.windows:
				window.visual.drawMark((window.openMarker.pos - window.start)/(window.end - window.start) * config.audioCanvasWidth, "red")
				window.visual.drawMark((window.closeMarker.pos - window.start)/(window.end - window.start) * config.audioCanvasWidth, "red")

	def newMarker(self): #Makes sure that windows have an accurate record of the markers within
		newestMark = self.sungio.keypoints[-1]
		for window in self.windows:
			if newestMark.pos > window.start and newestMark.pos < window.end:
				window.keypoints.append(newestMark)
				self.render()
				print("Window #", window.order, "contains newest mark")
				
				
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
		self.movePoint = "empty"
		self.sungio = sungio
		self.workspace = workspace
		self.keypoints = []
		self.start = start
		self.end = end
		self.order = order


		self.frame = tk.Frame(self.workspace.audioWindowsFrame, bg = "#B3CBC0", height = 213, width = 1900);
		self.frame.grid(column=0, row = order)

		self.buttonFrame = tk.Frame(self.frame, height =213, bg = "#B3CBC9", width = 213)
		self.buttonFrame.grid(row = 0, column = 0)
		self.play = tk.Button(self.buttonFrame, text = "play", command = lambda: self.playSong())
		self.play.pack()

		self.visual = Visual(self.frame)

		self.visual.canvas.bind('<Button-1>', self.pressMouseLeft)
		self.visual.canvas.bind('<ButtonRelease-1>', self.releaseMouseLeft)

		self.containedMarks = []
		self.openMarker = Marker(start + (end - start)*.01, "open", "NA")
		self.closeMarker = Marker(end - (end - start)*.01, "close", "NA")

	def playSong(self):
		self.sungio.playFromHereToThere(self.openMarker.pos, self.closeMarker.pos)
	
	def doesHandleContainMousePos(self, x, y, pos):
		north = config.audioCanvasHeight - 21; # This is the box that is a keypoint
		south = config.audioCanvasHeight;
		east = (pos - self.start)/(self.end - self.start) * config.audioCanvasWidth + 10
		west = (pos - self.start)/(self.end - self.start) * config.audioCanvasWidth - 10

		if y > north and y < south and x > west and x < east:
			return True
		else:
			return False

	def fractionToFrame(self, time = 1): #takes a point in time of a song as the fraction of the whole song and returns closest frame to that ideal pint.
		return int(self.sungio.totalFrames*time)

	def pressMouseLeft(self, event):
		fPos = self.start + (event.x/config.audioCanvasWidth) * (self.end - self.start) # Floating point poisition
		if self.workspace.action == "place":		
			self.sungio.keypoints.append(Marker(fPos, "switch", rank = 1))
			self.workspace.newMarker()
		if self.workspace.action == "move":		
			for mark in self.keypoints:
				if self.doesHandleContainMousePos(event.x, event.y, mark.pos):
					print("Point ", mark.pos, "Clicked")
					self.movePoint = mark

			if self.doesHandleContainMousePos(event.x, event.y, self.openMarker.pos):
					self.movePoint = self.openMarker

			if self.doesHandleContainMousePos(event.x, event.y, self.closeMarker.pos):
					self.movePoint = self.closeMarker
				

	def releaseMouseLeft(self, event):
		fPos = self.start + (event.x/config.audioCanvasWidth) * (self.end - self.start) # Floating point poisition
		print(self.movePoint)
		if self.workspace.action == "move" and  self.movePoint != "empty":
			self.movePoint.pos = fPos
			self.movePoint = "empty"
			self.workspace.render()
		
class Visual:
	def __init__(self, frame):
		self.frame = tk.Frame(frame, height =213, bg = "#B3CBC9", width = 213)
		self.canvas = tk.Canvas(frame, height = config.audioCanvasHeight, bg = "#DDD8B8", width = config.audioCanvasWidth)
		self.canvas.grid(row = 0, column = 1)
		 
	
	def drawAmplitude(self, pos, amp, color):
		self.canvas.create_line(pos, 0, pos, config.audioCanvasHeight*amp, fill = color)
	
	def drawMark(self, pos, color):
		self.canvas.create_line(pos, 0, pos, config.audioCanvasHeight, fill = color)
		self.canvas.create_rectangle(pos-10, config.audioCanvasHeight - 21, pos+10, config.audioCanvasHeight, fill = color)	
	
	def refresh(self):
		self.canvas.create_rectangle(0, config.audioCanvasHeight - 21, 0, config.audioCanvasHeight, fill = config.audioCanvasColor)	
