class Rnd:
	a = 56543 #99839 #61211 #699649
	c = 99881 #99881 #56543 #699527
	seed = 0
	m = 700001 #100003 #65537
	
	def __init__(self, seed = 0):
		self.seed = seed
	
	def get(self, max = None):
		self.seed = (self.a * self.seed + self.c) % self.m
		
		if not(max):
			return self.seed
		if max == 1:
			return 0
			
		return (self.seed * max + 1) // self.m
