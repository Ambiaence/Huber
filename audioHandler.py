import pyaudio 
import wave
import time
import sys

#wave data

#Instance of pyaudio

class Player:
	def Player(file):
		waveDash = wave.open(file, 'rb') 
		podio = pyaudio.PyAudio()

	#Ripped from documentation
	def callback(in_data, frame_count, time_info, status):
		data = wf.readframes(frame_count)
		return (data, pyaudio.paContinue)
	
	def start


