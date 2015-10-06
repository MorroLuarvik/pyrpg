#!/usr/bin/python

from Tkinter import *

root = Tk()

root.title('Test application')
root.geometry('600x400')

withLabel = Label(text='Width:')
withLabel.pack()
heightLabel = Label(text='Height:')
heightLabel.pack()


root.mainloop()

print("Bye!")
