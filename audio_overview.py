import tkinter as tk

class AudioOverview:
	def __init__(self, root):
		self.__root = root
		self.frame = tk.Frame(self.__root, bg= "#84A9C0", height = 75, width = 1920, pady = 7)
		self.frame.grid(column=0, row=0)
		self.pack
	
	def pack(self):
		self.frame.pack()
	
	def unPack(self):
		self.frame.pack_forget()

	def redraw(self):
		print("redraw")

	
		
