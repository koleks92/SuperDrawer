'''SuperDrawer main file'''
from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter as tk
import functions


class Drawer():
    def __init__(self, root):
        root.geometry('1200x800')
        root.title('SuperDrawer')

        self.root = root

    def tools_menu(self):
        tool_frame = Frame(self.root, width=100, height=800, bg='grey')
        tool_frame.pack(side=LEFT)
        
        self.paint_color = "blue"
        color_button = Button(tool_frame, bg = self.paint_color,width=10,height=5, command=lambda: functions.color_changer(paint_color))
        color_button.pack()
        print(paint_color)


    def sketchpad(self):
        canvas = Canvas(self.root, bg='white', width=1100, height=800)
        canvas.pack(side=RIGHT)
        canvas.bind("<Button-1>", self.save_position)
        canvas.bind("<B1-Motion>", self.add_line)

        self.canvas = canvas
        self.paint_size = 10

    # Mouse position       
    def save_position(self, event):
        self.lastx = event.x
        self.lasty = event.y
    # Drawing a line
    def add_line(self, event):
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y,width=self.paint_size, fill=self.paint_color)
        self.save_position(event)





def main():
    # Initiate tkinkter engine
    root = Tk()
    # Initiate drawer class
    drawer = Drawer(root)

    drawer.sketchpad()

    drawer.tools_menu()

    # Loop for window
    root.mainloop()



    


if __name__ == "__main__":
    main()