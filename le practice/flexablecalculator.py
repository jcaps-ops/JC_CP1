#jc 2nd flexable calculator

import math

def calc(want, *numbers):
   #write out all the if conditions for each one based on a value
   #Then call the way to do it
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
#Get what the user wants to do
def wants():
    playerinput = input("Which of these do you want to do (1 -sum 2-avarge 3-max 4-min 5-product)")
    return playerinput


testlist = []
while True:
    numimput = input("what number to add(N to stop)")
    #check if the value can be added 
    if numimput.isnumeric():
        numimput = float(numimput)
        testlist.append(numimput)
        #Break off if it is the accepted answer
    if numimput == "n":
        break
#Call a function to do the calculation 
plywants = wants()

#Display the output of the user
print(calc(plywants,testlist))