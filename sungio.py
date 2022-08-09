import wave
import time
from io import BytesIO

class Sungio:
	def __init__(self, file):
		self.keypoints = []
		self.webs = []
		self.filePath=file
		self.waveFile = open(self.filePath, 'rb')  
		self.waveObj = wave.open(self.waveFile, 'rb')
		print(self.waveObj.getcomptype())
		self.getAverageAmplitudes(0, 1, 100)

	#Returns a list of the average value of bytes as a slice of the wave file
	def getAverageAmplitudes(self, start, end, resolution): 
		list = []
		self.waveObj.setpos(int(start*self.waveObj.getnframes()))

		scope = end - start  #Get thie size or scope in n frames of the portion of data to be displayed
		print("scope", scope)
		snipitSize = int((scope/resolution)*self.waveObj.getnframes())
		print("snipitSize", snipitSize)
		print(self.waveObj.getsampwidth())
		for i in range(resolution):
			bytes = self.waveObj.readframes(snipitSize)
			list.append((sum(bytes)/snipitSize)/(2**8))

		return list

