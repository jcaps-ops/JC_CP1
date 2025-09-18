#Jc 2nd a security system from a horror game

import random

currentcam = 1
camon = False
Needsreload = False
Refreshchance = 1
plyaction = ""

def breakdown():
    print("It brok oh")
    Needsreload = True
    print(Needsreload)


print("Welcome user to the H security cams system for help please type help in your terminal")
for X in range(1,100):
    #plyaction = input("Terminal input:") 
    if plyaction == "help":
        print("For turing on cam systems please enter: Cams")
        print("To Move on cameras please enter: A or D")
        print("To activate alarms please enter:E")
        print("To refresh please Enter:R")
        print("To go into tasks Enter:T")
        print("To Leave cameras please type EXIT")
    if plyaction == "Cams":
        camon = False
        currentcam = 1
        print("Basic cam layout")
    if plyaction == "D":
        if camon == True:
            currentcam += 1
            if currentcam > 5:
                currentcam = 1
            if currentcam == 2:
                print("Cam2 layout")
            if currentcam == 3:
                print("Cam3 layout")
            if currentcam == 4:
                print("Cam4 layout")
    if plyaction == "T":
        print("Tasks")
    if plyaction == "Exit":
        camon = False
    breakdown()