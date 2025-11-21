#jc 2nd puesdo code

#import math
import math
#Def factorial(num)
def factorial(num):
    #factors = []
    factors = []
    #while num > 0
    while num > 0:
        #factors.append(num)
        factors.append(num)
        #num -= 1
        num -= 1
    #return factors
    return factors
#while true:
while True:
    #Get user number
    num = input("What numbers do you want to imput")
    #if numbers !int or is negative:
    #Changed it to is not numeric not is int
    if not num.isnumeric():
        #Made it if statement afterwards after converting into a int
        #pass
        pass
    #else:
    else:
        num = int(num)
        if num < 0:
            pass
        else:
        #print(f"{number}, facotrio is{prod(factoral(numbers))}")
            print(f"{num}, factorial is: {math.prod(factorial(num))}")       