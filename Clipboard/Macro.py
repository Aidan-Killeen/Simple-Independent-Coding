from tkinter import Tk, Button, Entry, Label, Toplevel, messagebox
from pynput.keyboard import Key, Controller, Listener

class Macro:   
    changing_shortcut = False
    listening = False
    top = None
    command = None
    shortcut = Key.insert

    def change(self):
        #Changes mode of get_shortcut function
        self.changing_shortcut = True

        #Creates a Popup
        self.top = Toplevel(self.root)
        self.top.geometry("300x100")
        self.top.title("Select Key")
        Label(self.top, text= "Press any Key").grid(column=0, row=0)

        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)

    def get_shortcut(self, key):
        #If swapping what hotkey is being used
        if self.changing_shortcut:
            self.shortcut = key
            self.short_disp.delete(0, "end")
            self.short_disp.insert( len(self.short_disp.get()), '{}'.format(self.shortcut))
            self.changing_shortcut = False

            #Deleting popup
            if self.top != None:
                self.top.destroy()
        #If operating as a macro
        elif self.listening:
            print('{} pressed'.format(key))
            if key == self.shortcut:
                self.command()
            elif key == Key.esc:
                print("Shutting Down...")
                return False

    def macro_start(self):
        #Removes the window, changes get_shortcut into macro mode
        self.root.destroy()
        print("Launching Macro")
        self.listening = True
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            self.listener.stop()
            print("Shutting Down...")

    
    def __init__(self, macro_command):
        #pass
        self.keyboard = Controller()
        self.listener = Listener(on_press=self.get_shortcut)
        self.listener.start()
        self.command = macro_command

        root = Tk()
        root.geometry("500x500")
        root.title("Clipboard")
        

        single_use = Button(root, text = "Single Edit", command = macro_command, 
                        padx = 30, pady = 10)
        single_use.grid(row=0, column = 0)
        self.short_disp = Entry(root, width = 50)
        self.short_disp.grid(row=1, column = 0)
        self.short_disp.insert( len(self.short_disp.get()), '{}'.format(self.shortcut))

        change = Button(root, text="Change", command=self.change)
        change.grid(row=1, column=1)

        min = Button(root, text="Launch Macro", command=self.macro_start)
        min.grid(row=2)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root = root
        self.root.mainloop()
        self.listener.join()
