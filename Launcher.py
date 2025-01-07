import os

#Finding Program names - each one is named after the directory it is in
MYDIR = "."
folder_names = []
for entry_name in os.listdir(MYDIR):
    entry_path = os.path.join(MYDIR, entry_name)
    if os.path.isdir(entry_path) and entry_name != ".git":
        folder_names.append(entry_name)

# print(folder_names)

#Menu
while(True):
    print("Available Programs:")
    for i in range(len(folder_names)):
        print("\t", i+1, folder_names[i])
    selection = input("Select the program to launch: ")
    if selection.isdigit() and int(selection) in range(1, len(folder_names)+1):
        selection = int(selection) - 1
        break
    else:
        print("Invalid Input: Enter a number from 1 to", len(folder_names))
    
file = folder_names[selection]
path = "./" + file + "/" + file + ".py"
print("Running", file)

#Running the selected File
import subprocess
subprocess.run(["python", path])
