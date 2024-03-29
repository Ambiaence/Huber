import wave
import math
import pyaudio
import time
import simpleaudio
import pydub
import threading

from io import BytesIO

class Sungio:
	def __init__(self, file):
		self.chunk = 1024
		self.keypoints = []
		self.webs = []
		self.filePath=file
		self.waveFile = open(self.filePath, 'rb')  
		self.waveObj = wave.open(self.waveFile, 'rb')
		print(self.waveObj.getcomptype())

		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(
			format = self.p.get_format_from_width(self.waveObj.getsampwidth()),
			channels = self.waveObj.getnchannels(),
			rate = self.waveObj.getframerate(),
			output = True
			)
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
	
	def playFromHereToThere(self, start, end):
		self.thread =  threading.Thread(target = self.play, args=(start, end))
		self.thread.start()

	def play(self,start,end):
		self.waveObj.setpos(int(start * self.waveObj.getnframes()))
		nChunks = int((self.waveObj.getnframes()*(end-start))/self.chunk)
		chunksToPlay = []

		for mark in self.keypoints:
			if mark.pos > start and mark.pos < end: #Is the pos relavant to this frame? 
				chunksToPlay.append(int((mark.pos - start)/(end-start) * nChunks)) #find the chunk the point occupies

		data = self.waveObj.readframes(self.chunk)
		print(chunksToPlay)
			
		for n in range(nChunks):
			modData = []
			if n in chunksToPlay:
				for x in range(len(data)):
					modData.append(int((data[x] + (math.sin(x/2) + 1)*20)/2))
			else:
				self.stream.write(data)

			data = self.waveObj.readframes(self.chunk)
			
	def close(self):
		self.stream.close()
		self.p.terminate()
