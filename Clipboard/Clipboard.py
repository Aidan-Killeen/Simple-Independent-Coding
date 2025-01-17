import subprocess
from tkinter import Tk
from tkinter import TclError

def paste():
    try:
        return root.clipboard_get()
    except TclError:
        return ""


def copy(txt):
    root.clipboard_clear()
    root.clipboard_append(txt)


def adjust(txt):
    return txt.replace("\n", " ")

root = Tk()
root.withdraw()

current_clip = paste()
current_clip = adjust(current_clip)
copy(current_clip)
print(current_clip)