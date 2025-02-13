from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

from os.path import basename

def load_file():
    global open_file
    file_path = askopenfilename()

    try:
        with open(file_path, 'r') as file:   
            data = file.read()
            file_text.delete('1.0', END)
            file_text.insert(END, data)
            open_file = file_path
            root.title(basename(file_path))
    except FileNotFoundError:
        return
    

def new_file():
    temp = file_text.get("1.0", "end-1c")
    file_text.delete('1.0', END)
    global open_file
    prev_file = open_file
    open_file = ""
    if not save_file():
        open_file = prev_file
        file_text.insert(END, temp)


def save_file():
    INPUT = file_text.get("1.0", "end-1c")
    print(INPUT)
    global open_file
    try:
        if(open_file == ""):
            open_file = asksaveasfilename(defaultextension=".txt", filetypes=(("All Files", "*.*"), ("Text file", "*.txt")))
        with open(open_file, 'w') as file:
            file.write(INPUT)
            file.close()
        root.title(basename(open_file))
        return True
    except FileNotFoundError:
        return False
        



if __name__=="__main__":
    root = Tk()
    root.geometry("800x400")
    root.title("unknown file")
    open_file = ""

    file_text = Text(root, width = 50)
    file_text.configure(font = ("Courier New", 12, ""))

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new_file)
    filemenu.add_command(label="Open", command=load_file)
    filemenu.add_command(label="Save", command=save_file)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    root.config(menu=menubar)
    #input_box.grid(row=0, column = 0)

    file_text.pack(expand = YES, fill = BOTH)


    root.mainloop()

