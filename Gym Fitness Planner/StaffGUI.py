from Tkinter import *
from tkMessageBox import *
from Tkinter import Tk, Frame, BOTH
import os

class GUI(Frame):

    def __init__(self, parent = None):

        Frame.__init__ (self)
        self.pack()
        self.master.title("Staff GUI")
        self.master.minsize(width=100,height=70)

        
        radioframe = LabelFrame(self, text="Radio").pack(anchor = CENTER, expand = TRUE, fill=BOTH)
        global var
        var = IntVar()
        storestatus = Label(radioframe, text="Store status:").pack(padx=15)
        R1 = Radiobutton(radioframe, text="Enable", variable=var, value=1).pack(padx=15, anchor = W)
        R2 = Radiobutton(radioframe, text="Disable", variable=var, value=2).pack(padx=15, anchor = W)
        Button(radioframe, text="Apply", command=saveshopstatus).pack(padx=15, pady=10)

def saveshopstatus():
    global var
    shopvar = var.get()
    if shopvar == 1:
        text = "Enabled"
        with open("state.txt", "w") as f:
            f.write(text)
            os._exit(0)
    elif shopvar == 2:
        text = "Disabled"
        with open("state.txt", "w") as f:
            f.write(text)
            os._exit(0)
            
def main():
    root = Tk()
    entry = GUI(root)
    entry.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()

