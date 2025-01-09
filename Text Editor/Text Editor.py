from tkinter import *

def load_file(filename: str):
    with open("./Text Editor/"+filename, 'r') as file:
        data = file.read()
        file_text.insert(END, data)

def save():
    INPUT = file_text.get("1.0", "end-1c")
    print(INPUT)



root = Tk()
root.geometry("500x500")
root.title("unknown file")


file_text = Text(root, width = 50)
file_text.configure(font = ("Arial", 20, ""))




#input_box.grid(row=0, column = 0)




save_button = Button(root, height = 2,
                 width = 20, 
                 text ="Save",
                 command = lambda:save())



save_button.pack(expand = YES, fill = BOTH)
file_text.pack(expand = YES, fill = BOTH)

import os
print(os.listdir('.'))

filename = "Testfile.txt"
load_file(filename)

root.mainloop()

