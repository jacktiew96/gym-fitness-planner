from Tkinter import *
from tkMessageBox import *
from Tkinter import Tk, Frame, BOTH
import os
import sys

class GUI(Frame):

    def __init__(self, parent = None):

        Frame.__init__(self)
        self.pack()
        self.master.title("Gym Fitness Planner")
        self.master.minsize(width=250, height=100)
        
        #instruction text for user
        mainframe = Frame(self)
        mainframe.pack(ipady=2)
      
        Label(mainframe,text = "Who Are You?").pack()
        Button(mainframe,text="Customer", command = UserUserSelection, width=7,height=2).pack(pady=3)
        Button(mainframe,text="Staff", command = UserStaffLogin, width=7,height=2).pack(pady=3)
        
def UserUserSelection():
        os.system ("UserGUI.py")
        os._exit(0)     

def UserStaffLogin():
        os.system ("StaffLogin.py")
        os._exit(0)    

def main():
    root = Tk()
    entry = GUI(root)
    entry.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()
