import tkinter as tk

import config

class NavigationFrame:
	def __init__(self):
		print(config.root)
		self.bugs = []
		self.frame = tk.Frame(config.root, bg= "#84A9C0", height = 75, width = 1920, pady = 7)
		self.frame.grid(column=0, row=2)
		self.pack
	
	def pack(self):
		self.frame.pack()
	
	def unPack(self):
		self.frame.pack_forget()

	def redraw(self):
		print("redraw")

	
		
