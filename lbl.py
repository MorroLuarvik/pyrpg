''' tk_put_pixel.py
place a pixel at pos=(x,y) with color="#rrggbb" on a Tkinter PhotoImage
image area

note:
one pixel might be hard to see, so create a series of pixels
to form a line or lines of different colors to form a rainbow ribbon
(dns)
'''

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


def putPixel(image, pos, color):
    """
    place a pixel at pos=(x,y) with color="#rrggbb" on an image area
    """
    x, y = pos
    image.put(color, (x, y))


root = tk.Tk()
#root.geometry("{}x{}+{}+{}".format(w, h, x, y))
root.geometry("{}x{}+{}+{}".format(300, 100, 70, 100))
root.title("PhotoImage.put(color, pos)")

# create a blank image area
w = 250
h = 50
photoImage = tk.PhotoImage(width=w, height=h)

# takes color in HTML hex format "#rrggbb"
# here are some examples ...
red = "#ff0000"
darkred = "#8b0000"
green = "#00ff00"
darkgreen = "#008000"
lightgreen = "#90ee90"
blue = "#0000ff"
navy = "#000080"
lightblue = "#add8e6"
plum = "#dda0dd"
purple = "#a020f0"
violet = "#ee82ee"
yellow = "#ffff00"
gold = "#ffd700"
orange = "#ffa500"
darkorange = "#ff8c00"
magenta = "#ff00ff"
brown = "#a52a2a"
black = "#000000"
white = "#ffffff"

# create a series of pixels on the image area
y = 16
for x in range(0, w):
    #print(x, y)  # test
    # draw lines to form a rainbow ribbon
    putPixel(photoImage, (x, y), darkred)
    putPixel(photoImage, (x, y+1), red)
    putPixel(photoImage, (x, y+2), darkorange)
    putPixel(photoImage, (x, y+3), orange)
    putPixel(photoImage, (x, y+4), gold)
    putPixel(photoImage, (x, y+5), yellow)
    putPixel(photoImage, (x, y+6), lightgreen)
    putPixel(photoImage, (x, y+7), green)
    putPixel(photoImage, (x, y+8), darkgreen)
    putPixel(photoImage, (x, y+9), lightblue)
    putPixel(photoImage, (x, y+10), blue)
    putPixel(photoImage, (x, y+11), navy)

label = tk.Label(root, image=photoImage)
label.grid(padx=10)

root.mainloop()