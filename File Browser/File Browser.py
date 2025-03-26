from tkinter.filedialog import askopenfilename
from tkinter import *


def browse():
    run = True
    while run:
        file = askopenfilename(title="Select a File")
        if file == "":
            run = False
        else:
            target_file_label.configure(text="File Opened: "+file)
    #Need to open the file using system default

if __name__=="__main__":
    root = Tk()
    root.geometry("500x500")
    root.title('File Explorer')

    target_file_label = Label(root, text="No Files chosen")
    target_file_label.grid(column=1, row=1)

    browse_button = Button(root, text="Browse Files", command=browse)
    exit = Button(root, text = "Exit",command = exit)
    browse_button.grid(column=1, row=2)
    exit.grid(column=1, row=3)

    root.mainloop()



