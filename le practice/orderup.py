# JC order up 2nd


#A resturant
#This checks to see if the item is in the section then adds it to the users items
def orderup(orderval,menu,playing,orderitem):
    if orderval == 1:
        mainorder = input("What Main do you want:")
        if mainorder in menu["Main"].keys():
            orderitem[mainorder] = menu["Main"][mainorder]
            orderval += 1
        else:
            print("That is not in the menu")
            playing = True
            return(playing)
    if orderval == 2:
        mainorder = input("What is the first side you want:")
        if mainorder in menu["Sides"].keys():
            orderitem[mainorder] = menu["Sides"][mainorder]
            orderval += 1
        else:
            print("That is not in the menu")
            playing = True
            return(playing)
    if orderval == 3:
        mainorder = input("What is the second side you want:")
        if mainorder in menu["Sides"].keys():
            orderitem[mainorder] = menu["Sides"][mainorder]
            orderval += 1
        else:
            print("That is not in the menu")
            playing = True
            return(playing)
    if orderval == 4:
        mainorder = input("What is the drink you want:")
        if mainorder in menu["Drinks"].keys():
            orderitem[mainorder] = menu["Drinks"][mainorder]
            orderval += 1
            playing = False
            return(playing)
        else:

            print("That is not in the menu")
            playing = True
            return(playing)
#sets the menu
menu = {
    "Main": {
        "burger": 10.25,
        "pizza": 9.95,
        "Chicken": 12.25,
        "Suprise me": 9.99,
        "John": 12.25
    },
    "Sides": {
        "fries": 2.25,
        "salad": 20.74,
        "soup": 1.20,
        "raw onion": 12.78,
        "Ranch": 2.27
    },
    "Drinks": {
        "Pebsi": 2.00,
        "Dr.copyright": 1.70,
        "Lemonade": 0.76,
        "Real lemonade": 2.00
    }
}
#makes the items you have chosen
orderitem = {}
#print out the menu
for x in menu.keys():
    print(x)
    for y in menu[x].keys():
        print(f"{y} price {menu[x][y]}")
        print("")

orderval = 1
playing = True
while playing:

    playing = orderup(orderval,menu,playing,orderitem)
#print out what you have ordered
print("This is what you ordered")
for x in orderitem.keys():
    print(x)
for x in orderitem.values():
    print(x)
totalcost = 0.00
for x in orderitem.values():
    totalcost += x
print(f"your total is {totalcost} dollars")