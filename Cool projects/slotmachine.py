#JC 2nd this is a slot machine

import random

Money = 100
bet = 0

slot1 = ""
slot2 = ""
slot3 = ""

randomvalue = random.randint(1,5)
if randomvalue == 1:
    slot1 = "X"
if randomvalue == 2:
    slot1 = "O"
if randomvalue == 3:
    slot1 = "V"
if randomvalue == 4:
    slot1 = "Z"
if randomvalue == 5:
    slot1 = "W"

randomvalue = random.randint(1,5)
if randomvalue == 1:
    slot2 = "X"
if randomvalue == 2:
    slot2 = "O"
if randomvalue == 3:
    slot2 = "V"
if randomvalue == 4:
    slot2 = "Z"
if randomvalue == 5:
    slot2 = "W"

randomvalue = random.randint(1,5)
if randomvalue == 1:
    slot3 = "X"
if randomvalue == 2:
    slot3 = "O"
if randomvalue == 3:
    slot3 = "V"
if randomvalue == 4:
    slot3 = "Z"
if randomvalue == 5:
    slot3 = "W"

bet = input("How Much do you want to bet:")

print(f"---{slot1}---{slot2}---{slot3}---")

if slot1 == slot2 or slot2 == 3:
        Money += bet * 1.5
    if p:
        money -= bet