#Lets make money

import random
import time

money = 100
items = []
maketsize = 2
itemstobuy = []
buyingitemscost = []

def randomizemarket1(marketsize,itemstobuy,buyingitemscost):
    for x in range (0, marketsize):
        ranval = random.randrange(1,4)
        if ranval == 1 and "Wheat" not in itemstobuy:
            itemstobuy.append("Wheat")
            buyingitemscost.append(2)
        if ranval == 2 and "wood" not in itemstobuy:
            itemstobuy.append("wood")
            buyingitemscost.append(3)
        if ranval == 3 and "leather" not in itemstobuy:
            itemstobuy.append("leather")
            buyingitemscost.append(3)
        if ranval == 4 and "Wine" not in itemstobuy:
            itemstobuy.append("Wine")
            buyingitemscost.append(8)
    return(itemstobuy, buyingitemscost,ranval)
def marketbuy(money, itemstobuy, buyingitemscost,marketsize,items):
    print("Hello mercant what goods would you like to purcase")
    time.sleep(0.1)
    for x in range (0, marketsize):
        print(f"Item {x + 1} is {itemstobuy[x-1]} it costs {buyingitemscost[x-1]} coins")
        time.sleep(0.1)
    buying = True
    while buying:
        playeranswer = input("What goods would you like to buy.(Please input the number of the good or type N for no goods.): ")
        time.sleep(0.1)
        isanumber = playeranswer.isdigit()
        if isanumber == True:
            playeranswer = int(playeranswer)
            if playeranswer <= maketsize:
                money -= buyingitemscost[playeranswer - 1]
                print(f"You have bought some {itemstobuy[playeranswer - 1]}")
                time.sleep(0.1)
                items.append(itemstobuy[playeranswer - 1])
                print(f"Your iventory now is {items}")
                time.sleep(0.1)
                print(f"You know have {money} gears ")
                time.sleep(0.1)
                playeranswer = input("Would you like to buy again(type N for no)")
                time.sleep(0.1)
                print(playeranswer)
                if playeranswer == "N":
                    buying == False
        if playeranswer == "N":
            buying == False
        


marketgoods = randomizemarket1(maketsize,itemstobuy,buyingitemscost)
itemstobuy = marketgoods[0]   
buyingitemscost = marketgoods[1]
marketbuy(money,itemstobuy,buyingitemscost, maketsize,items)        
