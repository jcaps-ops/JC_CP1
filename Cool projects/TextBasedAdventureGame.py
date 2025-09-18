#Jc 2nd Spread sheet managment game

import random

#Setting up my varibles
Score = 0
tasks = 3
difficulty = 1
currenttask = 1
playeranswer = ""
incorrectline = 0
stage = 1


                

#Function blocks
def tasktype1(taskroll):
    
    incorrectline = 0
    if taskroll == 1:
                incorrectline = 3
                print("Tonny taco's --- Tonny taco's")
                print("Buy amount:10 --- Buy amount:10")
                print("Buy object:Party hats --- Buy object:Party hat" )
                print("Order date:1/10 --- Order date:1/10" )
                print("Order arrival:3/10 --- Order arrival:3/10")
                print("Cost total:12.75 --- Cost total:12.75")
                print("Shipment location:Arrived --- Shipment location:Arrived")
    if taskroll == 2:
                incorrectline = 7
                print("Tonny taco's --- Tonny taco's")
                print("Buy amount:10 --- Buy amount:10")
                print("Buy object:Party hats --- Buy object:Party hats")
                print("Order date:1/10 --- Order date:1/10")
                print("Order arrival:3/10 --- Order arrival:3/10")
                print("Cost total:12.75 --- Cost total:12.75")
                print("Shipment location:Arrived --- Shipment location:Ongoing")
    if taskroll == 3:
                incorrectline = 1
                print("Tonny taco's --- Tony taco's")
                print("Buy amount:10 --- Buy amount:10")
                print("Buy object:Party hats --- Buy object:Party hats")
                print("Order date:1/10 --- Order date:1/10")
                print("Order arrival:3/10 --- Order arrival:3/10")
                print("Cost total:12.75 --- Cost total:12.75")
                print("Shipment location:Arrived --- Shipment location:Arrived")
    if taskroll == 4:
                incorrectline = 4
                print("Tonny taco's --- Tonny taco's")
                print("Buy amount:10 --- Buy amount:10")
                print("Buy object:Party hats --- Buy object:Party hats")
                print("Order date:1/10 --- Order date;2/10")
                print("Order arrival:3/10 --- Order arrival:3/10")
                print("Cost total:12.75 --- Cost total:12.75")
                print("Shipment location:Arrived --- Shipment location:Arrived")
    if taskroll == 5:
                incorrectline = 2
                print("Tonny taco's --- Tonny taco's")
                print("Buy amount:10 --- Buy amount:12")
                print("Buy object:Party hats --- Buy object:Party hats")
                print("Order date:1/10 --- Order date:1/10")
                print("Order arrival:3/10 --- Order arrival:3/10")
                print("Cost total:12.75 --- Cost total:12.75")
                print("Shipment location:Arrived --- Shipment location:Arrived")
    if taskroll == 6:
                incorrectline = "no"
                print("Tonny taco's --- Tonny taco's")
                print("Buy amount:10 --- Buy amount:10")
                print("Buy object:Party hats --- Buy object:Party hats")
                print("Order date:1/10 --- Order date:1/10")
                print("Order arrival:3/10 --- Order arrival:3/10")
                print("Cost total:12.75 --- Cost total:12.75")
                print("Shipment location:Arrived --- Shipment location:Arrived")


print("Hello employee please look over these buy orders to find mistakes (L to look out of your monitor) ")
print(incorrectline)
for x in range(0, tasks):
    print("Hello user here is you order list")

    taskroll = random.randint(1,6)
    if currenttask == 1:
        if difficulty == 1:
            print("")
            if taskroll == 1:
                incorrectline = 3
            if taskroll == 2:
                incorrectline = 7
            if taskroll == 3:
                incorrectline = 1
            if taskroll == 4:
                incorrectline = 4
            if taskroll == 5:
                incorrectline = 2
            if taskroll == 6:
                incorrectline = "no"

    if currenttask == 1:
        if difficulty == 1:
           tasktype1(taskroll)
    playeranswer = input("Which Line is incorrect(There can be nothing wrong):")
    incorrectline = str(incorrectline)
    if playeranswer == (incorrectline):
        print("")
        print("correct")
        print("")
    else:
        if playeranswer != "l":
            tasks += 1
            print("Incorrect")
        else:
            print("------------------------------")
            print("------------------------------")
            print("------------------------------")
            print("------------------------------")
            print("----------------------*######+")
            print("----------*@@@@%@@@@@-#@@@@@@#")
            print("----------+####*#####-#@@@@@@#")
            print("--=%@@%=--=++++=+++++-#@@@@@@#")
            print("--=@@@%=--------------#@@@@@@#")
            print("==+****========-------#@@@@@@#")
            print("+++++++++++++++=------#@@@@@@#")
            print("+++++++++++++++=------#@@@@@@#")

            print("You see nothing Now it has reset")
    
print("Task commplete.Now onto your next task")





