#Jc 2nd this is a rouglike but with money


import random

currentpath = "dice"
branchpath1 = ""
branchpath2 = ""
pathrand = 0
money = 100
boonbet = 0
boons = []
potentailboonname = ["double trouble","money laundering","bonus check"]
potentailbooncost = [60, 120, 70]

def pathgen():
    global currentpath
    pathrand = random.randint(1,5)
    global branchpath1
    if pathrand == 1:
        branchpath1 = "dice"
    if pathrand == 2:
        branchpath1 = "slot machine"
    if pathrand == 3:
        branchpath1 = "blackjack" 
    if pathrand == 4:
        branchpath1 = "wheel"
    if pathrand == 5:
        branchpath1 = "store"
    pathrand = random.randint(1,5)
    global branchpath2
    if pathrand == 1:
        branchpath2 = "dice"
    if pathrand == 2:
        branchpath2 = "slot machine"
    if pathrand == 3:
        branchpath2 = "blackjack" 
    if pathrand == 4:
        branchpath2 = "wheel"
    if pathrand == 5:
        branchpath2 = "store"
    

    print(f"---------------{branchpath1}----")
    print(f"--{currentpath}-----------------")
    print(f"---------------{branchpath2}----")

    

    p_choice = input("Which path do you want to take (W or S):")

    if p_choice == "w":
        currentpath = branchpath1
        print(currentpath)
    elif p_choice == "s":
        currentpath = branchpath2
        print(currentpath)
    else:
        print("Wrong pathway")

def pathchoice():
    global currentpath
    if currentpath == "dice":
        dicegame()
    if currentpath == "slot machine":
        slotmachinegame()
    if currentpath == "blackjack":
         blackjackgame()
    if currentpath == "wheel":
         wheelgame()
    if currentpath == "store":
        store()


def dicegame():
    global money
        
    global boonbet
    boonbet = 0
    p_roll = 0
    D_roll = 0


    #You Draw the card

    print(f"Your current money is {money}")

    boonbet = input("How much would you like to bet:")
    boonbet = int(boonbet)

    p_roll = random.randint(1,6)
    D_roll = random.randint(1,6)
    D_roll = str(D_roll)
    p_roll = str(p_roll)

    print(f"You rolled a {p_roll}")
    print(f"The Dealer rolled a {D_roll}")

    if p_roll > D_roll:
        calcboon()
        money += boonbet * 2
    if p_roll < D_roll:
        calcboon()
        money -= boonbet

def slotmachinegame():
    global money
    bet = 0

    slot1 = ""
    slot2 = ""
    slot3 = ""

    randomvalue = random.randint(1,5)
    if randomvalue == 1:
        slot1 = "X"
    if randomvalue == 2:
         slot1 = "O"
    if randomvalue == 3:
        slot1 = "V"
    if randomvalue == 4:
        slot1 = "Z"
    if randomvalue == 5:
         slot1 = "W"

    randomvalue = random.randint(1,5)
    if randomvalue == 1:
            slot2 = "X"
    if randomvalue == 2:
            slot2 = "O"
    if randomvalue == 3:
            slot2 = "V"
    if randomvalue == 4:
            slot2 = "Z"
    if randomvalue == 5:
            slot2 = "W"

    randomvalue = random.randint(1,5)
    if randomvalue == 1:
            slot3 = "X"
    if randomvalue == 2:
            slot3 = "O"
    if randomvalue == 3:
            slot3 = "V"
    if randomvalue == 4:
            slot3 = "Z"
    if randomvalue == 5:
            slot3 = "W"

    bet = input("How Much do you want to bet:")
    bet = int(bet)
    print(f"---{slot1}---{slot2}---{slot3}---")

    if slot1 == slot2 and slot2 == slot3:
                money += bet * 3
    elif slot1 == slot2 or slot2 == slot3:
                money += bet
    else:
                money -= bet
        
def blackjackgame():
      
    global money
    bet = 0
    total = 0
    is_playing = True
    d_total = 0

    
    print(f"the anount of money you have is {money}")
    bet = input("How much do you want to bet:")
    bet = int(bet)

    while bet > money:
            print("You do not have enough money to bet that")
            bet = input("How much do you want to bet:")
            bet = int(bet)

    total = 0

    total +=  random.randint(1,10)
    total +=  random.randint(1,10)

    print(f"Your total is {total}")

    is_playing = True

    while is_playing == True:
        p_action = input("Would you like to hit or stand:")

        if p_action == "hit":
            total +=  random.randint(1,10)
            print(total)

            if total > 21:
                total = 0
                print("You busted")
                print("what")
                is_playing = False

        elif p_action == "stand":
                print("what")
                is_playing = False
        else:
                print("That is not an acceptible option")

    d_total = 0

    while d_total < 17:
        d_total += random.randint(1,10)

        if d_total > 21:

            d_total = 0

    print(f"The dealers total is {d_total}")

    if total > d_total:
        money += bet
        print("You won")
    if total == d_total:
        print("You both tied")
    if total < d_total:
        print("You lost")
        money -= bet

def wheelgame():
    global money
    bet = 0
    bet_location = "white"

    print(f"This is the amount of money you have {money}")
    bet = input("How much would you like to bet:")
    bet_location = input("What color are you betting on(black-red-green):")
    bet = int(bet)

    wheelspin = random.randint(1,101)
    wheelcolor = ""
    if wheelspin < 51:
            wheelcolor = "black"
    if wheelspin > 50 and wheelspin < 101:
            wheelcolor = "red"
    if wheelspin == 101:
            wheelcolor = "green"
        
    print(f"The wheel landed on a {wheelcolor}")

    if wheelcolor == bet_location:
            money += bet * 2
            print("You won")
            if wheelcolor == "green":
                money += bet * 2
    else:
            money -= bet
            print("You lost")

def store():
    global money
    global potentailboonname
    global potentailbooncost

    boonrand1 = random.randint(0,2)
    print(boonrand1)
    storeoption1name = potentailboonname[boonrand1]
    storeoption1cost = potentailbooncost[boonrand1]

    boonrand2 = random.randint(0,2)
    storeoption2name = potentailboonname[boonrand2]
    storeoption2cost = potentailbooncost[boonrand2]
    global boons

    print("The options at the store")
    print(f"The first option is {storeoption1name} it costs {storeoption1cost} dollars")
    print(f"the second option is {storeoption2name} it costs{storeoption2cost} dollars")
    plyerinput = input("If you want to buy an option please input the number.If you do not want to buy one type n:")
    if plyerinput == "1":
         if money >= storeoption1cost:
              boons.append(storeoption1name)
              money -= storeoption1cost
              potentailboonname.pop(boonrand1)
              potentailbooncost.pop(boonrand1)
    elif plyerinput == "2":
         if money >= storeoption2cost:
              boons.append(storeoption2name)
              money -= storeoption2cost
              potentailboonname.pop(boonrand2)
              potentailbooncost.pop(boonrand2)
    elif plyerinput == "n":
         pass
    else:
         print("not excepted input skill issue")
    
    print(boons)
    print(potentailbooncost)
    print(potentailboonname)
    
    
def calcboon():
    global boonbet
    global boons
    if "double trouble" in boons:
        boonbet * 2


store()
dicegame()
playing = True
while playing == True:
    pathgen()
    pathchoice()
    

