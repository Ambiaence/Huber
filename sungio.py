import wave
class Sungio:
	windows = []
	keypoints = []
	webs = []
	width = 1500

	fileRate = 41000
	def __init__(self, file):
		Sungio.filePath=file
		Sungio.data = wave.open(Sungio.filePath, 'rb')
		Sungio.channelNum = Sungio.data.getnchannels()
		Sungio.fileRate = Sungio.data.getframerate()
		Sungio.playRate = Sungio.fileRate # Maybe keep this in some sort of player object
		Sungio.frameNumber = Sungio.data.getnframes()
		Sungio.endFrame = Sungio.frameNumber


class Web(Sungio):
	def __init__(self, start=0, gap=Sungio.fileRate, rank=0):
		Sungio.webs.append(self)
		self.start = start
		self.gap = gap	
		self.rank = rank

	def setStart(self, start):
		self.start = start	
								
	def getNKeypoint(self, n): #Returns the frame location of a keypoint
		return self.start + self.gap * n  
	
	def moveKeypoints(n, offset): # See notes for equation
		interval = (n*self.gap + offset)/n
	
class Keypoint(Sungio): 
	def __init__(self, rank, pos):
		Sungio.keypoints.append(self)
		self.rank = rank
		self.pos = pos

class Window(Sungio):
	def __init__(self, parent = "Root"):
		Sungio.windows.append(self)

		if parent == "Root":
			self.parent = "Root"

			self.idealStart = 0.0
			self.frameStart = 0 

			self.idealEnd = 1.0
			self.frameEnd = (Sungio.endFrame//Sungio.width)*Sungio.width #Is always divisible by width
			self.degree = 0
		else:
			self.parent = parent
			self.start = parent.start
			self.end = self.parent.endFrame
			self.degree = parent.degree+1
	
	def makeChild(self):
		self.child = Window(self)
		return self.child
	
	def removeSelf(self):
		print("len", len(Sungio.windows), "degree", self.degree)
		for x in range(len(Sungio.windows)-1, self.degree-1, -1):
			del Sungio.windows[x]

	def setInterval(self, start, end): #start and end are fractions of the whole song			
		self.idealStart = start
		self.idealEnd = end
		self.step = int((((end - start)*Sungio.endFrame)//Sungio.width)) # (percentage of 
		self.frameStart = int(start*Sungio.endFrame)
		self.frameEnd = int(self.step*Sungio.width+self.frameStart) #This end might be useless or unhelpfull


	#for x in range(len(Sungio.windows)-1, self.degree-1, -1):

