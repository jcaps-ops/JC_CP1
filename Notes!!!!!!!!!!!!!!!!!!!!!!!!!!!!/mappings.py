#Jc 2nd mapping 

numbered = [1,2,3,4,5,6,7,8]
divided = []
'''

for num in numbered:
    divided.append(num/2)

for i, num in enumerate(numbered):
    print(f"{num} divided is {divided[i]}")

 lambda num,: num/2
'''

divided = list(map( lambda num,: num/2, numbered))

for i, num in enumerate(numbered):
    print(f"{num} divided is {divided[i]}")