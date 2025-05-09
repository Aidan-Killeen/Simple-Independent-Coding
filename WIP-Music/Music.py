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
    using_scale = False
    mode = None
    MUSIC_END = USEREVENT+1
    time = None
    sec_offset = 0
    
    def get_audio(self):    
        temp = askopenfilename(filetypes=[("Audio Files", ".mp3 .wav .ogg")])
        if temp != "":
            # For a valid file selection, load the file
            self.file = temp
            self.file_name.set("Currently playing: " + os.path.basename(temp))
            mixer.music.load(self.file)
            val = mixer.Sound(temp)
            self.timescale.configure(to=val.get_length()-1)     #This rounds the length up

        else:
            # If no valid file selected
            self.file_name.set("No file selected")
            print(self.file)

    def check_end(self):
        # Check if current sound finished playing
        for e in event.get():
            if e.type == self.MUSIC_END:
                self.reset()
        
        milli = mixer.music.get_pos()
        sec = int(milli/1000)
        if(not self.using_scale):
            self.timescale_val.set(sec+self.sec_offset)       

        self.root.after(100, self.check_end)

    def time_display(self, var, index, mode):
        #Whenever the variable linked to the slider changes, adjusts the label displaying the time
        sec = self.timescale.get()
        min = sec//60
        sec = sec%60
        self.time.set("{:02}:{:02}".format(min, sec))

    def adjust_scale(self, event):
        print("Click")
        self.using_scale = True

    def update_to_scale(self, event):
        print("Release")
        self.using_scale = False
        time = float(self.timescale.get())#  * 1000
        self.sec_offset = time
        print(time)
        #mixer.music.play(loops=0, start=time)
        if self.file != "":
            if self.toggle: #and not self.paused: # If drag back while playing, time not displahying accuratley
                mixer.music.play()
                mixer.music.set_pos(time)
                self.paused = True
                mixer.music.pause()
            else:
                #mixer.music.stop()
                #mixer.music.rewind()
                mixer.music.play()
                mixer.music.set_pos(time)
            self.timescale.set(time)
    
    def reset(self):
        self.toggle = True
        self.paused = False
        self.mode.set("Play")
        self.time.set("00:00")
        self.sec_offset = 0

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

        # Display time - text
        self.time = StringVar()
        self.time.set("0:00")
        display_time =Label(root, textvariable=self.time)
        display_time.grid(row=3, column = 1, padx=10, sticky="nw")
        self.timescale_val = IntVar()
        self.timescale_val.trace_add('write', self.time_display)

        # Display time - on scale
        self.timescale = Scale(root, from_=0, to=0, orient=HORIZONTAL, showvalue=0, variable=self.timescale_val)
        self.timescale.bind("<Button-1>", self.adjust_scale)
        self.timescale.bind("<ButtonRelease-1>", self.update_to_scale)
        self.timescale.grid(row=3, column = 0, padx=10, sticky="nw")

        self.root = root
        self.check_end()
        self.root.mainloop()
        quit()

if __name__=="__main__":
    MusicPlayer()