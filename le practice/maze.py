#JC 2nd maze games
import random
import turtle
#Store the grid of the maze
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
    #Creates the rows of the grid
    for row in rows:
        for x in range (0,6):
            row.append(random.randrange(0,2))
    #Creates the colums of the grid
    for colum in colums:
        for y in range (0,6):
            colum.append(random.randrange(0,2))
    return(rows,colums)
def walldraw(rows,colums):
    
    #Sets up the the turtles
    line1 = turtle.Turtle()
    line1.speed(20000)
    line1.penup()
    line1.setx(-300)
   
   #Creates the bottom of  the maze
    line1.penup()
    line1.forward(50)
    line1.pensize(5)
    line1.pendown()
    line1.sety(0)
    line1.forward(250)
    
    #Creates a wall of  the maze
    line1.pendown()
    line1.left(90)
    line1.forward(50)
    line1.right(180)
    line1.forward(50)
    line1.left(90)
    #Creates a wall of  the maze
    line1.penup()
    line1.setx(-300)
    line1.pendown()
    line1.sety(50)
    #Based on the rows it draws the walls
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

    #Top of the maze
    line1.penup()
    line1.setx(-300)
    line1.pendown()
    line1.pensize(5)
    line1.pendown()
    line1.forward(250)
    line1.penup()
    line1.forward(50)
    
    #Sets up for y
    line1.penup()
    line1.setx(-300)
    line1.sety(0)
    line1.right(180)
    line1.left(90)
    line1.forward(50)

    #Based on the colums it draws

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
        print(stack)
        x, y = stack.pop()

        if x == size and y == size:
            return(True)
        if (x, y) in visted:
            continue
        visted.add((x,y))

        if x < size and colums[y][x+1] == 0:
            stack.append((x+ 1, y))
        if y < size and rows[y+1][x] == 0:
            stack.append((x, y+1))
        if y > 0 and rows[y-1][x] == 0:
            stack.append((x , y-1))
        if x > 0 and colums[y][x-1] == 0:
            stack.append((x-1 , y))
    
    return False
# Sets up the randomizers
turncounter = 0
issolvable = False 
while issolvable == False:
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
    randomizer1 = randomize(rows,colums)
    rows = randomizer1[0]
    rows = randomizer1[1]
    solvable = can_solve(rows,colums)
    turncounter += 1
    if solvable == True:
        print(turncounter)
        print(solvable)
        issolvable = True

print("It can be solved")    
walldraw(rows,colums)
turtle.done()