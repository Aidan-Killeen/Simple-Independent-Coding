from tkinter import *

def load_file():
    global filename
    filename = "Testfile.txt"
    root.title(filename)
    with open(path+filename, 'r') as file:
        data = file.read()
        file_text.insert(END, data)

def new_file():
    return

def save_file():
    INPUT = file_text.get("1.0", "end-1c")
    print(INPUT)
    global filename
    if(filename == ""):
        return #Run new_file command
    with open(path+filename, 'w') as file:
        file.write(INPUT)
        file.close()  



root = Tk()
root.geometry("500x500")
root.title("unknown file")
path = "./Text Editor/"
filename = ""

file_text = Text(root, width = 50)
file_text.configure(font = ("Arial", 20, ""))

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

