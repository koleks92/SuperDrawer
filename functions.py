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

def cut(text):
    global data
    try:
        if text.selection_get():
            data = text.selection_get()
            text.delete('sel.first','sel.last')
    except:
        pass

def copy(text):
    global data
    try:
        if text.selection_get():
            data = text.selection_get()
    except:
        pass
def paste(text):
    global data
    try:
        text.insert(tk.END, data)
    except:
        pass
def delete(text):
    try:
        if text.selection_get():
            text.delete('sel.first','sel.last')
    except:
        pass
def select_all(text, event=None):
    '''Select all text'''
    text.tag_add("sel", "1.0","end")
    text.tag_config("sel",background="gray",foreground="white")
    return 'break'


def about(window):
    global pop
    pop = Toplevel(window)
    pop.title('About SuperEditor')
    pop.geometry(f"+600+400")

    pop_label = Label(pop, text="App created by koleks92")
    pop_label.pack (pady=10)
    
    pop_label_2 = Label(pop, text="Final project for CS50P")
    pop_label_2.pack (pady=20)

def help(window):
    global pop
    pop = Toplevel(window)
    pop.title('Help')
    pop.geometry("900x400")

    pop_label = Label(pop, text="How to use SuperDrawer", font=("Helvetica", 16))
    pop_label.pack (pady=10)

    pop_label_2 = Label(pop, text='If you want to create a new file, save current file or open other file, click "File" option\nIf you want to change font family, font size, font color or background color, click "Format" option\nIf you want to change to fullscreen, click "View" option\nIf you want to undo/redo action, copy, cut, paste or select all, click "Edit" option')
    pop_label_2.pack (pady=20)

    pop_label_3 = Label(pop, text="If you want to make text bold, italic, underlined or overstruk,\nselect text or select all (Ctrl+A) and choose option from menu")
    pop_label_3.pack (pady=30)        