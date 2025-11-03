#jc fnaf

import time
import random

monsterloc = 0
mmc = 100

m1 = " "
m2 = " "
m3 = " "
m4 = " "
m5 = " "
m6 = " "
m7 = " "
m8 = " "

def map(m1,m2,m3,m4,m5,m6,m7,m8):
    print(f"-{m1}---{m2}---{m3}-")
    print(f"-{m4}---{m5}---{m6}-")
    print(f"-{m7}---0---{m8}-")

def tickchance(mmc):
    move = random.randrange(1,mmc)
    if move == mmc:
        move()

map(m1,m2,m3,m4,m5,m6,m7,m8)

while True:
    time.sleep(0.1)
