#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *

class MainWindow:
	def __init__(self):
		self._createUI()
		
	def start(self):
		self.root.mainloop()
		
	def _createUI(self):
		self.root = Tk()
		self.root.title('Test application')
		self.root.geometry('600x400')
		
		self.firstRow = Frame(self.root)
		self.firstRow.pack(fill=X)

		self.withLabel = Label(self.firstRow, text='Width: ')
		self.withLabel.pack(side=LEFT)
		self.withLabelValue = Label(self.firstRow, text='xxx')
		self.withLabelValue.pack(side=LEFT)

		self.secondRow = Frame(self.root)
		self.secondRow.pack(fill=X)

		self.heightLabel = Label(self.secondRow, text='Height: ')
		self.heightLabel.pack(side=LEFT)
		self.heightLabelValue = Label(self.secondRow, text='yyy')
		self.heightLabelValue.pack(side=LEFT)
		
		self.actionButton = Button(self.root, text='Action!')
		self.actionButton.pack()

		self._setBindings()
		
	def _setBindings(self):
		self.root.bind('<Configure>', self._resizeApp)
		self.actionButton.bind('<Button-1>', self._click)

	def _resizeApp(self, event):
		self.withLabelValue.config(text=self.root.winfo_width())
		self.heightLabelValue.config(text=self.root.winfo_height())

	def _click(self, event):
		print('click event')

if __name__ == "__main__":
    mw = MainWindow()
    mw.start()

print("Bye!")
 
