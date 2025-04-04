from tkinter import Tk, Button, Label, StringVar
from tkinter.filedialog import askdirectory, askopenfilename
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

def launch(file: str):
    print("Playing", file)

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()



    print("End")

# ToDo
# Track playback
#       Play/Pause buttons and functions
#       Start audio from specific time - text box

class MusicPlayer:
    file = ""
    file_name = None
    
    def changeDir(self):
        #temp = askdirectory()
        temp = askopenfilename(filetypes=[("Audio Files", ".mp3 .wav")])
        if temp != "":
            self.file = temp
            self.file_name.set("Currently playing: " + os.path.basename(temp))
            launch(self.file)
        else:
            self.file_name.set("No file selected")
            print(self.file)

        

    def __init__(self):
        root = Tk()
        root.geometry("500x500")
        root.title('Music Player')


        folder_but = Button(root, width=10, height=1, text = "Browse...", command = self.changeDir)
        folder_but.grid(row=0, column = 1, padx=10, sticky="nw")


        self.file_name = StringVar()
        self.file_name.set("No file selected")
        display_name = Label(root, textvariable=self.file_name)
        display_name.grid(row=0, column = 0, padx=10, sticky="nw")
        #self.display = display_name
        root.mainloop()

if __name__=="__main__":
    MusicPlayer()