'''SuperDrawer main file'''
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import *
from tkinter.colorchooser import askcolor
import functions
import PIL.ImageGrab as ImageDraw
import PIL



class Drawer():
    def __init__(self, root):
        root.geometry('1200x800')
        root.title('SuperDrawer')
        root.resizable(0,0)
        self.root = root

        # Drawing area
        self.canvas = Canvas(root, bg='white', width=1050, height=800)
        self.canvas.pack(side=RIGHT)
        self.canvas.bind("<Button-1>", self.save_position)
        self.canvas.bind("<B1-Motion>", self.add_line_normal)
        
        self.click_number = 0 # Checker for shapes !
        self.background_color = 'white'

        # Format Menu Left Side
        self.tool_frame = Frame(root, width=150, height=800, bg='grey')
        self.tool_frame.pack(side=LEFT)

    def canvasf(self):
        self.canvas_frame = LabelFrame(self.tool_frame, text="Canvas")
        self.canvas_frame.pack()
        # Clear the canvas
        self.clear_button = Button(self.canvas_frame,width=11, text = "Clear", relief="raised", command=lambda: self.clear_canvas())
        self.clear_button.pack()
        # Background
        self.background_button = Button(self.canvas_frame,width=11, text = "Background", relief="raised", command=lambda: self.background_canvas())
        self.background_button.pack()

    def shapes(self):
        self.shape_frame = LabelFrame(self.tool_frame, text="Shapes")
        self.shape_frame.pack()
        # Line
        self.line_button = Button(self.shape_frame,width=11, text = "Line", relief="raised", command=lambda: self.line_shape())
        self.line_button.pack()
        # Polygon 
        self.polygon_button = Button(self.shape_frame, width=11, text = "Polygon", relief="raised", command=lambda: self.polygon_shape())
        self.polygon_button.pack()
        # Oval
        self.oval_button = Button(self.shape_frame, width=11, text = "Oval", relief="raised", command=lambda: self.oval_shape())
        self.oval_button.pack()

    def brush_erase(self):
        #Brush style frame and brush buttons
        self.brush_frame = LabelFrame(self.tool_frame, text="Brush")
        self.brush_frame.pack()

        # Normal
        self.normal_brush_button = Button(self.brush_frame, width=11, text = "Normal", relief="raised", command=lambda: self.normal_brush())
        self.normal_brush_button.pack()
        # Funky
        self.funky_brush_button = Button(self.brush_frame, width=11, text = "Funky", relief="raised", command=lambda: self.funky_brush())
        self.funky_brush_button.pack()
        # Eraser
        self.erase_button = Button(self.brush_frame, width=11, text = "Eraser", relief="raised", command=lambda: self.erase_function())
        self.erase_button.pack()

    def size_color(self):
        # Size frame and brush size changer
        self.size_frame = LabelFrame(self.tool_frame, text="Brush size")
        self.size_frame.pack()

        self.brush_size = 10
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
        self.color_button.configure(bg=paint_color[1])

    # Clear canvas function
    def clear_canvas(self):
        msg_box = tk.messagebox.askquestion('Save me!',
        'Do you want to clear the canvas?',
        icon='warning')
        if msg_box == 'yes':
            self.canvas.delete("all")

    # Canvas background color
    def background_canvas(self):
        self.background_color = askcolor()
        self.canvas.configure(bg=self.background_color[1])

    # Mouse position       
    def save_position(self, event):
        self.lastx = event.x
        self.lasty = event.y
    # Drawing a line (brush)
    def add_line_normal(self, event):
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y,width=self.brush_size.get(), fill=self.paint_color, smooth=False, capstyle='round')
        self.save_position(event)

    def add_line_funky(self, event):
        self.canvas.create_oval(self.lastx, self.lasty, event.x, event.y,width=self.brush_size.get(), fill=self.paint_color, outline=self.paint_color)
        self.save_position(event)

    # Drawing a lines (shape)
    def add_line_shape(self, event):
        if self.click_number == 0:
            self.lastx = event.x
            self.lasty = event.y
            self.click_number = 1
        else:
            self.canvas.create_line(self.lastx,self.lasty,event.x,event.y, width=self.brush_size.get(), fill=self.paint_color, capstyle="round", joinstyle="round")
            self.click_number = 0

    def add_polygon_shape(self, event):
        if self.click_number == 0:
            self.lastx = event.x
            self.lasty = event.y
            self.click_number = 1
        else:
            self.canvas.create_line(self.lastx,self.lasty,event.x,event.y, width=self.brush_size.get(), fill=self.paint_color, capstyle="round", joinstyle="round")
            self.save_position(event)

    def add_oval_shape(self, event):
        if self.click_number == 0:
            self.lastx = event.x
            self.lasty = event.y
            self.click_number = 1
        else:
            self.canvas.create_oval(self.lastx,self.lasty,event.x,event.y, width=self.brush_size.get(), fill=self.paint_color)
            self.click_number = 0


    # Buttons behaviour

    def line_shape(self):
        if self.line_button.config('relief')[-1] == 'sunken': # Check if button pressed
            self.line_button.config(relief="raised")
            self.canvas.bind("<Button-1>", self.save_position)
        else:
            self.click_number = 0 ## Reset last position !
            self.oval_button.config(relief="raised")
            self.polygon_button.config(relief="raised")
            self.line_button.config(relief="sunken") 
            self.normal_brush_button.config(relief="sunken")
            self.funky_brush_button.config(relief="raised")
            self.canvas.bind("<B1-Motion>", self.add_line_normal)
            self.canvas.bind("<Button-1>", self.add_line_shape)


    def polygon_shape(self):
        if self.polygon_button.config('relief')[-1] == 'sunken': # Check if button pressed
            self.polygon_button.config(relief="raised")
            self.canvas.bind("<Button-1>", self.save_position)
        else:
            self.click_number = 0 ## Reset last position !
            self.oval_button.config(relief="raised")
            self.polygon_button.config(relief="sunken")
            self.line_button.config(relief="raised")  
            self.normal_brush_button.config(relief="sunken")
            self.funky_brush_button.config(relief="raised")
            self.canvas.bind("<B1-Motion>", self.add_line_normal)
            self.canvas.bind("<Button-1>", self.add_polygon_shape)

    def oval_shape(self):
        if self.oval_button.config('relief')[-1] == 'sunken': # Check if button pressed
            self.oval_button.config(relief="raised")
            self.canvas.bind("<Button-1>", self.save_position)
        else:
            self.click_number = 0 ## Reset last position !
            self.oval_button.config(relief="sunken")
            self.polygon_button.config(relief="raised")
            self.line_button.config(relief="raised") 
            self.normal_brush_button.config(relief="sunken")
            self.funky_brush_button.config(relief="raised")
            self.canvas.bind("<B1-Motion>", self.add_line_normal)
            self.canvas.bind("<Button-1>", self.add_oval_shape)
    
        
    def erase_function(self):
        if self.erase_button.config('relief')[-1] == 'sunken': # Check if button pressed
            self.erase_button.config(relief="raised") 
            copy_color = self.color_button.cget('bg') # Get color before eraser from color_button
            self.paint_color = copy_color
        else:
            self.erase_button.config(relief="sunken")
            self.paint_color = self.background_color[1]

    def normal_brush(self):
        if self.normal_brush_button.config('relief')[-1] == 'sunken': # Check if button pressed
            self.normal_brush_button.config(relief="raised")
            self.funky_brush_button.config(relief="sunken")
            self.canvas.bind("<B1-Motion>", self.add_line_funky)
        else:
            self.funky_brush_button.config(relief="raised") 
            self.normal_brush_button.config(relief="sunken")
            self.canvas.bind("<B1-Motion>", self.add_line_normal)


    def funky_brush(self):
        if self.funky_brush_button.config('relief')[-1] == 'sunken': # Check if button pressed
            self.funky_brush_button.config(relief="raised")
            self.normal_brush_button.config(relief="sunken")
            self.canvas.bind("<B1-Motion>", self.add_line_normal)
        else:
            self.normal_brush_button.config(relief="raised") 
            self.funky_brush_button.config(relief="sunken")
            self.canvas.bind("<B1-Motion>", self.add_line_funky)

    def menu_bar(self):
        menubar = Menu(self.canvas)
        
        #File Menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: functions.new_file(self.root, self.canvas))
        filemenu.add_command(label="Open", command=lambda: functions.open_file(self.root, self.canvas))
        filemenu.add_command(label="Save", command=lambda: functions.save_file(self.root,self.canvas))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: functions.exit(self.root,self.canvas))
        menubar.add_cascade(label="File", menu=filemenu)
        # Edit menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command='TODO', accelerator="Ctrl+Z")
        editmenu.add_command(label="Redo", command='TODO')
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=lambda: functions.cut(self.canvas), accelerator='Ctrl-X')
        editmenu.add_command(label="Copy", command=lambda: functions.copy(self.canvas), accelerator='Ctrl-C')
        editmenu.add_command(label="Paste", command=lambda: functions.paste(self.canvas), accelerator='Ctrl-V')
        editmenu.add_command(label="Clear", command=lambda: self.clear_canvas())
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command=lambda: functions.select_all(self.canvas), accelerator='Ctrl-A')
        menubar.add_cascade(label="Edit", menu=editmenu)
        # About menu
        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Help", command=lambda: functions.help(self.root))
        aboutmenu.add_command(label="About", command=lambda: functions.about(self.root))
        menubar.add_cascade(label="About", menu=aboutmenu)
        
        # Add the menu bar
        self.root.config(menu=menubar)


def main():
    # Initiate tkinkter engine
    root = Tk()
    # Initiate drawer class
    drawer = Drawer(root)
    # Canvas frame
    drawer.canvasf()
    # Shapes frame
    drawer.shapes()
    # Brush and erase frame
    drawer.brush_erase()
    # Size and color frame
    drawer.size_color()
    # Menu bar
    drawer.menu_bar()
    # Loop for window
    root.mainloop()

  


if __name__ == "__main__":
    main()