import os
from typing import List
import subprocess

from tkinter import Tk, messagebox, Button, Grid, Text
from tkinter import Scrollbar, RIGHT, Y, Frame, BOTH, Canvas, LEFT, TOP
from sys import executable


#Finding Program names - each one is named after the directory it is in
def list_subfolders(dir: str) -> List[str]:
    """
    Find all subfolders that contain python files

    Parameters
    ----------
    dir : str
        The Directory the function is searching for valid subfolders

    Returns
    ----------
    list
        A List of Strings containing the names of all valid subfolders to use the launcher on
    """
    folder_names = []
    for entry_name in os.listdir(dir):
        entry_path = os.path.join(dir, entry_name)
        if os.path.isdir(entry_path) and entry_name[0] != "." and "WIP" not in entry_name:
            if os.path.isfile(dir + "/" + entry_name + "/" + entry_name + ".py"):
                folder_names.append(entry_name)
    return folder_names

def launch(dir: str, file: str):
    """
    Function to Launch Other Python files

    Parameters
    ----------
    dir : str
        The Directory the file structure is contained within is in
    file : str
        The name of the folder containing the python file 
        (Should be the same as the name of the python file)
    """

    path = dir + "/" + file + "/" + file + ".py"
    print("Launching", file, path)
    
    subprocess.Popen([executable, path])

    print("End")

def menu(folder_names: List[str]) -> int:
    """
    Text based that selects which program will be opened.

    Parameters
    ----------
    folder_names : List[str]
        A List of strings containing the names of the folders containing the python files
        (Should be the same name for the folder and the python file)    

    Returns
    ----------
    int
        The index of the file in the input array that was selected
    """
    index = 0
    while(True):
        print("Available Programs:")
        for i in range(len(folder_names)):
            print("\t", i+1, folder_names[i])
        selection = input("Select the program to launch: ")
        if selection.isdigit() and int(selection) in range(1, len(folder_names)+1):
            index = int(selection) - 1
            break
        elif selection.lower() == "exit":
            print("Exiting program...")
            index = -1
            break
        else:
            print("Invalid Input: Enter a number from 1 to", len(folder_names), "or type 'exit'")
    return index

class Launcher:
    """
    A class created to be able to launch other python programs using a UI

    Attributes
    ----------
    root : tkinter.Tk
        Window to display launcher in
    canvas : tkinter.Canvas
        A canvas, used to make the Button UI scrollable
    dir : str
        Directory program is running in
    files : List[str]
        The list of folder/file names for the python files
    

    """
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            print("Shutting Down...") 
    
    def _on_mousewheel(self, event):
        """
        Event Handler for mousewheel being scrolled.

        Parameters
        ----------
        event : event
            Data from the Event that is triggered by scrolling the mousewheel    

        """
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def menu_ui(self):
        """
        Tkinter based UI that allows the user to select which program will be opened.

        """
        root = Tk()
        window_size = 500
        root.geometry(str(window_size) + "x" + str(window_size))
        root.title("Launcher")

        # Creating scrollable area for buttons
        win = Frame(root)
        win.pack(fill=BOTH, expand=True)

        canvas = Canvas(win, bg="skyblue")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(win, orient='vertical', command = canvas.yview)
        scrollbar.pack(side = RIGHT, fill = Y)

        s_width = scrollbar.winfo_reqwidth()

        sub_win = Frame(canvas, background="skyblue")

        #Add Buttons
        margin = 10
        button_width = 50
        for i in range(len(self.files)):
            single_use = Button(sub_win, width=button_width, height=5,
                                text = self.files[i], command = lambda i = self.files[i]: launch(self.dir,i))
            single_use.grid(row=i+1, column = 0, padx=margin, sticky="n")


        frame_id = canvas.create_window(window_size//2-s_width//2, 0, window=sub_win, anchor="n", tags="inner_frame",)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.update()

        #Setting size of scrollable area
        bbox = list(canvas.bbox("inner_frame"))
        canvas_width = canvas.winfo_width()
        canvas_heigth = canvas.winfo_height()
        if bbox[2] < canvas_width:
            bbox[2] = canvas_width
        if bbox[3] < canvas_heigth:
            bbox[3] = canvas_heigth
        canvas.configure(scrollregion=(0, 0, bbox[2], bbox[3]))

        bbox = tuple([0,0] + bbox[2:])
        canvas.bind(
            '<Configure>', lambda e: canvas.configure(scrollregion=bbox)
        )

        canvas.bind_all(
            "<MouseWheel>", self._on_mousewheel
        )

        self.canvas = canvas
        
        self.root = root
        self.root.mainloop()

    
    
    def __init__(self, dir=".", text=False):
        """
        Initialises a Launcher object.

        Parameters
        ----------
        dir : str
            The directory to run the Laucher object in
        text : boolean
            Boolean to select which mode the launcher runs - True is text based, False is using a Graphical UI   

        """
        folder_names = list_subfolders(dir)
        self.dir = dir
        self.files = folder_names
        if(text):
            index = menu(folder_names)
            if index >= 0:   
                file = folder_names[index]
                launch(dir, file)

        else:
            self.menu_ui()

if __name__=="__main__":
    #Launcher(text=True)
    Launcher()
