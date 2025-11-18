#jc 2nd flexable calculator

def calc(want, *numbers):
   if want == "1":
       revalue = sum(numbers[0])
   if want == "2":
       valuetotal = sum(numbers[0])
       revalue = valuetotal/ len(numbers[0])
   return revalue

def wants():
    playerinput = input("Which of these do you want to do (1 -sum 2-avarge 3-max 4-min 5-product)")
    return playerinput


testlist = []
while True:
    numimput = input("what number to add(N to stop)")
    #isnumeric
    if numimput.isdigit():
        numimput = float(numimput)
        testlist.append(numimput)
    if numimput == "n":
        break

print(testlist)
plywants = wants()

print(calc(plywants,testlist))