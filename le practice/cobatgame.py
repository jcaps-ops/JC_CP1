#jc 2nd battle
#Not for self make this tunbased fighter

defense = 0
attack = 0 
health = 0
plyclass = ""
grid1 = ["|","0","0","0","0","0","0","0","0","0","0","|"]
grid2 = ["|","0","0","0","0","0","0","0","0","0","0","|"]
grid3 = ["|","=","=","=","=","=","=","=","=","=","=","|"]
grid4 = ["|","0","0","0","0","0","0","0","0","0","0","|"]
grid5 = ["|","0","0","0","0","0","0","0","0","0","0","|"]

def playerturn():
    plyaction = input("What would you like to do (1:wait 2:build a arrow tower)")

def place():
    line = input("which line do you put it on")
    row = input("where do you put it on")
    if line == "1":
        if grid1.index(row) != 0:
            grid1.pop(row)
            grid1.insert(row)



#Gameloop
print("".join(grid1))
print("".join(grid2))
print("".join(grid3))
print("".join(grid4))
print("".join(grid5))

place()