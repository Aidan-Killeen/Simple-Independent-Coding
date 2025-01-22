from tkinter import Tk, Button, Entry
import pyperclip

import re
from pynput.keyboard import Key, Controller, Listener

def pdf_edit():
    current_clip = pyperclip.paste()
    current_clip = adjust(current_clip)
    pyperclip.copy(current_clip)

    print(current_clip)


def adjust(txt):
    output = re.sub(r"([^.])\n",r"\1 ", txt) #losing char
    return output





changing_shortcut = False
listening = False
def get_shortcut(key):
    global changing_shortcut
    global shortcut
    if changing_shortcut:
        shortcut = key
        short_disp.delete(0, "end")
        short_disp.insert( len(short_disp.get()), '{}'.format(shortcut))
        changing_shortcut = False
    elif listening:
        print('{} pressed'.format(key))
        if key == shortcut:
            pdf_edit()
        elif key == Key.esc:
            return False

def change():
    #Needs to create a popup
    global changing_shortcut
    changing_shortcut = True

def macro():
    root.destroy()
    global listening
    listening = True
    
    

shortcut = Key.insert

if __name__=="__main__":
    keyboard = Controller()
    listener = Listener(on_press=get_shortcut)
    listener.start()

    root = Tk()
    root.geometry("500x500")
    root.title("Clipboard")
    

    single_use = Button(root, text = "Single Edit", command = pdf_edit, 
                    padx = 30, pady = 10)
    single_use.grid(row=0, column = 0)
    short_disp = Entry(root, width = 50)
    short_disp.grid(row=1, column = 0)
    short_disp.insert( len(short_disp.get()), '{}'.format(shortcut))

    change = Button(root, text="Change", command=change)
    change.grid(row=1, column=1)

    min = Button(root, text="Launch Macro", command=macro)
    min.grid(row=2)

    root.mainloop()
    print("Macro launched")
    listener.join()