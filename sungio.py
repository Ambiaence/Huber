import wave

class Sungio:
	def __init__(self, file):
		self.windows = []
		self.keypoints = []
		self.webs = []
		self.filePath=file
		self.data = wave.open(self.filePath, 'rb')  
		self.totalFrames = self.data.getnframes()
