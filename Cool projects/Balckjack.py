#JC 2nd were making blackjack

import random

money = 100
bet = 0
total = 0
is_playing = True
d_total = 0

for x in range (1,100):
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
        money += bet
        print("You won")
    if total == d_total:
        print("You both tied")
    if total < d_total:
        print("You lost")
        money -= bet


    
