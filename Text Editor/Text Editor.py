from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def load_file():
    global open_file
    file_path = askopenfilename()

    with open(file_path, 'r') as file:
    #with open(path+filename, 'r') as file:    
        data = file.read()
        file_text.delete('1.0', END)
        file_text.insert(END, data)
        open_file = file_path
        root.title(file_path)
    

def new_file():
    file_text.delete('1.0', END)
    global open_file
    open_file = ""
    save_file()


def save_file():
    INPUT = file_text.get("1.0", "end-1c")
    print(INPUT)
    global open_file
    if(open_file == ""):
        open_file = asksaveasfilename()
    with open(open_file, 'w') as file:
        file.write(INPUT)
        file.close()
    root.title(open_file)




root = Tk()
root.geometry("500x500")
root.title("unknown file")
path = "./Text Editor/"
open_file = ""

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

