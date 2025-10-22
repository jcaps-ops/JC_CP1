#JC 2nd ceasuers cypher


def encypt(message):
    #Get the message it uses
    changer = input("How much do you want to change it by")
    changer = int(changer)
    letter = ""
    newmessage = []
    #checks for each letter
    for letter in message:
        newcearerletter = ord(letter) + changer
        #Checks if lower
        if newcearerletter > 172:
            diffrence = newcearerletter - 172
            newcearerletter = 141 + diffrence
            #checks if upper case
        if newcearerletter > 132 and newcearerletter < 172:

            diffrence = newcearerletter - 132
            newcearerletter = 101 + diffrence
        newcearerletter = chr(newcearerletter)
        newmessage.append(newcearerletter)

    finalmessage = "".join(newmessage)
    return(finalmessage)

def decrypt(message):
    #Get the message it uses
    changer = input("How much do you want to change it by")
    changer = int(changer)
    letter = ""
    newmessage = []
    #checks for each letter
    for letter in message:
        newcearerletter = ord(letter) - changer
        #Checks if lower
        if newcearerletter > 172:
            diffrence = newcearerletter - 172
            newcearerletter = 141 + diffrence
            #checks if upper case
        if newcearerletter > 132 and newcearerletter < 172:

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
    message = encypt(plyimput)
    print(f"This is your new message {message}")
if plyimput == "2":
    plyimput = input("What messgae would you like to decrypt")
    message = decrypt(plyimput)
    print(f"This is your new message {message}")



#ord turns letter into acsii database
#chr turns ascii number into letter