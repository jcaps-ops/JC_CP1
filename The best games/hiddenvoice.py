#Jc 2nd this is testing a tick system for speed
import time

tickrate = 0

def tickratetimers(x):
    for y in range (0, x):
        time.sleep(0.1)
        y += 1
    print("Tick timer")

def clock(tickrate):
    tickrateinput = input("What speed would you like to do(f, m, s)")
    if tickrateinput == "f":
        tickrate = 5
    elif tickrateinput == "m":
        tickrate = 10
    elif tickrateinput == "s":
        tickrate = 15
    return tickrate
while True:
    tickratetimers(tickrate)
    playeraction = input("What would you like to do")
    if playeraction == "clock":
        tickrate = clock(tickrate)
    

