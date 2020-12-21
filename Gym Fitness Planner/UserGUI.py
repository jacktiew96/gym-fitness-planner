from Tkinter import *
from Tkinter import Tk, Frame, BOTH
import sys
import os
import time
import random
from random import randint
import tkMessageBox
from tkMessageBox import *
import Tkinter

class GUI(Frame):

    def __init__(self, parent = None):

        Frame.__init__ (self)
        self.pack()
        self.master.title("User GUI")
        self.master.minsize(1000,500)       

        #mainframe
        mainframe=Frame(self).pack(fill=BOTH, expand=TRUE, ipadx=5)

        #predefined value
        global Frame2
        TotalCost=0
        showBMI=0
        ticketnumber=0
        
        now = time.asctime( time.localtime(time.time()) )
        Label (mainframe, text="Login since: " + str(now)).pack(anchor=NE, padx=5)

        global TotalCost

        Button(mainframe, text="Checkout", command = checkout).pack(anchor=SE ,padx=10 , pady=5, side=BOTTOM)            
        
        Frame1 = LabelFrame(mainframe)
        Frame1.pack(side = LEFT, pady=20, padx=20, fill=BOTH,  expand=TRUE)

        #bmi       
        bmiframe = LabelFrame(Frame1, text="BMI")
        bmiframe.pack(fill=BOTH,  expand=TRUE, padx=10, ipady=3)

        global TotalBMI
        global weightentry
        global heightentry
        global showBMI
        global ticketnumber

        Label(bmiframe, text="Weight (kg): ").pack(side = TOP)

        weightentry = Entry(bmiframe, bd=5)
        weightentry.pack()

        Label(bmiframe, text="Height (m): ").pack(side = TOP)

        heightentry = Entry(bmiframe, bd=5)
        heightentry.pack()
        
        Button(bmiframe, text="Calculate", command=calcbmi).pack(pady=2)

        suggestionframe = LabelFrame(Frame1, text="Suggestion")
        suggestionframe.pack(fill=BOTH,  expand=TRUE, padx=10,pady=8)

        Label(suggestionframe, text="BMI < 18.5\nUnderweight. Please seek advise from doctor.\n").pack()

        Label(suggestionframe, text="BMI = 18.5-25\nEctomorph can do more reps at relative intensities than other body types. Longer rest periods between\nsets (3-5 minutes). More frequent workouts. Because they recover faster, the ectomorph needs to work out\nmore than the other body types. Ectomorphs can even get away with 3-4 full-body workouts a week.\nEctomorphs should avoid cardio and pay VERY close attention to their diet.\n").pack()

        Label(suggestionframe, text="BMI = 25-30\nA 3-4 day a week split should suffice. Break up the workouts to focus on certain body parts\neach day (ex. Monday-bench, chest,shoulders. Tuesday-squat, quads, hamstrings, glutes. Etc.)\nMix in some cardio (or circuittraining) to keep off any fat. Mesomorphs gain muscle quickly but \nalso have a propensity to gain fat.\n").pack()

        Label(suggestionframe, text="BMI > 30\nCompound movements are the base for an endomorph's program. Circuit training is ideal for endomorphs.\nPick 3-5 exercises and go through each one with no rest between exercises. Rest 2 minutes between circuits. \nHIIT is very important to aid in fat loss. Diet is crucial to the endomorph, minimize the carbs and\nchoose fats wisely.").pack()

        #right frame
        Frame2 = LabelFrame(mainframe)

        #membership

        membershipframe = LabelFrame(Frame2, text="Membership")
        membershipframe.pack(fill=BOTH, expand=TRUE, padx=10)

        global var
        var = IntVar()
        R1 = Radiobutton(membershipframe, text="RM300/30 Days", variable=var, value=1).pack(anchor = W)
        R2 = Radiobutton(membershipframe, text="RM550/90 Days", variable=var, value=2).pack(anchor = W)
        R3 = Radiobutton(membershipframe, text="RM750/180 Days", variable=var, value=3).pack(anchor = W)
        R4 = Radiobutton(membershipframe, text="RM1000/365 Days", variable=var, value=4).pack(anchor = W)

        Button(membershipframe, text="Buy This!", command=calcmembership).pack()

        Label(Frame2, text="Note: Only press 'Buy Now' button \nonce after confirmed the selection. You can buy multiple memberships and\n nutrient supplements by repeating the same steps.\n").pack(side=BOTTOM, fill=BOTH, ipadx=10)

        #nutrient supplement  product list
        global musclebooster
        global vitaminbooster
        global proteinbooster
        
        nutrientsupplementframe = LabelFrame(Frame2, text="Nutrient Supplements")
        nutrientsupplementframe.pack(expand=TRUE, fill=BOTH, padx=10,pady=8)
        
        Label(nutrientsupplementframe, text="Muscle Booster (RM90/pcs)").pack(pady=5)

        musclebooster= Spinbox(nutrientsupplementframe, from_=0, to=10)
        musclebooster.pack()

        Label(nutrientsupplementframe, text="Vitamin Booster (RM100/pcs)").pack(pady=5)

        vitaminbooster = Spinbox(nutrientsupplementframe, from_=0, to=10)
        vitaminbooster.pack()
    
        Label(nutrientsupplementframe, text="Mineral Booster (RM110/pcs)").pack(pady=5)

        proteinbooster = Spinbox(nutrientsupplementframe, from_=0, to=10)
        proteinbooster.pack()

        Button(nutrientsupplementframe, text="Buy This!", command=calcnutrient).pack(pady=12)
    
def calcbmi():
    global weightentry
    global heightentry
    global showBMI
    global TotalBMI
    global Frame2
    GetWeight=weightentry.get()
    GetHeight=heightentry.get()
    TotalBMI = float(float(GetWeight)/(float(GetHeight)*float(GetHeight)))
    showBMI = Label(text="BMI calc. history:\nYour BMI is: " + str(round(TotalBMI, 1))).pack()
    f = open('state.txt','r')
    verifyshopstatus = f.readline()
    if verifyshopstatus == "Enabled":
        Frame2.pack(side = RIGHT, pady=20, padx=20, expand=TRUE, fill=BOTH)
    elif verifyshopstatus == "Disabled":
        Frame2.pack_forget()

def calcmembership():
    global var
    global TotalCost
    radiovar = var.get()
    if radiovar == 1:
        TotalCost = TotalCost + 300
    elif radiovar == 2:
        TotalCost = TotalCost + 550
    elif radiovar == 3:
        TotalCost = TotalCost + 750
    elif radiovar == 4:
        TotalCost = TotalCost + 1000

def calcnutrient():
    global musclebooster
    global vitaminbooster
    global proteinbooster
    global TotalCost
    muscle = int(musclebooster.get())
    vitamin = int(vitaminbooster.get())
    protein = int(proteinbooster.get())
    TotalCost = TotalCost + (muscle * 90)
    TotalCost = TotalCost + (vitamin * 100)
    TotalCost = TotalCost + (protein * 110)
    print TotalCost

def checkout():
    global TotalCost
    global ticketnumber
    if TotalCost > 0:
        ticketnumber=(randint(0,99999))
        tkMessageBox.showinfo("Order Confirmed", "Total cost is: RM" + str(TotalCost) + " and your ticket number is: " + str(ticketnumber) + ". Please wait until your ticket number is being called. Thank you.")
        os._exit(0)
    else:
        tkMessageBox.showinfo("Shopping cart empty", "See you next time!")
        os._exit(0)
        
def main():
    root = Tk()
    entry = GUI(root)
    entry.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()
