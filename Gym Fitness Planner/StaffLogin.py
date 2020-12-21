from Tkinter import *
from tkMessageBox import *
from Tkinter import Tk, Frame, BOTH
import tkMessageBox
import os
import sys

class GUI(Frame):

    def __init__(self, parent = None):

        Frame.__init__ (self)
        self.pack()
        self.master.title("Staff Login")
        self.master.minsize(width=200,height=120)

        #predefined value
        global usernameentry
        global passwordentry
        global username
        global password
        global database
        database=[    ['staff','1234'],['admin','4321']   ]        

        #login
        self.instructionFrame = Frame(self)
        self.instructionFrame.pack()

        Label(self.instructionFrame, text="Username: ").pack()

        usernameentry = Entry(self.instructionFrame, bd=5)
        usernameentry.pack()
        
        Label(self.instructionFrame, text="Password: ").pack()

        passwordentry = Entry(self.instructionFrame, bd=5, show="*")
        passwordentry.pack()

        Button(self.instructionFrame, text="Login", command = self.loginbutton).pack()

    def loginbutton(self):
        global usernameentry
        global passwordentry
        global username
        global password
        global database
        username=usernameentry.get()
        password=passwordentry.get()
        if [username,password] in database:
            os.system ("StaffGUI.py")
        while [username,password]not in database:
            tkMessageBox.showinfo("Access Denied", "Please try again!").pack()
  
def main():
    root = Tk()
    entry = GUI(root)
    entry.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()
