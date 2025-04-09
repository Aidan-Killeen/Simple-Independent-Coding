from tkinter import Tk, Button, Label, StringVar
from tkinter.filedialog import askdirectory, askopenfilename
from typing import List
#import vlc as vlc
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer, event, USEREVENT, init, quit

def list_mp3s(dir: str) -> List[str]:
    mp3s = []
    for entry_name in os.listdir(dir):
        print(entry_name, entry_name[len(entry_name)-4:])
        if entry_name[len(entry_name)-4:].startswith(".mp3"):
            mp3s.append(entry_name)
    return mp3s


# ToDo
# Track playback
#       Stop button
#       Start audio from specific time - text box

class MusicPlayer:
    file = ""
    file_name = None
    mixer.init()
    paused = False
    toggle = True
    mode = None
    MUSIC_END = USEREVENT+1
    
    def changeDir(self):
        #temp = askdirectory()
        temp = askopenfilename(filetypes=[("Audio Files", ".mp3 .wav")])
        if temp != "":
            self.file = temp
            self.file_name.set("Currently playing: " + os.path.basename(temp))
            mixer.music.load(self.file)

        else:
            self.file_name.set("No file selected")
            print(self.file)

    def check_end(self):
        for e in event.get():
            if e.type == self.MUSIC_END:
                #print('music end event')
                self.toggle = True
                self.paused = False
                self.mode.set("Play")

        self.root.after(100, self.check_end)

    def play_pause(self):
        if(self.file != ""):
            if(self.toggle):
                if(self.paused):
                    mixer.music.unpause()
                else:
                    mixer.music.play()
                self.paused = False
                self.toggle = False
                self.mode.set("Pause")
            else:
                mixer.music.pause()
                self.paused = True
                self.toggle = True
                self.mode.set("Play")
        else:
            print("Error: No music loaded")
        
        

        

    def __init__(self):
        init()
        root = Tk()
        root.geometry("500x500")
        root.title('Music Player')
        mixer.music.set_endevent(self.MUSIC_END)


        folder_but = Button(root, width=10, height=1, text = "Browse...", command = self.changeDir)
        folder_but.grid(row=0, column = 1, padx=10, sticky="nw")


        self.file_name = StringVar()
        self.file_name.set("No file selected")
        display_name = Label(root, textvariable=self.file_name)
        display_name.grid(row=0, column = 0, padx=10, sticky="nw")
        #self.display = display_name

        self.mode = StringVar()
        self.mode.set("Play")
        play = Button(root, width=10, height=1, textvariable=self.mode, command = self.play_pause)
        play.grid(row=1, column = 0, padx=10, sticky="nw")
        #pause = Button(root, width=10, height=1, text = "Pause", command = self.pause)
        #pause.grid(row=1, column = 1, padx=10, sticky="nw")
        self.root = root

        self.check_end()
        self.root.mainloop()
        quit()

if __name__=="__main__":
    MusicPlayer()