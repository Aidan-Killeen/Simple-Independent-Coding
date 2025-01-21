import tkinter
from pynput.keyboard import Key, Controller, Listener
import subprocess
from Clipboard import pdf_edit

def on_press(key):
    print('{} pressed'.format(key))
    #print(dir(key))

    if key == Key.insert:
        subprocess.Popen(["python", "./Clipboard/Clipboard.py"])
        #pdf_edit()

    
def on_release(key):
    print('{} release'.format(key))

    if key == Key.esc:
        # Stop listener
        return False
0
# --- main ---

keyboard = Controller()

listener = Listener(on_press=on_press, on_release=on_release)

listener.start()

# ... other code ...

listener.join()