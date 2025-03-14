import os
from typing import List
import subprocess

from tkinter import Tk, messagebox
from tkinter import Scrollbar, RIGHT, Y, Frame, BOTH, Canvas, LEFT

#Finding Program names - each one is named after the directory it is in
def list_subfolders(dir: str) -> List[str]:
    # dir = "."
    folder_names = []
    for entry_name in os.listdir(dir):
        entry_path = os.path.join(dir, entry_name)
        if os.path.isdir(entry_path) and entry_name[0] != "." and "WIP" not in entry_name:
            if os.path.isfile("./" + entry_name + "/" + entry_name + ".py"):
                folder_names.append(entry_name)
    return folder_names

def menu(folder_names: List[str]) -> int:
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
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            print("Shutting Down...") 
    
    def menu_ui(self):
        root = Tk()
        root.geometry("500x500")
        root.title("Launcher")

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

        #Add Buttons
        # For Loop, function to link each filepath to buttons?

        canvas.create_window((0, 0), window=sub_win, anchor="nw")

        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root = root
        self.root.mainloop()

    
    
    def __init__(self, dir=".", text=True):
        folder_names = list_subfolders(dir)
        if(text):
            index = menu(folder_names)
            if index >= 0:   
                file = folder_names[index]
                path = dir + "/" + file + "/" + file + ".py"
                print("Running", file)
                subprocess.Popen(["python", path])
                print("End")
        else:
            self.menu_ui()

if __name__=="__main__":
    Launcher()
    #Launcher(text=False)
