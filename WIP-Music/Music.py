from tkinter import Tk, Button, Label, StringVar, IntVar, DoubleVar, Scale, HORIZONTAL
from tkinter.filedialog import askopenfilename
from typing import List
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
#       Start audio from specific time - text box

class MusicPlayer:
    file = ""
    file_name = None
    mixer.init()
    paused = False
    toggle = True
    mode = None
    MUSIC_END = USEREVENT+1
    time = None
    

    
    def get_audio(self):    
        temp = askopenfilename(filetypes=[("Audio Files", ".mp3 .wav")])
        if temp != "":
            # For a valid file selection, load the file
            self.file = temp
            self.file_name.set("Currently playing: " + os.path.basename(temp))
            mixer.music.load(self.file)
            val = mixer.Sound(temp)
            self.timescale.configure(to=val.get_length())

        else:
            # If no valid file selected
            self.file_name.set("No file selected")
            print(self.file)

    def check_end(self):
        # Check if current sound finished playing
        for e in event.get():
            if e.type == self.MUSIC_END:
                #print('music end event')
                self.reset()

        # Check the current time
        milli = mixer.music.get_pos()
        sec = int(milli/1000)
        # Make conditional - need to be able to alter this
        self.timescale.set(sec)
        m = sec//60
        sec = sec % 60
        self.time.set("{:02}:{:02}".format(m, sec))
        
        # Addition - Update slider
        

        self.root.after(100, self.check_end)

    def update_time(self, event):
        return
    
    def reset(self):
        self.toggle = True
        self.paused = False
        self.mode.set("Play")
        self.time.set("0:00")

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


    def stop(self):
        if(self.file != ""):
            self.reset()
            mixer.music.stop()
        else:
            print("Error: No music loaded")
        

    def __init__(self):
        init()
        root = Tk()
        root.geometry("500x500")
        root.title('Music Player')
        mixer.music.set_endevent(self.MUSIC_END)

        # Select file
        folder_but = Button(root, width=10, height=1, text = "Browse...", command = self.get_audio)
        folder_but.grid(row=0, column = 1, padx=10, sticky="nw")

        # Display selected file
        self.file_name = StringVar()
        self.file_name.set("No file selected")
        display_name = Label(root, textvariable=self.file_name)
        display_name.grid(row=0, column = 0, padx=10, sticky="nw")

        # Play/Pause Button
        self.mode = StringVar()
        self.mode.set("Play")
        play = Button(root, width=10, height=1, textvariable=self.mode, command = self.play_pause)
        play.grid(row=1, column = 0, padx=10, sticky="nw")

        # Stop Button
        stop = Button(root, width=10, height=1, text = "Stop", command = self.stop)
        stop.grid(row=1, column = 1, padx=10, sticky="nw")

        # Display time
        self.time = StringVar()
        self.time.set("0:00")
        display_time =Label(root, textvariable=self.time)
        display_time.grid(row=3, column = 1, padx=10, sticky="nw")

        self.timescale = Scale(root, from_=0, to=0, orient=HORIZONTAL, showvalue=0)
        self.timescale.bind("<ButtonRelease-1>", self.update_time)
        self.timescale.grid(row=3, column = 0, padx=10, sticky="nw")

        self.root = root
        self.check_end()
        self.root.mainloop()
        quit()

if __name__=="__main__":
    MusicPlayer()