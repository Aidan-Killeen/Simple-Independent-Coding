from tkinter import Tk, Button, Entry, Label, Toplevel, messagebox
import pyperclip

import re
from pynput.keyboard import Key, Controller, Listener

def pdf_edit():
    #Adjusts copied text
    current_clip = pyperclip.paste()
    output = re.sub(r"([^\\.])\r\n", r"\1 ", current_clip)
    pyperclip.copy(output)


changing_shortcut = False
listening = False
top = None
def change():
    #Changes mode of get_shortcut function
    global changing_shortcut
    changing_shortcut = True

    #Creates a Popup
    global top
    top = Toplevel(root)
    top.geometry("300x100")
    top.title("Select Key")
    Label(top, text= "Press any Key").grid(column=0, row=0)

    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)

def get_shortcut(key):
    global changing_shortcut
    global shortcut
    #If swapping what hotkey is being used
    if changing_shortcut:
        shortcut = key
        short_disp.delete(0, "end")
        short_disp.insert( len(short_disp.get()), '{}'.format(shortcut))
        changing_shortcut = False

        #Deleting popup
        global top
        if top != None:
            top.destroy()
    #If operating as a macro
    elif listening:
        print('{} pressed'.format(key))
        if key == shortcut:
            pdf_edit()
        elif key == Key.esc:
            print("Shutting Down...")
            return False

def macro():
    #Removes the window, changes get_shortcut into macro mode
    root.destroy()
    print("Launching Macro")
    global listening
    listening = True
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        listener.stop()
        print("Shutting Down...")

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

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    listener.join()