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

def monster(php,pd,ma):
    php -= ma - pd
    turntimer = 0
    return(php,turntimer)
    


plyclassoption = input("What class do you want to play (1,warror 2,mage 3,tank)")
if plyclassoption == "1":
    php = 30
    pa = 10
    pd = 3
if plyclassoption == "2":
    php = 30
    pa = 15
    pd = 1
if plyclassoption == "3":
    php = 40
    pa = 10
    pd = 1

rand = random.randrange(1,2)
if rand == 1:
    turntimer = 0
    playerstats = [player(php,pa,pd,mhp)]
    
else:
    turntimer = 1
    monster(php,pd,ma)




