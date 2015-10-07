#!/usr/bin/python

from Tkinter import *

def resizeApp(event):
	click(click)
	#print('resizeApp')

root = Tk()
root.title('Test application')
root.geometry('600x400')
root.bind('<Configure>', resizeApp)


firstRow = Frame(root)
firstRow.pack(fill=X)

withLabel = Label(firstRow, text='Width: ')
withLabel.pack(side=LEFT)
withLabelValue = Label(firstRow, text='xxx')
withLabelValue.pack(side=LEFT)

secondRow = Frame(root)
secondRow.pack(fill=X)

heightLabel = Label(secondRow, text='Height: ')
heightLabel.pack(side=LEFT)
heightLabelValue = Label(secondRow, text='yyy')
heightLabelValue.pack(side=LEFT)

def click(event):
	withLabelValue.config(text=root.winfo_width())
	heightLabelValue.config(text=root.winfo_height())
	#print('Action button is clicked')
	#print(event)

actionButton = Button(root, text='Action!')
actionButton.bind('<Button-1>', click)
actionButton.pack()

root.mainloop()

print("Bye!")
 
