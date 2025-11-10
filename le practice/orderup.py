# JC order up 2nd


#A resturant
menu = {
    "Main": {
        "burger": 10.25,
        "pizza": 9.95,
        "Chicken": 12.25,
        "Suprise me": 9.99
    },
    "sides": {
        "fries": 2.25,
        "salad": 20.74,
        "soup": 1.20,
        "raw onion": 12.78
    },
    "drinks": {
        "Dr.pepper": 2.00,
        "Dr.copyrigt": 1.70,
        "Lemonade": 0.76,
        "Real lemonade": 2.00
    }
}

for x in menu.keys():
    print(x)
    for y in x.value():
        print(y)
  

