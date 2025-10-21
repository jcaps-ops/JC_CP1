#JC 2nd ceasuers cypher



def encypt(message):
    changer = input("How much do you want to change it by")
    changer = int(changer)
    letter = ""
    newmessage = ""
    for letter in message:
        newcearerletter = ord(letter) + changer
        newmessage += newcearerletter
    return newmessage

plyimput = input("What would you like to do encyrpt or decrypt (1 or 2)")
if plyimput == "1":
    plyimput = input("What messgae would you like to encrypt")
    encypt(plyimput)



#ord turns letter into acsii database
#chr turns ascii number into letter