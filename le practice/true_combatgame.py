#jc 2nd cobat game

import random

php = 0
pa = 0
pd = 0
mhp = 30
ma = 5
md = 7
turntimer = 0
def player(php,pa,pd,mhp,turntimer):
    pinput = input("What would you like ot do (1.attack 2.heal 3.defend 4.gamble)")
    if pinput == "1":
        mhp = mhp + md - pa
    if pinput == "2":
        php += 5
    if pinput == "3":
        pd += 1
    if pinput == "4":
        if random.randrange(1,2) == 1:
            php += 10
            pa += 5
            pd += 1
    turntimer = 1
    return(php,pa,pd,mhp,turntimer)

def monster(php,pd,ma,turntimer):
    php -= ma - pd
    turntimer = 0
    return(php,pd,ma,turntimer)
    

plyclassoption = input("What class do you want to play (1,warror 2,mage 3,tank)")
if plyclassoption == "1":
    php = 30
    print(f" you have {php} health")
    pa = 10
    print(f"you have {pa} attack")
    pd = 3
    print(f"You have {pd} defence")
if plyclassoption == "2":
    php = 30
    print(f" you have {php} health")
    pa = 15
    print(f"you have {pa} attack")
    pd = 1
    print(f"You have {pd} defence")
if plyclassoption == "3":
    php = 40
    print(f" you have {php} health")
    pa = 10
    print(f"you have {pa} attack")
    pd = 1
    print(f"You have {pd} defence")

rand = random.randrange(1,2)
if rand == 1:
    turntimer = 0
    
    playerstats = player(php,pa,pd,mhp,turntimer)
    php = playerstats[0]
    pa = playerstats[1]
    pd = playerstats[2]
    mhp = playerstats[3]
    turntimer = playerstats[4]

    
else:
    print("The monster attacks")
    turntimer = 1
    monsterstats = monster(php,pd,ma,turntimer)
    php = monsterstats[0]
    pg = monsterstats[1]
    ma = monsterstats[2]
    turntimer[3]
    print(f"you have {php} health left")

while php > 0 or mhp > 0:
    if turntimer == 1:
        turntimer = 1
        print("The monster attacks")
        monsterstats = monster(php,pd,ma,turntimer)
        php = monsterstats[0]
        pg = monsterstats[1]
        ma = monsterstats[2]
        turntimer = monsterstats[3]
        print(f"you have {php} health left")
    if turntimer == 0:
        playerstats = player(php,pa,pd,mhp,turntimer)
        php = playerstats[0]
        pa = playerstats[1]
        pd = playerstats[2]
        mhp = playerstats[3]
        turntimer = playerstats[4]
        print(f"The monster has {mhp}")

if php < 1:
    print("you died")
if mhp < 1:
    print("The monster died")


