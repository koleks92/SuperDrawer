'''SuperDrawer main file'''
from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter as tk
import functions


class Drawer():
    def __init__(self, root):
        root.geometry('1200x800')
        root.title('SuperDrawer')


        # Drawing area
        self.canvas = Canvas(root, bg='white', width=1100, height=800)
        self.canvas.pack(side=RIGHT)
        self.canvas.bind("<Button-1>", self.save_position)
        self.canvas.bind("<B1-Motion>", self.add_line)

        self.brush_size = 10

        # Format Menu Left Side
        self.tool_frame = Frame(root, width=100, height=800, bg='grey')
        self.tool_frame.pack(side=LEFT)

        # size frame and brush size changer
        self.size_frame = LabelFrame(self.tool_frame, text="Brush size")
        self.size_frame.pack()

        self.brush_size = tk.Entry(self.size_frame)
        self.brush_size.insert(END, "10")
        self.brush_size.pack()
        
        # Color frame and color changer
        self.color_frame = LabelFrame(self.tool_frame, text="Color")
        self.color_frame.pack()

        self.paint_color = "black"
        self.color_button = Button(self.color_frame, bg = self.paint_color,width=10,height=5, command=lambda: self.color_changer())
        self.color_button.pack()

       


    #Color changer
    def color_changer(self):
        paint_color = askcolor()
        self.paint_color = paint_color[1]
        self.color_button.configure( bg=paint_color[1])

    # Mouse position       
    def save_position(self, event):
        self.lastx = event.x
        self.lasty = event.y
    # Drawing a line
    def add_line(self, event):
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y,width=self.brush_size.get(), fill=self.paint_color)
        self.save_position(event)
    





def main():
    # Initiate tkinkter engine
    root = Tk()
    # Initiate drawer class
    drawer = Drawer(root)



    # Loop for window
    root.mainloop()



    


if __name__ == "__main__":
    main()