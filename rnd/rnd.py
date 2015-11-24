class Rnd:
	a = 61211
	c = 56543
	seed = 0
	m = 65537#65521
	
	def __init__(self, seed = 0):
		self.seed = seed
	
	def get(self, max = None):
		self.seed = (self.a * self.seed + self.c) % self.m
		
		if not(max):
			return self.seed
		if max == 1:
			return 0
			
		return (self.seed * max + 1) // self.m
