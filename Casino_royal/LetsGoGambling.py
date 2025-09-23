#JC 2nd Casino time

import random

money = 100
bet = 0 
debt = 0
p_roll = 0
D_roll = 0


#You Draw the card

for x in range(1,100):

    print(f"Your current money is {money}")

    bet = input("How much would you like to bet:")
    bet = int(bet)

    p_roll = random.randint(1,6)
    D_roll = random.randint(1,6)
    D_roll = str(D_roll)
    p_roll = str(p_roll)

    print(f"You rolled a {p_roll}")
    print(f"The Dealer rolled a {D_roll}")

    if p_roll > D_roll:
        money += bet * 2
    if p_roll < D_roll:
        money -= bet
    

    