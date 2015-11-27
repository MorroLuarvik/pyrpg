import Tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.spritesheet = tk.PhotoImage(file="sprite.gif")
        self.num_sprintes = 4
        self.last_img = None
        self.images = [self.subimage(32*i, 0, 32*(i+1), 48) for i in range(self.num_sprintes)]
        self.canvas = tk.Canvas(self, width=100, height=100)
        self.canvas.pack()
        self.updateimage(0)

    def subimage(self, l, t, r, b):
        print(l,t,r,b)
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    def updateimage(self, sprite):
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(16, 24, image=self.images[sprite])
        self.after(100, self.updateimage, (sprite+1) % self.num_sprintes)

app = App()
app.mainloop()