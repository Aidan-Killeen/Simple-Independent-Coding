from tkinter.filedialog import askopenfilename
from tkinter import Tk
from subprocess import call
from os import startfile
from platform import system

def browse():
    """
    Function that loops opening a file dialog, and opens the file using the system default whenever a file is selected. 

    """
    run = True
    while run:
        file = askopenfilename(title="Select a File")
        if file == "":
            run = False
            exit()
        else:
            if system() == 'Darwin':
                call(('open', file))
            elif system() == "Windows":
                startfile(file)
            else:
                call(('xdg-open', file))

if __name__=="__main__":
    root = Tk()
    root.geometry("500x500")
    root.title('File Explorer')

    root.withdraw()

    browse()

    root.mainloop()



