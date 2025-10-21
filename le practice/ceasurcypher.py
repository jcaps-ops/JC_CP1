#JC 2nd ceasuers cypher

alphebetlist = "abcdefghijklmnopqrstuvwxyz"

def encypt(message, alphebetlist):
    changer = input("How much do you want to change it by")
    changer = int(changer)
    letter = ""
    if letter in message:
        newcypherletter = alphebetlist(letter)
        print(newcypherletter)
    return message

plyimput = input("What would you like to do encyrpt or decrypt (1 or 2)")
if plyimput == "1":
    plyimput = input("What messgae would you like to encrypt")
    encypt(plyimput, alphebetlist)