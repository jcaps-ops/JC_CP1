#JC 2nd ceasuers cypher

alphebet = ["qwertyuiopasdfghjklzxcvbnm"]

def encypt(message,alphebet):
    #Get 
    changer = input("How much do you want to change it by")
    changer = int(changer)
    letter = ""
    newmessage = []
    alphebetupper = "".join(alphebet)
    alphebetupper = alphebetupper.upper()
    alphebetupperlist = [alphebetupper]
    for letter in message:
        newcearerletter = ord(letter) + changer
        if letter in alphebet and newcearerletter > 172:
            print("Lower")
            diffrence = newcearerletter - 172
            newcearerletter = 141 + diffrence
        if letter in alphebetupperlist and newcearerletter > 132:
            print("upper")
            diffrence = newcearerletter - 132
            newcearerletter = 101 + diffrence
        newcearerletter = chr(newcearerletter)
        newmessage.append(newcearerletter)

    finalmessage = "".join(newmessage)
    return(finalmessage)


#Asks the user for what they want to do
plyimput = input("What would you like to do encyrpt or decrypt (1 or 2)")
#If they chose 1 then go and encrpyt 
if plyimput == "1":
    plyimput = input("What messgae would you like to encrypt")
    message = encypt(plyimput,alphebet)
    print(f"This is your new message {message}")
#if plyimput == ""



#ord turns letter into acsii database
#chr turns ascii number into letter