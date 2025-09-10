#JC 2nd time game



import random


errorslector = [1,2,3,4,5,6,7,8,9,"no"]

score = 0

for x in range(1,100):
    

    #Setting up what can be randomly generated
    errorslector = [1,2,3,4,5,6,7,8,9,"no"]
    randvar = random.choice(errorslector)


    #Seting up the grid board
    pos1 = "1"
    pos2 = "2"
    pos3 = "3"
    pos4 = "4"
    pos5 = "5"
    pos6 = "6"
    pos7 = "7"
    pos8 = "8"
    pos9 = "9"

    # setting up the random error
    if randvar == 1:
        pos1 = "2"
    if randvar == 2:
        pos2 = "6"  
    if randvar == 3:
        pos3 = "7"
    if randvar == 4:
        pos4 = "12 "
    if randvar == 5:
        pos5 = "7"
    if randvar == 6:
        pos6 = "5 "  
    if randvar == 7:
        pos7 = "8"
    if randvar == 8:
        pos8 = "9"
    if randvar == 9:
        pos9 = "8"
    
    #Finializing the board 
    grid1 = pos1+pos2+pos3
    grid2 = pos4+pos5+pos6
    grid3 = pos7+pos8+pos9

    print(grid1)
    print(grid2)
    print(grid3)

    answer = input("report problems:")
    if answer != "no":
        answer = int(answer)

    if answer == randvar:
        score += 1
        print(score)
    else:
        print("you failed")


    