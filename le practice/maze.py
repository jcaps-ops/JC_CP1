#JC 2nd maze games
import random
import turtle
rows = [
      [],
      [],
      [],
      [],
      [],
      []
]
colums = [
      [],
      [],
      [],
      [],
      [],
      []
]
wall = turtle.Turtle

def randomize(rows,colums):
    for row in rows:
        for x in range (0,6):
            row.append(random.randrange(0,2))
    for colum in colums:
        for y in range (0,6):
            colum.append(random.randrange(0,2))
    return(rows,colums)
def walldraw(rows,colums):
    
    line1 = turtle.Turtle()
    line1.speed(20000)
    line1.penup()
    line1.setx(-300)
   
    line1.penup()
    line1.forward(50)
    line1.pensize(5)
    line1.pendown()
    line1.sety(0)
    line1.forward(250)
    

    line1.pendown()
    line1.left(90)
    line1.forward(50)
    line1.right(180)
    line1.forward(50)
    line1.left(90)

    line1.penup()
    line1.setx(-300)
    line1.pendown()
    line1.sety(50)
    for row in rows:
        for x in row:
            if x == 1:
                line1.pendown()
                line1.forward(50)
            if x == 0:
                line1.penup()
                line1.forward(50)

        line1.pendown()
        line1.left(90)
        line1.forward(50)
        line1.right(180)
        line1.forward(50)
        line1.left(90)

        line1.penup()
        line1.setx(-300)
        line1.pendown()
        line1.left(90)
        line1.forward(50)
        line1.right(90)

    line1.penup()
    line1.setx(-300)
    line1.pendown()
    line1.pensize(5)
    line1.pendown()
    line1.forward(250)
    line1.penup()
    line1.forward(50)
    

    line1.penup()
    line1.setx(-300)
    line1.sety(350)
    line1.right(90)
    line1.forward(50)

    for colum in colums:
        for y in colum:
            if y == 1:
                line1.pendown()
                line1.forward(50)
            if y == 0:
                line1.penup()
                line1.forward(50)

        line1.penup()
        line1.sety(350)
      
        line1.left(90)
        line1.forward(50)
        line1.right(90)

def can_solve(rows,colums):
    size = len(rows) - 1
    visted = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop

        if x == size - 1 and y == size - 1:


randomizer1 = randomize(rows,colums)
rows = randomizer1[0]
rows = randomizer1[1]
walldraw(rows,colums)
turtle.done()