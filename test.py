#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from time import time
from rnd import Rnd
from particle import Particle

#global img

class MainWindow:
	def __init__(self):
		self._createUI()
		self.paused = True
		self.rnd = Rnd()
		self.frameTime = 40
		
		self.part = None
		self.particleImgId = None
			
	def start(self):
		self.root.mainloop()
		
	def _createUI(self):
		self.root = tk.Tk()
		self.root.title('Test application')
		self.root.geometry('600x400')
		
		self.firstRow = tk.Frame(self.root)
		self.firstRow.pack(fill=tk.X)

		self.withLabel = tk.Label(self.firstRow, text='Width: ')
		self.withLabel.pack(side=tk.LEFT)
		self.withLabelValue = tk.Label(self.firstRow, text='xxx')
		self.withLabelValue.pack(side=tk.LEFT)

		self.secondRow = tk.Frame(self.root)
		self.secondRow.pack(fill=tk.X)
		
		self.thirdRow = tk.Frame(self.root)
		self.thirdRow.pack(fill=tk.X)

		self.heightLabel = tk.Label(self.secondRow, text='Height: ')
		self.heightLabel.pack(side=tk.LEFT)
		self.heightLabelValue = tk.Label(self.secondRow, text='yyy')
		self.heightLabelValue.pack(side=tk.LEFT)
		
		self.speedLabelValue = tk.Label(self.secondRow, text='speed')
		self.speedLabelValue.pack(side=tk.LEFT)
		
		self.actionButton = tk.Button(self.thirdRow, text='Animate', width=10)
		self.actionButton.pack(side=tk.LEFT)
		
		self.spaceLabel = tk.Label(self.thirdRow, text='   ')
		self.spaceLabel.pack(side=tk.LEFT)
		
		self.otherButton = tk.Button(self.thirdRow, text='other', width=10, padx=10)
		self.otherButton.pack(side=tk.LEFT)

		self.bgg = '#111';
		
		self.canvas = tk.Canvas(self.root, bg=self.bgg) #, bg=self.bgg
		self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
		
		self.img = tk.PhotoImage() #width=800, height=600
		#self.img.blank()

		self.canvas.create_image(0, 0, image=self.img, anchor='nw')  # , state="normal", anchor='nw'
		
		self._setBindings()
		
		self.root.after(1000, self.animate)
		
	def animate(self):
		startTime = time()
		if not(self.paused):
			for cou in xrange(0, 20):
				size = self.rnd.get(32)
				self.plotPixel(
					self.img, 
					self.rnd.get(self.canvas.winfo_width() - size), 
					self.rnd.get(self.canvas.winfo_height() - size), 
					'#{0:1X}{1:1X}{2:1X}'.format(
						self.rnd.get(10), 
						self.rnd.get(10), 
						self.rnd.get(10)), 
					size)
		
		if self.part: 
			self.part.animate(self.particleImg)
			#print(self.part.elems)
		
				
		execTime = int((time() - startTime) * 1000)
		if execTime:
			speed = 1000 // execTime
		else:
			speed = 'inf'
		self.speedLabelValue.config(text=speed)
		#frameTime = 40
		waiting = max(1, self.frameTime - execTime)
		self.root.after(waiting, self.animate)
		
	def _setBindings(self):
		self.root.bind('<Configure>', self._resizeApp)
		self.actionButton.bind('<Button-1>', self._click)
		self.otherButton.bind('<Button-1>', self._otherAction)

	def _resizeApp(self, event):
		self.withLabelValue.config(text=self.canvas.winfo_width())
		self.heightLabelValue.config(text=self.canvas.winfo_height())

	def plotPixel(self, img, x, y, color, size = 3):
		img.put(color, (x, y, x+size, y+size))
		#for sy in xrange(0, size):
			#img.put('{' + (color + ' ') * size + '}', (x, y+sy))
		
	def _click(self, event):
		self.paused = not(self.paused)
		if self.paused:
			self.actionButton.config(text='Animate')
		else:
			self.actionButton.config(text='Pause')

	def _otherAction(self, event):
		#self.otherImg = tk.PhotoImage(file='mark')
		#self.otherImg = tk.PhotoImage(width=16, height=16)
		
		#self.otherImg.put('#f11', (0, 0, 7, 7))
		#self.otherImg.put('#111', (1, 1, 6, 6))
		#self.otherImg.put('#11f', (8, 8, 16, 16))
		
		#self.canvas.create_image(100, 100, image=self.otherImg, anchor='nw')  # , state="normal", anchor='nw'
		
		#self.otherImg.write('mark')
		
		#print(self.otherImg)
		
		self.part = Particle(self.rnd)
		self.particleImg = tk.PhotoImage(width=192, height=192)
		
		if (self.particleImgId):
			self.canvas.delete(self.particleImgId)
			
		self.particleImgId = self.canvas.create_image(100, self.canvas.winfo_height()-self.particleImg.height(), image=self.particleImg, anchor='nw')
		
		#print(self.part.elems)
		print('created: {}'.format(self.particleImgId))
		print(self.canvas.find_all())
		print('_otherAction')
		#self.otherImg.blank()
			
if __name__ == "__main__":
    mw = MainWindow()
    mw.start()

print("Bye!")
 
