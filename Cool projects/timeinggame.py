#JC 2nd time game

import random
pos1 = "-"
pos2 = "-"
pos3 = "-"
pos4 = "-"
pos5 = "-"
pos6 = "-"
pos7 = "-"
pos8 = "-"
pos9 = "-"

grid1 = pos1+pos2+pos3
grid2 = pos4+pos5+pos6
grid3 = pos7+pos8+pos9

errorslector = [1,2,3,4,5,6,7,8,9,"no"]
print(random.choice(errorslector))
print(grid1)
print(grid2)
print(grid3)

for x in range(1,100):
    print("test")
    errorslector = [1,2,3,4,5,6,7,8,9,"no"]

    pos1 = "-"
    pos2 = "-"
    pos3 = "-"
    pos4 = "-"
    pos5 = "-"
    pos6 = "-"
    pos7 = "-"
    pos8 = "-"
    pos9 = "-"

    if errorslector == 1:
        pos1 = "_"
    if errorslector == 2:
        pos2 = "_ "  
    if errorslector == 3:
        pos3 = "_"
    if errorslector == 4:
        pos4 = "_ "
    if errorslector == 5:
        pos1 = "_"
    if errorslector == 6:
        pos2 = "_ "  
    if errorslector == 7:
        pos3 = "_"
    if errorslector == 8:
        pos4 = "_"
    if errorslector == 9:
        pos1 = "_"
    
    print(grid1)
    print(grid2)
    print(grid3)
    