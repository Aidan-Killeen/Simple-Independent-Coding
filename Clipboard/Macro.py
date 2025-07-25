from tkinter import Tk, Button, Label, Toplevel, messagebox

from tkinter import Scrollbar, RIGHT, Y, Frame, BOTH, Canvas, LEFT
from pynput.keyboard import Key, Controller, Listener

def test_macro():
    """
    Simple test function to feed into Macro class constructor. 

    """
    print("Test 1")

def test_macros():
    """
    Simple test function to feed into Macro class constructor. 

    """
    print("Test 2")
class Macro:
    """
    A class created to be able to run functions upon pressing a key on the keyboard

    Attributes
    ----------
    changing_shortcut : boolean
        Boolean that adjusts class behavior when in the process of changing the shortcut associated with a function
    change_index : int
        Integer that holds the index of which functions' key is being changed when changing_shortcut is True
    listening : boolean
        Boolean that swaps modes between setup and running the macro - is True when setup is finished
    top : tkinter.Toplevel
        Popup prompting user to press a key when changing shortcut used for macro 
    commands : List[function]
        The list of the commands the macro runs on pressing keys
    displays : List[tkinter.Label]
        List of labels displaying the currently designated keys to trigger each function
    shortcuts : List[Key]
        The list of keys that are currently being used as shortcuts
    

    """
    changing_shortcut = False
    change_index = 0
    listening = False
    top = None
    commands = None
    displays = None
    shortcuts = [Key.insert]

    def change(self, i):
        """
        Function to prompt user if they decide to change the shortcut key for a function - adjusts variables for listener function to do so

        Parameters
        ----------
        i : int
            Index of the function that is having it's shortcut adjusted

        """
        #Changes mode of get_shortcut function
        if self.changing_shortcut == False:
            self.changing_shortcut = True
            self.change_index = i

            #Creates a Popup
            self.top = Toplevel(self.root)
            self.top.geometry("300x100")
            self.top.title("Select Key")
            Label(self.top, text= "Press any Key").grid(column=0, row=0)

            self.top.columnconfigure(0, weight=1)
            self.top.rowconfigure(0, weight=1)

    def get_shortcut(self, key):
        """
        Listener function that will adjust which key is used for each function if in preparation mode or triggers the functions if in listening mode

        Parameters
        ----------
        key : Key
            The key that has been pressed, triggering the listener
        
        """
        #If swapping what hotkey is being used
        if self.changing_shortcut:
            # Find the index of the keybind being changed
            if key != Key.esc:
                index = self.change_index
                self.shortcuts[index] = key
                self.displays[index].config(text=self.shortcuts[index])
            else:
                print("Cannot keybind to Esc: Required to exit")
            self.changing_shortcut = False

            #Deleting popup
            if self.top != None:
                self.top.destroy()
        #If operating as a macro
        elif self.listening:
            print('{} pressed'.format(key))
            if key in self.shortcuts:                                                #get which keys this corresponds to
                triggered = [ x for x, y in enumerate(self.shortcuts) if y == key ]
                print(triggered)
                for command in triggered:
                    self.commands[command]()                                                  #get which command is running
            elif key == Key.esc:
                print("Shutting Down...")
                return False

    def macro_start(self):
        """
        Swaps the Macro object out of preparation mode and into listening mode

        """
        self.root.destroy()
        print("Launching Macro")
        self.listening = True
        
    def on_closing(self):
        """
        Creates a prompt to ask if you really want to close program
        
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            self.listener.stop()
            print("Shutting Down...")

    
    def __init__(self, macro_command=test_macro, *additional_macros):
        """
        Initialises a Macro object.

        Parameters
        ----------
        macro_command : fuction
            Fuction that is to be applied a keyboard shortcut
        additional_macros : List[function]
            A List of Functions to apply keyboard shortcuts to
            (combined with macro_command improves versitility of input for amount of functions)   

        """
        self.keyboard = Controller()
        self.listener = Listener(on_press=self.get_shortcut)
        self.listener.start()
        if type(macro_command) is list:
            self.commands = macro_command + list(additional_macros)
        else:
            self.commands = [macro_command] + list(additional_macros)
        print(self.commands)

        total_macros = len(self.commands)
        self.shortcuts = [Key.insert] * total_macros
        self.displays = [None] * total_macros

        root = Tk()
        root.geometry("500x500")
        root.title("Clipboard")

        
        # Making list of functions scrollable
        win = Frame(root)
        win.pack(fill=BOTH, expand=1)

        canvas = Canvas(win)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = Scrollbar(win, orient='vertical', command = canvas.yview)
        scrollbar.pack(side = RIGHT, fill = Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            '<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        sub_win = Frame(canvas)

        Label(sub_win, text= "Macros").grid(column=1, row=0)

        #Individual macro prep
        for i in range(total_macros):
            single_use = Button(sub_win, text = "Test: " + self.commands[i].__name__, command = self.commands[i])
            single_use.grid(row=i+1, column = 0)

            self.displays[i] = Label(sub_win, bg="white", text=self.shortcuts[i], width = 40)
            self.displays[i].grid(row=i+1, column = 1)

            change = Button(sub_win, text="Change", command= lambda i = i: self.change(i))
            change.grid(row=i+1, column=2)


        launch = Button(sub_win, text="Launch Macros", command=self.macro_start)
        launch.grid(row=total_macros+1, column=1)

        canvas.create_window((0, 0), window=sub_win, anchor="nw")

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root = root
        self.root.mainloop()
        self.listener.join()


if __name__=="__main__":
    Macro()
    #Macro(test_macro, test_macros)
    #Macro([test_macros, test_macro])
    #Macro([test_macro]*100)