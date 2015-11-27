#from rnd import Rnd

class Particle:
	elems = []
	width = 192
	height = 192
	lifeTime = 10
	gravity = 1
	color = '#faa'
	
	def __init__(self, rnd):
		self.rnd = rnd
		self.color = '#{0:1X}{1:1X}{2:1X}'.format(
						6 + self.rnd.get(10), 
						6 + self.rnd.get(10), 
						6 + self.rnd.get(10))
		self.elems = []
		for cou in xrange(0, 1 + self.rnd.get(8)):
			self.elems.append(self.createElem())
	
	def animate(self, canvas = None):
		canvas.blank()
		for elem in self.elems:
			self.drawElement(canvas, elem)
			self.calcElement(elem)
	
	def drawElement(self, canvas, elem):
		canvas.put(
			self.color, 
			(	elem['x'], 
				elem['y'], 
				elem['x'] + elem['size'], 
				elem['y'] + elem['size']))
	
	def calcElement(self, elem):
		if (self.rnd.get(10) == 0):
			elem['size'] += 1
		
		elem['x'] += elem['xSpeed']
		elem['x'] = min(max(0, elem['x']), self.width - elem['size'])
		elem['y'] += elem['ySpeed'] + self.gravity * elem['lifeTime'] // 2
		elem['y'] = min(max(0, elem['y']), self.height - elem['size'])
		elem['lifeTime'] += 1
		if self.rnd.get(elem['dieProb']) == 0:
			for key, val in self.createElem().items():
				elem[key] = val
	
	def createElem(self):
		return {
			'xSpeed': 4 - self.rnd.get(9),
			'ySpeed': 4 - self.rnd.get(9),
			'x': self.width // 2 + 2 - self.rnd.get(5),
			'y': self.height // 2 - 24 - self.rnd.get(5),
			'size': 1 + self.rnd.get(4),
			'dieProb': 1 + self.rnd.get(10),
			'lifeTime': 0
		}
		
