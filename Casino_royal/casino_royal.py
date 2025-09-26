#Jc 2nd this is a rouglike but with money


import random

currentpath = "dice"
branchpath1 = ""
branchpath2 = ""
pathrand = 0
money = 150
boonbet = 0
boons = []
potentailboonname = ["double trouble","money laundering","bonus check","Basic inssurance","diamond inssurance","Daily Double", "Daily Triple"]
potentailbooncost = [60, 120, 70, 100, 180, 50, 100]
global islost
islost = False
levelCounter = 10

def pathgen():
    global currentpath
    global islost
    islost = False
    pathrand = random.randint(1,5)
    global branchpath1
    if pathrand == 1:
        branchpath1 = "dice--------"
    if pathrand == 2:
        branchpath1 = "slot machine"
    if pathrand == 3:
        branchpath1 = "blackjack---" 
    if pathrand == 4:
        branchpath1 = "wheel-------"
    if pathrand == 5:
        branchpath1 = "store-------"
    pathrand = random.randint(1,5)
    global branchpath2
    if pathrand == 1:
        branchpath2 = "dice--------"
    if pathrand == 2:
        branchpath2 = "slot machine"
    if pathrand == 3:
        branchpath2 = "blackjack---" 
    if pathrand == 4:
        branchpath2 = "wheel-------"
    if pathrand == 5:
        branchpath2 = "store-------"
    

    print(f"---------------{branchpath1}----")
    print(f"--{currentpath}-------------------------")
    print(f"---------------{branchpath2}----")

    

    p_choice = input("Which path do you want to take (W or S):")

    if p_choice == "w":
        currentpath = branchpath1
    
    elif p_choice == "s":
        currentpath = branchpath2
        
    else:
        print("Wrong pathway")

def pathchoice():
    global currentpath
    
    if currentpath == "dice--------":
        dicegame()
    if currentpath == "slot machine":
        slotmachinegame()
    if currentpath == "blackjack---":
         blackjackgame()
    if currentpath == "wheel-------":
         wheelgame()
    if currentpath == "store-------":
        store()


def dicegame():
    global money
    global boonbet
    global islost
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
        islost = True
        calcboon()
        money -= boonbet

def slotmachinegame():
    global money
    global boonbet
    global islost
    boonbet = 0

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
    print(f"You have {money} dollars")
    boonbet = input("How Much do you want to bet:")
    boonbet = int(boonbet)
    print(f"---{slot1}---{slot2}---{slot3}---")

    if slot1 == slot2 and slot2 == slot3:
                calcboon()
                money += boonbet * 3
    elif slot1 == slot2 or slot2 == slot3:
                calcboon()
                money += boonbet
    else:
                islost = True
                calcboon()
                money -= boonbet
        
def blackjackgame():
      
    global money
    global boonbet
    global islost
    boonbet = 0
    total = 0
    is_playing = True
    d_total = 0

    
    print(f"the anount of money you have is {money}")
    boonbet = input("How much do you want to bet:")
    boonbet = int(boonbet)

    while boonbet > money:
            print("You do not have enough money to bet that")
            boonbet = input("How much do you want to bet:")
            boonbet = int(boonbet)

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
                is_playing = False

        elif p_action == "stand":
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
        calcboon()
        money += boonbet
        print("You won")
    if total == d_total:
        calcboon()
        print("You both tied")
    if total < d_total:
        print("You lost")
        islost = True
        calcboon()
        money -= boonbet

def wheelgame():
    global money
    global boonbet
    global islost
    boonbet = 0
    bet_location = "white"

    print(f"You have {money} dollars")
    boonbet = input("How much would you like to bet:")
    bet_location = input("What color are you betting on(black-red-green):")
    boonbet = int(boonbet)

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
            calcboon()
            money += boonbet * 2
            print("You won")
            if wheelcolor == "green":
                calcboon()
                money += boonbet * 2
    else:
            calcboon()
            islost = True
            money -= boonbet
            print("You lost")

def store():
    global money
    global potentailboonname
    global potentailbooncost

    boonrand1 = random.randint(0,len(potentailbooncost) - 1)
    print(boonrand1)
    storeoption1name = potentailboonname[boonrand1]
    storeoption1cost = potentailbooncost[boonrand1]

    boonrand2 = random.randint(0,(len(potentailbooncost) - 1))
    storeoption2name = potentailboonname[boonrand2]
    storeoption2cost = potentailbooncost[boonrand2]
    global boons

    print(f"You have {money} dollars")
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
    global money
    global boonbet
    global boons
    if "double trouble" in boons:
        boonbet * 2
        
    if "bonus check" in boons:
         money += 5
         
    if "money laundering" in boons:
        
         monbet = random.randint(1,5)
         if monbet == 1:
              money += 30
              print(f"money laundering sucsess you now have{money}")
        
    if "Basic inssurance" in boons:
         
         if islost == True:
            bi = boonbet/4
            bi = int(bi)
            money += bi
            print(f"Your Basic insurance kicked in saving you {bi} dollars")
    
    if "diamond inssurance" in boons:
         
         if islost == True:
            bi = boonbet/2
            bi = int(bi)
            money += bi
            print(f"Your Diamond insurance kicked in saving you {bi} dollars")
    
    if "Daily Double" in boons:
         chance = random.randint(1,20)
         if chance == 1:
              print(f"You stared with {money}")
              money * 2
              print("Your daily double kicked in")
    if "Daily Triple" in boons:
         chance = random.randint(1,20)
         if chance == 1:
              print(f"You stared with {money}")
              money * 3
              print("Your daily Triple kicked in")
    

def jackblack():
    #this is baccarate 
    global money
    global boonbet
    curentmoney = money
    global islost
    print("*********************************##%%%%%%%%%%%#######%#########%%###########*#######%%%#########%%%%%%%%%%%%%%#################################*****##***************")
    print("*++++++************###############%%%#%%%%##########################%###############%%%%%#######%%%%%%%%%%%%###################################*****##***************")
    print("+++++*++********###########################%##############%%###############*####**===-==+++####*##%%%%%%%%%%%%%%%%%##########################***********************+")
    print("+++++++++*******###########################%##########%###%################*+====+**+--:.::::::=*##%#%%%%%%%%%%%%#%%########################****#**************++++++")
    print("+++++++++++*******#####**###############################################*+=-=+#%%@@%%#*--+++-::..:+=*##%%%%%%%%####%#####################********************++++++++")
    print("++++++++++++*********##################%##############################*===+*#%%%%#**###***##*+-....:+#*%%%%########################*#####******************++++++++++")
    print("++++++++++++************#*#############################%###########**==++*##%%%*++=========++++-:....:-*##%##%%###########################*************++++++++++++++")
    print("==+++++++++***++**********###*#############**#*###################*+=+**##%%%#*++============+++*::::...-#%%%%%%%#########################*************++++++++++++++")
    print("===+*+=+++++*+++***************########*###**####################+=+**##%%%##+++============++++*+--:....=##%%%%###################******************++++++++++++++++")
    print("***=-=====++++++********************##**######################*#+++**##%%###*++===============+++**+=:...:-##%%#############***##********************++++++++++++++++")
    print("*=++=+***--=++++++*++****************#*******##*****##########*+-=***#%%##***#***++++++++++++**++***=-::::=################*****#*******************+++++++++++++++++")
    print("*==+*****=-==*******+==+******************************#######++===**##%%%****+++****++++*###*****+*##*:::::=###############****##*********++*********++++++++++++++++")
    print("+++*********+=-==+**===+************************+**+****##**+====++*#%%%#***###%##**+=+*####***++++#%#+-:...+*#############***###******##**+******+*+++++++++++++++++")
    print("**********+**+-=-+*+==+++++*******************++*******##*#*======+##%%#*+++++++++++==++***##***+++*%%+-:.....-############********###******++***++++++++++++++++++++")
    print("**********=-+=-==++*++++++++==*******************++*****+**=====+**#%%%%*+++=====+++=++++++++++==++*%%+-::..::-*############**********+******++*+++++++++++++++++++++")
    print("+*********=----+++++++++++++++=++=+*++++***********+******+=-===+*##%%#**++++++++*##+****+====+++++###*-::..:.-+###*#######*****####**++*****++++++++++++++++++++++++")
    print("+++++++++==++**+-=+++++*******++=++*++++-==-++++=********+=====++*###**+***++++*++**##**+*+++++++++*###*--:..::=+*#########**#########*+***++*+++++++++++++++++++++++")
    print("=-+==+++=+*****+-===+++++********++*****+++=-=+*=++**+=+++++++=+++**+++++**++*****###**+++*+++++++++**#**-.....:-*#####****#########*****+++**+++++++++***++++++++++=")
    print("--+++++==**+*++***+==-===++*****+++++******+==:+********+-=++=+*++++++++******##########**+*+**++++++=+**:::::.::*#######################*++****+++++++**++++++++++++")
    print("+==+++***************===-=-=+*****************--+*******+++==++++**+++++********++**+**##***++*++++====++=.:.:::-***###################***+++***++*++++++++++++++++++")
    print("+++***********************+--++***************=:-********+**++++*#*+++++***#*++++++*+*****#*++++++========-::::--+++**#################*****++****+++++++++++++++++++")
    print("****++********************+==+***************+-:=***##*****+=++***++++++**##*++++++++**++****++++========-::::::**+*##*+*##############*****++++*++++++===+++++++++++")
    print("**********************++++***************+++=+*--==##**+=======+*++++++**###**+++++++*****###*++++===-===-:...:-+++*###################******+++++++++++====++++=====")
    print("+*********************+++==+****************--*:-==***#####+=-=+++***+**##*#**+=+++++**##%%%##*++++====++-::::::*****###############*********++++++++++++++==========")
    print("*******++++++++*****+*****-=****************==***++++++******+==+*###*#***+**+=+++++***#%%#%%##*++=====+=-::::=*=******############*************+++++++++++++=====+==")
    print("******+++++++++++*********++***********************#****####*+==+*#######**+++++=+++****##%%%%##*+++=-=---:--=-=+++==+****#*********************++----:::::::::::::-:")
    print("++++++*********++++**+++++****++++++++++++*********#****##**+:-+*####%%##***++++++++**#*#%%%%%%##%####*=-:::.:::::::::::::::-+******************+*********+=--::::::-")
    print("++*+++++=---------------------------::-----=----=--=*+-:-=******##########***++********##%%%%%%%%%######*=::.::::::::-:::::::::::::---+**************#****####*******")
    print("*******++-----=----==---=----=---=--------=---=----=+************#############%%#########%%%%%%%%#########*+--::::::=********###*****************###*##*######*****#*")
    print("*****+++*+------==--=--=----=+++++===-=+=+=++=+++=****************#*#######%%%%%%%%%%%%%%%%%%%%#############***+----:::+**##*#*#***********+++++*********####****##*#")
    print("***+++**+********+*+++++++++++++++++++++**++++++*********************########%%%%%%%%%%%%%%%%#################****+++---::+#####****#***+++********#*####***********#")
    print("+++++***++**+++++++++++++++++++++++++*++++++++*********************#*##########%%%%%%%%%%%%#################************+-::*#***#*###**++++++++*##**#######*********")
    print("****++**++**+++++++++++++++++++++++++++++++++**********************##*#######################################*************+-::+**#####********++*####################")
    print("*+++****+++*++++++++++++++++++++++++++++++++***********************########################################****#******###****=:-######***********##**################")
    print("************++++++++++++++++++**++***++++++********************##**#########################################*##*#***##########*--#*###**********######**#############")
    print("********++**+++++++++++++++++++*******+***+*********************#***###########################################################+:+####**********#####################")
    print("***##*******++++*******+++***************************************#*############################################################*-:*##***********#####################")
    print("***###**++**++***++******************************##************#*###############################################################*-:*##************###################")
    print("***##***************************************#**###************#*#################################################################=:-#***********################%%%%%")
    print("***###**************************************#####**************##################################################################*-:+#**********#################%%%%")
    print("#######**********************************#######***********#*#####################################################################*--#*******#*####################%%")
    print("########***#***********************#****########*********##########################################################################+:+*******################%%%#%%%%")
    print("*****###***#********************#******############**#############################################################%%####%##########*--*********##############%%%%%%%%")
    print("***********#**************************##########**#################################################################%%##%%###########+---------=***##########%%%%%%%%%")
    print("###*++*#***#************************##########%#*##################################################################%%%#%%%############=-----=***********###%%%%%%%%%%")
    print("########***#***********************###########%#*############################################################%%%%%#%%%%%%%###########*--==+*******###########%%%%%%%%")
    print("**#*###****##********#*************###########%#################################################################%%%%%%%%%%%###########+-=******##########%%%%#####%%%")
    print("+**######**##*#*****##***********############%%##################################################################%%%%%%%%%%%%#########*+-+###############%%%%%%%%%%%%")
    print("+======+***##*#******###*********###########%%%###################################################################%%@%%%%%%%%%%#########*+###%%%%%%%%%%%%%%%@@@%%%%%%")
    print("==++*******##*#*****#************##%#####%%%%%%###################################################################%%%%%%%%%%%%%##########+#%%%%%%%%%%%%%%%@%@@%%%%%%%")
    print("A chalager approches you he challenges you to baccarate")
    print("It is time to face your first boss jack black you must get twice your current amount of money")
    while money < curentmoney * 2:   
            print(f"you have {money} dollars")
            boonbet = input("How much would you like to bet:")
            total = 0
            total += random.randint(1,9)
            total += random.randint(1,9)

            if total >= 10:
                total -= 9

            print(total)

            p_action = input("would you like to stand or hit")
            if p_action == "hit":
                total += random.randint(1,9)
                if total >= 10:
                    total -= 9
            pdist = 9 - total
            dealertotal = random.randint(5,9)
            ddist = 9 - dealertotal

            print(f"You got a {total}")
            print(f"Jack black got a {dealertotal}")

            ddist = abs(ddist)
            pdist = abs(pdist)
            
            boonbet = int(boonbet)
            if pdist < ddist:
                print("you won")
                calcboon()
                money += boonbet
            elif pdist == ddist:
                 calcboon()
            else:
                 print("You lose")
                 calcboon()
                 money -= boonbet
        


    

playing = True
while playing == True:
    pathgen()
    pathchoice()
    levelCounter -= 1
    if levelCounter <= 0:
        input("Are you ready to countinue")
        jackblack()

