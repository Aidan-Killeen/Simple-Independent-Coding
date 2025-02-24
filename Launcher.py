import os
from typing import List
import subprocess

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

if __name__=="__main__":
    folder_names = list_subfolders(".")
    index = menu(folder_names)
    if index >= 0:   
        file = folder_names[index]
        path = "./" + file + "/" + file + ".py"
        print("Running", file)
        subprocess.Popen(["python", path])
    print("End")
