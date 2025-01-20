import subprocess
from tkinter import Tk
from tkinter import Button
from tkinter import TclError
import re

def paste():
    try:
        return root.clipboard_get()
    except TclError:
        return ""


def copy(txt):
    root.clipboard_clear()
    root.clipboard_append(txt)


def adjust(txt):
    output = re.sub(r"([^.])\n",r"\1 ", txt) #losing char
    return output

def pdf_edit():
    current_clip = paste()
    current_clip = adjust(current_clip)
    copy(current_clip)
    print(current_clip)

if __name__=="__main__":
    root = Tk()
    #root.withdraw()
    root.geometry("500x500")
    root.title("Simple Calculator")
    

    b1 = Button(root, text = "Edit", command = pdf_edit, 
                    padx = 30, pady = 30)
    b1.pack()

    root.mainloop()