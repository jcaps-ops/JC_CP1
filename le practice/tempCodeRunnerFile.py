for x in menu.keys():
    print(x)
    for y in menu[x].keys():
        print(f"{y} price {menu[x][y]}")
        print("")