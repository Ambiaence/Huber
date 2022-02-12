import pyaudio 
import wave
import time
import sys

#wave data

#Instance of pyaudio

#27.27.21 19: Audio stuff is mostly ripped from documentation and is basically just wrapped the way I want it. until I realize how far I can push the library, I am thinking that certain implementations of this class will be slow so they are subject to change. Also seeing as how there are an indefinite number of ways to implement the visuals I think I should keep it uninvolved for now.

class Player:
	def __init__(self, file):
		self.file = file
		self.waveDash = wave.open(file, 'rb') 
		self.podio = pyaudio.PyAudio()

		self.stream = self.podio.open(format=self.podio.get_format_from_width(self.waveDash.getsampwidth()),
                channels=self.waveDash.getnchannels(),
                rate=self.waveDash.getframerate(),
                output=True,
                stream_callback=self.callback)

	#Ripped from documentation
	def callback(self, in_data, frame_count, time_info, status):
		data = self.waveDash.readframes(frame_count)
		return (data, pyaudio.paContinue)

	#Starts stream
	def start():
		self.stream.start_stream()

	def stop():
		self.stream.stop_stream()

	def kill(): 
		self.stream.quit_stream()

	def murk(): #Get you a man who does both
		self.stream.stop_stream()
		self.stream.quit_steam()
	
	def jumpTo(self, frame):
		self.waveDash.setpos(frame)

		
		

	
							

