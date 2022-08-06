import wave
import time
from io import BytesIO

class Sungio:
	def __init__(self, file):
		self.keypoints = []
		self.webs = []
		self.filePath=file
		self.waveDisk = open(self.filePath, 'rb')  
		self.waveMemory = BytesIO(self.waveDisk.read())
		self.waveDisk.seek(0)
		self.waveMemory.seek(0)
		self.waveObjFromDisk = wave.open(self.waveDisk, 'rb')
		self.waveObjFromMem = wave.open(self.waveMemory, 'rb')
		if  self.waveMemory.read() == self.waveDisk.read():
			print("Works")

		self.waveObjFromDisk.setpos(0)
		self.waveObjFromMem.setpos(0)
		start = time.time_ns()
		sum = 0 
		for i in range(self.waveObjFromDisk.getnframes() // 1000):
			self.bytes = self.waveObjFromDisk.readframes(1000)
			for y in self.bytes:
				sum = sum+y

			sum = 0

		print(time.time_ns() - start)
		input()
			
		sum = 0 
		start = time.time_ns()
		for i in range(self.waveObjFromMem.getnframes() // 1000):
			self.bytes = self.waveObjFromMem.readframes(1000)
			for y in self.bytes:
				sum = sum+y

			sum = 0
				
		print(time.time_ns() - start)
