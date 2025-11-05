#Lets make money

import random

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
def marketbuy(money, itemstobuy, buyingitemscost,marketsize):
    print("Hello mercant what goods would you like to purcase")
    for x in range (0, marketsize):
        print(f"Item {x + 1} is {itemstobuy[x]} it costs {buyingitemscost[x]} coins")
marketgoods = randomizemarket1(maketsize,itemstobuy,buyingitemscost)
itemstobuy = marketgoods[0]   
buyingitemscost = marketgoods[1]
marketbuy(money,itemstobuy,buyingitemscost, maketsize)        
