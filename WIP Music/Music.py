from tkinter import Tk
from typing import List
import os

def list_mp3s(dir: str) -> List[str]:
    mp3s = []
    for entry_name in os.listdir(dir):
        print(entry_name, entry_name[len(entry_name)-4:])
        if entry_name[len(entry_name)-4:].startswith(".mp3"):
            mp3s.append(entry_name)
    return mp3s

if __name__=="__main__":
    root = Tk()
    root.geometry("500x500")
    root.title('File Explorer')

    test = list_mp3s(".")
    print(test)