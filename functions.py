import tkinter as tk
import tkinter.filedialog as fd
from tkinter import font
from tkinter import *
from tkinter.colorchooser import askcolor
import PIL.ImageGrab as ImageGrab



filetypes = [("Text Files", "*.txt"), ('All Files', '*.*')]

'''File menu'''

def save_file(window, text):
    '''Save file'''
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    img = ImageGrab.grab(xdisplay="0")
    img.show()
    filename = fd.asksaveasfilename(defaultextension=".jpg", filetypes=filetypes)
    if not filename:
        return
    else:
        with open(filename, "w") as output_file:
            text = text.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"SuperEditor - {filename}")

def new_file(window, text):
    '''New file'''
    file_not_empty(window, text)
    text.delete("all")

def open_file(window, text):
    '''Open file'''
    if len(text.get("1.0", "end-1c")) != 0:
        file_not_empty(window, text)
    try:
        filename = fd.askopenfilename(initialdir='/home/zbenik', filetypes=filetypes)
        text.delete(1.0, tk.END)
        with open(filename, "r") as input_file:
            read = input_file.read()
            text.insert(tk.END, read)
        window.title(f"SuperEditor - {filename}")
    except:
        pass

def exit(window, text):
    msg_box = tk.messagebox.askquestion('Save me!',
    'Do you want to save current file before you exit SuperEditor?',
    icon='warning')
    if msg_box == 'yes':
        save_file(window, text)        

    window.quit()
    

def file_not_empty(window, text):
    msg_box = tk.messagebox.askquestion('Save me!', 'Do you want to save current file before opening a new file?',
                                        icon='warning')
    if msg_box == 'yes':
        save_file(window, text)        
    else:
        pass

'''Edit Menu'''

def delete(text):
    try:
        if text.selection_get():
            text.delete('sel.first','sel.last')
    except:
        pass



def about(window):
    global pop
    pop = Toplevel(window)
    pop.title('About SuperDrawer')
    pop.geometry(f"+800+600")

    pop_label = Label(pop, text="App created by koleks92")
    pop_label.pack (pady=10)
    
    pop_label_2 = Label(pop, text=" www.github.com/koleks92 ")
    pop_label_2.pack (pady=20)

def help(window):
    global pop
    pop = Toplevel(window)
    pop.title('Help')
    pop.geometry("800x600")

    pop_label = Label(pop, text="How to use SuperDrawer", font=("Helvetica", 16))
    pop_label.pack (pady=10)

    pop_label_2 = Label(pop, text="To clear the canvas, please click 'Clear' button in 'Canvas Label Frame'")
    pop_label_2.pack (pady=20)

    pop_label_3 = Label(pop, text="To change background color, pleace click 'Background' button in 'Canvas Label Frame'\n and choose a color")
    pop_label_3.pack (pady=22)      

    pop_label_4 = Label(pop, text="To draw a shape (Line/Polygon/Oval), first choose a shape type from 'Shapes Label Frame',\n after choose starting point on canvas(mouse left click),\n and choose ending point(mouse left click)")
    pop_label_4.pack (pady=24) 

    pop_label_5 = Label(pop, text="To draw with a brush (Normal/Funky/Eraser), first choose a brush type form 'Brush Label Frame,\n after click on canvas(mouse left click) and hold while moving the cursor")
    pop_label_5.pack (pady=26) 

    pop_label_6 = Label(pop, text="To change brush/shape size, please write the size in pixels in 'Brush Size Label'")
    pop_label_6.pack (pady=28) 

    pop_label_7 = Label(pop, text="To change brush/shape color, please click the color square button under 'Brush Size Label'")
    pop_label_7.pack (pady=30) 