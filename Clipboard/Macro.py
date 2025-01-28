from tkinter import Tk, Button, Entry, Label, Toplevel, messagebox
from pynput.keyboard import Key, Controller, Listener

def test_macro():
    print("Test")
class Macro:   
    changing_shortcut = False
    listening = False
    top = None
    commands = None
    displays = None
    shortcuts = [Key.insert]

    def change(self, i):
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
            self.shortcuts[0] = key
                                                                            #Get which shortcut is changing
            display = self.displays[0]
            display.delete(0, "end")
            display.insert( len(display.get()), '{}'.format(self.shortcuts[0]))
            self.changing_shortcut = False

            #Deleting popup
            if self.top != None:
                self.top.destroy()
        #If operating as a macro
        elif self.listening:
            print('{} pressed'.format(key))
            if key == self.shortcuts[0]:                                                #get which keys this corresponds to
                self.commands[0]()                                                  #get which command is running
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

    
    def __init__(self, macro_command=test_macro, *additional_macros):
        self.keyboard = Controller()
        self.listener = Listener(on_press=self.get_shortcut)
        self.listener.start()
        self.commands = [macro_command] + list(additional_macros)

        total_macros = 1 + len(additional_macros)
        self.shortcuts = [Key.insert] * total_macros
        self.displays = [None] * total_macros

        root = Tk()
        root.geometry("500x500")
        root.title("Clipboard")
        Label(root, text= "Macros").grid(column=1, row=0)

        #Individual macro prep
        for i in range(total_macros):
            single_use = Button(root, text = "Test: " + macro_command.__name__, command = macro_command)
            single_use.grid(row=i+1, column = 0)


            self.displays[i] = Entry(root, width = 50)
            self.displays[i].grid(row=i+1, column = 1)
            self.displays[i].insert( len(self.displays[i].get()), '{}'.format(self.shortcuts[0]))   #change this to var

            change = Button(root, text="Change", command= lambda i = i: self.change(i))
            change.grid(row=i+1, column=2)

        launch = Button(root, text="Launch Macros", command=self.macro_start)
        launch.grid(row=total_macros+1, column=1)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root = root
        self.root.mainloop()
        self.listener.join()


if __name__=="__main__":
    Macro()