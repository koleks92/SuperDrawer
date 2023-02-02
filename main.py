'''SuperDrawer main file'''
from tkinter import *
import tkinter as tk

class Drawer():
    def __init__(self, root):
        root.geometry('1200x800')
        root.title('SuperDrawer')

        self.root = root


    def sketchpad(self):
        canvas = Canvas(self.root, bg='grey', width=1100, height=800)
        canvas.pack(side=RIGHT)
        canvas.bind("<Button-1>", self.save_position)
        canvas.bind("<B1-Motion>", self.add_line)

        self.canvas = canvas
        self.paint_size = 10
        self.paint_color = "blue"

        
    def save_position(self, event):
        self.lastx = event.x
        self.lasty = event.y

    def add_line(self, event):
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y,width=self.paint_size, fill=self.paint_color)
        self.save_position(event)





def main():
    # Initiate tkinkter engine
    root = Tk()
    # Initiate drawer class
    drawer = Drawer(root)

    drawer.sketchpad()

    # Loop for window
    root.mainloop()



    


if __name__ == "__main__":
    main()