#!/usr/bin/python

from Tkinter import *

root = Tk()

root.title('Test application')
root.geometry('600x400')

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


root.mainloop()

print("Bye!")
 
