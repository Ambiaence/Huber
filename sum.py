class Summation:
	def __init__(self):	
		self.avg = 0
		self.n = 0
		
	def add(self,  z):
		self.n = self.n + 1
		self.avg = self.avg + (1/self.n)*(z - self.avg) 
		
