from tkinter import Tk
from typing import List
#import vlc as vlc
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer

def list_mp3s(dir: str) -> List[str]:
    mp3s = []
    for entry_name in os.listdir(dir):
        print(entry_name, entry_name[len(entry_name)-4:])
        if entry_name[len(entry_name)-4:].startswith(".mp3"):
            mp3s.append(entry_name)
    return mp3s

def launch(dir: str, file: str):
    path = dir + "/" + file
    print("Playing", file, path)

    mixer.init()
    mixer.music.load(path)
    mixer.music.play()



    print("End")

# ToDo
# Let select folder to list files from
#    Needs error handling if no audio files available in folder
# Menu UI
# Track playback
#       Pause and resume functions
#       Start audio from specific time

if __name__=="__main__":
    root = Tk()
    root.geometry("500x500")
    root.title('File Explorer')

    test = list_mp3s(".")
    launch(".", test[0])
    print(test)

    root.mainloop()