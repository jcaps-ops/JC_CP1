#JC 2nd this is for a ruletee wheel

money = 100
bet = 0
bet_location = "white"

import random

for x in range (1,100):
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

    

