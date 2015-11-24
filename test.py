#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from rnd import Rnd

#global img

class MainWindow:
	def __init__(self):
		self._createUI()
		self.rnd = Rnd()
		
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

		self.heightLabel = tk.Label(self.secondRow, text='Height: ')
		self.heightLabel.pack(side=tk.LEFT)
		self.heightLabelValue = tk.Label(self.secondRow, text='yyy')
		self.heightLabelValue.pack(side=tk.LEFT)
		
		self.actionButton = tk.Button(self.root, text='Action!')
		self.actionButton.pack()

		self.bgg = '#fff';
		
		self.canvas = tk.Canvas(self.root, bg=self.bgg) #, bg=self.bgg
		self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
		
		self.img = tk.PhotoImage() #width=800, height=600
		#self.img.blank()

		self.canvas.create_image(0, 0, image=self.img, anchor='nw')  # , state="normal", anchor='nw'
		
		self._setBindings()
		
	def _setBindings(self):
		self.root.bind('<Configure>', self._resizeApp)
		self.actionButton.bind('<Button-1>', self._click)

	def _resizeApp(self, event):
		self.withLabelValue.config(text=self.canvas.winfo_width())
		self.heightLabelValue.config(text=self.canvas.winfo_height())

	def plotPixel(self, img, x, y, color, size = 3):
		for sy in xrange(0, size):
			img.put('{' + (color + ' ') * size + '}', (x, y+sy))
		
	def _click(self, event):
		for cou in xrange(0, 100):
			size = self.rnd.get(32) + 1
			self.plotPixel(
				self.img, 
				self.rnd.get(self.canvas.winfo_width() - size), 
				self.rnd.get(self.canvas.winfo_height() - size), 
				'#{0:1X}{1:1X}{2:1X}'.format(
					self.rnd.get(16), 
					self.rnd.get(16), 
					self.rnd.get(16)), 
				size)
		

if __name__ == "__main__":
    mw = MainWindow()
    mw.start()

print("Bye!")
 
