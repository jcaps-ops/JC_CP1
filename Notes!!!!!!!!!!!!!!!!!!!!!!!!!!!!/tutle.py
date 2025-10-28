#JC this is a note

import turtle
import time
import random

def turn(x, y):
    turtle.forward(10)
def move(x, y):
    turtle.left(10)
    
  # Now clicking into the turtle will turn it.


turtle.color("purple")
turtle.fillcolor("blue")
turtle.begin_fill()

for x in range (0, 4):
    turtle.forward(40)
    turtle.right(90)
    turtle.onclick(turn)
    turtle.onclick(move, 3, True)


turtle.end_fill()
turtle.done()


    



