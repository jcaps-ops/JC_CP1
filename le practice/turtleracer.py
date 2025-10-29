#Jc 2nd turtle racer

import turtle
import random

def movement():
    t1.forward(random.randrange(1,10))
    t2.forward(random.randrange(1,10))
    t3.forward(random.randrange(1,10))
    t4.forward(random.randrange(1,10))
    t5.forward(random.randrange(1,10))

line1 = turtle.Turtle()
line1.penup()
line1.setx(200)
line1.pendown()
line1.pensize(5)
line1.sety(200)



t1 = turtle.Turtle()
t1.penup()
t1.setx(-300)
t1.color("Red")
t1.shape("turtle")


t2 = turtle.Turtle()
t2.penup()
t2.setx(-300)
t2.sety(50)
t2.color("blue")
t2.shape("turtle")

t3 = turtle.Turtle()
t3.penup()
t3.sety(100)
t3.setx(-300)
t3.color("purple")
t3.shape("turtle")

t4 = turtle.Turtle()
t4.penup()
t4.setx(-300)
t4.sety(150)
t4.color("green")
t4.shape("turtle")


t5 = turtle.Turtle()
t5.penup()
t5.setx(-300)
t5.sety(200)
t5.color("Yellow")
t5.shape("turtle")

hasone = False

t1.pendown()
t2.pendown()
t3.pendown()
t4.pendown()
t5.pendown()



while hasone == False:

    movement()

    t1pos = (round(t1.xcor(), 5))
    t2pos = (round(t2.xcor(), 5))
    t3pos = (round(t3.xcor(), 5))
    t4pos = (round(t4.xcor(), 5))
    t5pos = (round(t5.xcor(), 5))

    
    if t1pos > 200 and hasone == False:
        print("Turtle 1 has won")
        hasone = True
    if t2pos > 200 and hasone == False:
        print("Turtle 2 has won")
        hasone = True
    if t3pos > 200 and hasone == False:
        print("Turtle 3 has won")
        hasone = True
    if t4pos > 200 and hasone == False:
        print("Turtle 4 has won")
        hasone = True
    if t5pos > 200 and hasone == False:
        print("Turtle 5 has won")
        hasone = True


turtle.done()
    