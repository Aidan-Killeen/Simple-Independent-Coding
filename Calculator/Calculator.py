# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:56:52 2022

@author: Aidan
"""

#Simple calculator using Form
#Click on numbers and add numbers together


from tkinter import *

class Calculator:
    """
    A simple calculator class

    Attributes
    ----------
    variable : int
        Integer that stores previously calculated values when doing a mathematical fuction
    operation : str
        String that stores which operation the calculator is going to perform upon pressing equals key
    input_box : tkinter.Entry
        A tkinter.Entry which stores and displays the current integer you are entering into the calculator
    """
    variable = 0
    operation = ""
    input_box = None
        
    def clicked(self, x):
        """
        A class created to be able to run functions upon pressing a key on the keyboard

        Parameters
        ----------
        x : int
            A Value of 0-9 that is going to be appended to the current value within the input_box
        """
        if (self.input_box.get() == "0"):
            self.input_box.delete(0, "end")
        self.input_box.insert( len(self.input_box.get()), x)
        
    def clear_all(self):
        self.clear_box()
        global variable
        variable = 0
        
    def clear_box(self):
        self.input_box.delete(0, "end")
        self.input_box.insert( len(self.input_box.get()), "0")
        
    def op_click(self, op: str):
        if(self.variable == 0):
            self.variable = int(self.input_box.get())
        else:
            self.equal_click()
        self.operation = op
        self.clear_box()
        
    def equal_click(self):
        temp = None
        box_val = int(self.input_box.get())
        if(self.operation == "+"):
            temp = self.variable + box_val
        elif(self.operation == "-"):
            temp = self.variable - box_val
        elif(self.operation == "*"):
            temp = self.variable * box_val
        elif(self.operation == "/"):
            if(box_val != 0):
                temp = int(self.variable / box_val)
        else:
            temp = box_val
        self.variable = temp
        self.input_box.delete(0, "end")
        self.input_box.insert(len(self.input_box.get()), self.variable)
        self.operation = ""
        
    def __init__(self):
        root = Tk()
        root.geometry("500x500")
        root.title("Simple Calculator")

        input_frame = Frame(root)
        input_frame.pack(expand = YES, fill = BOTH)


        input_box = Entry(input_frame, width = 50)
        input_box.configure(font = ("Arial", 20, ""))
        input_box.grid(row=0, column = 0)
        self.input_box = input_box
        self.clear_box()

        button_font = ("Arial", 15)
        button_frame = Frame(root)
        button_frame.pack(expand = YES, fill = BOTH)
        #Should be easier with manual buttons
        for i in range(0, 9):
            b1 = Button(button_frame, text = str(i+1), font = button_font, command = lambda i = i: self.clicked(str(i+1)), 
                        padx = 30, pady = 30)
            b1.grid(row = int(i/3 + 1), column = i%3, sticky="WE")
            
        zero = Button(button_frame, text = "0", font = button_font, command = lambda: self.clicked("0"), padx = 30, pady = 30)
        zero.grid(row = 4, column = 0, sticky="WE")

        clear = Button(button_frame, text = "C", font = button_font, command = self.clear_all, padx = 30, pady = 30)
        clear.grid(row = 4, column = 1, sticky="WE")

        equal = Button(button_frame, text = "=", font = button_font, command = self.equal_click, padx = 30, pady = 30)
        equal.grid(row = 4, column = 2, sticky="WE")
            
        add = Button(button_frame, text = "+", font = button_font, command = lambda: self.op_click("+"), padx = 30, pady = 30)
        add.grid(row = 1, column = 3, sticky="WE")
        minus = Button(button_frame, text = "-", font = button_font, command = lambda: self.op_click("-"), padx = 30, pady = 30)
        minus.grid(row = 2, column = 3, sticky="WE")
        mul = Button(button_frame, text = "*", font = button_font, command = lambda: self.op_click("*"), padx = 30, pady = 30)
        mul.grid(row = 3, column = 3, sticky="WE")
        div = Button(button_frame, text = "/", font = button_font, command = lambda: self.op_click("/"), padx = 30, pady = 30)
        div.grid(row = 4, column = 3, sticky="WE")

        root.mainloop()

if __name__=="__main__":
    Calculator()