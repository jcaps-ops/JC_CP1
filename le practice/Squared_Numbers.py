#jc squared numbers 2nd
import time


numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21] #Store the list of it

squared = list(map( lambda num,: num**2, numlist)) #make the map function to square it

for i, num in enumerate(numlist): #make a list and a loop
   
    print(f"{num} squared is {squared[i]}")  #display the two things toghter 
    time.sleep(0.1)