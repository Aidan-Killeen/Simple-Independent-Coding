import tkinter
#import keyboard
#import pynput

root = tkinter.Tk()

def key_handler(event):
    print(event.char, event.keysym, event.keycode)
    #handler = event.char
    handler = event.char
    if handler == 'q':
        root.quit()

root.bind("<Key>", key_handler)

#keyboard.on_press(key_handler)
#pynput

root.mainloop()