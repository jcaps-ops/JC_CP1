#jc 2nd flexable calculator

import math

def calc(want, *numbers):
   if want == "1":
       revalue = sum(numbers[0])
   if want == "2":
       valuetotal = sum(numbers[0])
       revalue = valuetotal/ len(numbers[0])
   if want == "3":
       revalue = max(numbers[0])
   if want == "4":
       revalue = min(numbers[0])
   if want == "5":
       revalue = math.prod(numbers[0])
    
   return revalue

def wants():
    playerinput = input("Which of these do you want to do (1 -sum 2-avarge 3-max 4-min 5-product)")
    return playerinput


testlist = []
while True:
    numimput = input("what number to add(N to stop)")
    #isnumeric
    if numimput.isnumeric():
        numimput = float(numimput)
        testlist.append(numimput)
    if numimput == "n":
        break

print(testlist)
plywants = wants()

print(calc(plywants,testlist))