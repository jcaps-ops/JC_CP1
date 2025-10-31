 t1pos = (round(t1.xcor(), 5))
    t2pos = (round(t2.xcor(), 5))
    t3pos = (round(t3.xcor(), 5))
    t4pos = (round(t4.xcor(), 5))
    t5pos = (round(t5.xcor(), 5))

    #Checks if it is greater than 200
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