#Jc 2nd final project

import time
import random

def combat(php,pd,pmd,ps,pm,mhp,md,mmd,ms,spelllist,mn,playeritems,sword):
    sword = playeritems[0]
    firstturncounter = 0
    activeturncounter = 0
    firstturn = True
    if ps > ms:
        turn = "p"
    else:
        turn = "m"
    fighting = True
    active_turn = True
    while fighting == True:
        if turn == "p":
            while active_turn:
                playeraction = input("Would you like to use a basic move:1 or a magical move:2")
                playeraction = int(playeraction )
                if playeraction == 1:
                    #list player options between basic attacks,defnse and speed boost,and sword swipe via 1-4 options
                    playeraction = input("Would you like to use your sword:1 defend:2, speed up:3 (if you have flintlock):4")
                    if playeraction == 1:
                        #Attack doing the sword damage
                        if sword == "weak sword":
                            Damage = random.randint(3,5)
                        elif sword == "sword":
                            Damage = random.randint(5,6)
                        elif sword == "warpstone sword":
                            Damage = random.randint(4,9)
                        attacktype = "physical"
                    elif playeraction == 2:
                        #increase defense for the battle
                        pd += 2
                    elif playeraction == 3:
                        #increase speed for the battle
                        ps += 2
                    elif playeraction == 4 and "flintlock" in playeritems:
                        ps -=1 
                        Damage = random.randrange(4-8)
                        attacktype = "physical"
                    
                    elif playeraction == 4 and not "flintlock" in playeritems:
                        print("You do not own the flintlock") 
                        continue
                    else:
                        print("that is not an option") 
                        continue
                         
                elif playeraction == 2:
                    #Then list players options asking play to give the spells name
                    spell_input = input("What spell would you like to use if you have learned them")
                    #The the player imput for spell
                    if spell_input == 1 and "heal" in spelllist :
                        php += 3
                        pm -= 2
                    elif spell_input == 2 and "fire blade " in spelllist:
                        Damage = random.randrange(4-8)
                        pm -= 2
                        attacktype = "magical"
                    elif spell_input == 3 and "ice spear" in spelllist :
                        Damage = random.randint(7,8)
                        pm -= 4
                        attacktype = "magical"
                    else:
                        print("that is not an option") 
                        continue
                active_turn = False
        else:
            if mn == "ratman":
                    damage = random.randrange(1,4)
                    attacktype = "physical"
                    print("the ratman swiped at you") 
            if mn == "cultist":
                    ma = random.randrange(1,2)
                    if ma == 1:
                        damage = random.randrange(2,6)
                        attacktype = "physical"
                        print("the cultist stabed you")
                    if ma == 2:
                        damage = random.randrange(3,5)
                        attacktype = "magical"
                        print(" the cultist used a magicak attack on you")
            if mn == "Falsehoods":
                if firstturn == True:
                    reality_stat = 100
                ma = random.randrange(1,reality_stat)
                if ma < 60:
                    damage = random.randrange(3,5)
                    reality_stat -= 5
                    attacktype = "magical"
                    print("the Falsehood used a magicak attack on you")
                elif ma < 70:
                    damage = random.randrange(2,6)
                    reality_stat -= 5
                    attacktype = "magical"
                    print("the hoodFalse used a attack magicak on you")
                elif ma < 80:
                    damage = random.randrange(1,8)
                    reality_stat -= 5
                    attacktype = "magical"
                    print("used attack the on you magical Falsehood a")
                elif ma < 90:
                    damage = random.randrange(0,12)
                    reality_stat -= 5
                    attacktype = "magical"
                    print("warping can you be you longer Reality no the around out make world seems to as")
                else:
                    damage = random.randrange(0,15)
                    reality_stat -= 5
                    attacktype = "magical"
                    print("the and all as and nothing makes non of as laws hear nature warps work turns directions you existant making crazy of sense Nothing around laughter beings")
                if mn == "lord of change":
                    if firstturn == True:
                        flop = False
                        grandstats = 0
                    if flop == False:
                        mmd = 999 
                        md = 1 - grandstats
                        ma = random.randrange(1,3)
                        if ma == 1:
                            damage = random.randrange(1,8)
                            attacktype = "physical"
                            print("the Lord of change stikes at you") 
                        if ma == 2:
                            damage = random.randrange(0,20)
                            attacktype = "physical"
                            print("the Lord of change two heads bites you") 
                        if ma == 3:
                            mhp += random.randrange(1,12)
                            grandstats += 5
                            print("the Lord of change speaks of the past weakening it to the future")
                            #display the Lord of change speaks of the past weakening it to the future
                        flop == True
                    else:
                        md = 999 
                        mmd = 1 - grandstats
                        ma = random.randrange(1,3)
                        if ma == 1:
                            damage = random.randrange(1,8)
                            attacktype = "magical"
                            print("the Lord of change casts arcare secrets at you")
                            #damage = 1-8 
                            #set damage as magical
                            #display the Lord of change casts arcare secrets at you
                        if ma == 2:
                            damage = random.randrange(0,10)
                            attacktype = "magical"
                            print("display the Lord of change two heads speaks of knowladge out of your comprenction ")
                            pmd += 3
                            pd -= 1
                            #set damage as magical
                            #display the Lord of change two heads speaks of knowladge out of your comprenction 
                        if ma == 3:
                            php += 3
                            grandstats -= 2
                            print("the Lord of change speaks of the future weakening it to the past")
                            #display the Lord of change speaks of the future weakening it to the past
                        flop = False
        if turn == "p":
            if attacktype == "magical":
                mhp -= damage - mmd
            else:
                mhp -= damage - md
            turn = "m"
        else:
            if attacktype == "magical":
                php -= damage - pmd
            else:
                php -= damage - pd
            turn = "p"
        if php >= 0:
            endgame = True
            return(php,pm,endgame)
        elif mhp >= 0:
            endgame = False
            return(php,pm,endgame)
        firstturncounter += 1
        activeturncounter += 1
        if firstturncounter <= 2:
            firstturn = True
        if activeturncounter == 3:
            activeturncounter = 0
            firstturn = True
            if ps > ms:
                turn = "p"
            else:
                turn = "m"
            

#define 
# function movement(room,looted rooms,finished rooms)
    #action promt = false
    #if room == te
        #display As you arrive to the city of altdorf
        #sleep for 0.1 seconds   #This point expect after all lines of display is a sleep for 0.1 seconds i refuse to write it 20 times
        #display You look around the larger village 
        #display And find it empty with no life around
        #display There are two places which you could go to a local home or the towns mayoral hall
        #While true
            #player move = input(1 for a local home or 2 for the mayors hall)
            # players move == 1:
                #room = lh
                #return room,room,looted rooms,finished rooms,action promt
            # players move == 2:
                #room = mh
                #return room,room,looted rooms,finished rooms,action promt
    #if room == lh:
        #if lh not in looted rooms:
            #display you go to the local home
            #display You look around the Home and find a suspicus bed and desk
                #player move = input(1 for the bed or 2 for desk, or 3 to return to the town entrance)
                # players move == 1:
                    #room = rt
                    #return room,room,looted rooms,finished rooms,action promt
                # players move == 2:
                    #looted rooms append lh
                    #Action prompt = true
                    ##return room,room,looted rooms,finished rooms,action promt
                #players move == 3:
                    #room = te
                    #return room,room,looted rooms,finished rooms,action promt
        #else
             #display you go to the local home
            #display You look around the Home and find a suspicus bed
                #player move = input(1 for the bed or 2 to return to the town entrance)
                # players move == 1:
                    #room = rt
                    #return room,room,looted rooms,finished rooms,action promt
                #players move == 2:
                    #room = te
                    #return room,room,looted rooms,finished rooms,action promt
    #if room == rt:
        #if rt not in finished rooms:
            #display you find a tunnel under the bed 
            #display as you enter into the tunnel you look around 
            #display when you encounter a filthy ratmen
            #display It looks a you and squeks out Intruder-thing in tunnels! Quick-quick, get-capture that man-thing!
            #display he attacks you 
            #action prompt = true
            #return room,room,looted rooms,finished rooms,action promt
        #else
            #display you go to empty tunnel where no movement can be seen 
                #player move = input(1 for the entrace or 2 or go further into the tunnel)
                # players move == 1:
                    #room = lh
                    #return room,room,looted rooms,finished rooms,action promt
                #players move == 2:
                    #room = uc
                    #return room,room,looted rooms,finished rooms,action promt
    #if room == uc 
        #if uc not in looted rooms:
            #display as you enter into the large cavern 
            #you see a large ratman city filled with glowing green stones radiating a strange light
            #With hundred of ratmen scowering around
            #Sqeaking sentances like Intruder-thing found-detected! Find-search them, yes-yes! Must have sneak-creeped into undercity-place!
            #You see two tunnels and a sign writen into a script you can read saying "Fight-kill-ring! Yes-yes!"
            #player move = input(1 for the first tunnel or 2 or go into the second tunnel or 3 to enter into the building with a sign)
                #if players move == 1:
                    #room = ic2
                    #return room,room,looted rooms,finished rooms,action promt
                #if players move == 2:
                    #room = icb
                    #return room,room,looted rooms,finished rooms,action promt
                #If player move == 3:
                    #room = fr1
                    #return room,room,looted rooms,finished rooms,action promt
    #if room == fr1
        #display A ratman approches you with out ill intent 
        #He dispite squeaking it out he manages to sound somewhat elegent says
        #"Yes-yes, greetings, new man-thing! I am owner-master of this place-hole! You want to fight-fight in ring-cage? We pay-pay you, yes!"
             #player move = input(1 to enter into the room or 2 to return outside)
                #if players move == 1:
                    #room = fr2
                    #return room,room,looted rooms,finished rooms,action promt
                #if players move == 2:
                    #room = uc
                    #return room,room,looted rooms,finished rooms,action promt
    #if room == fr2:
        #you enter into a dingy looking fighting ring
        #player move = input(1 to enter, 2 to leave) 
        #if players move == 1:
            #action promt = true
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = uc
            #return room,room,looted rooms,finished rooms,action promt
    #if room == mh:
        #You enter into the mayors hall and see it empty
        #Its almost like you could hear a prevasive silence
        #There is no movement,no breath,no sounds of speech  
        #there lies a note on the desk at the end of hall that reads
        #To the right honorable witch hunter may you investigate the imperial collage
        #As I heard reports of people going missing around there
        #you finish reading the note and look up to see a open door to the armory
        #player move = input(1 - leave for the imperial collage, 2 go to the armory)
        #if players move == 1:
            #room == arm
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = ic1
            #return room,room,looted rooms,finished rooms,action promt
    #if room = arm:
        #print You enter into the ajar door to the armory and see a man
        #Ah stop there he shouts almost like a screech
        #He prooceds to say oh sorry there witch hunter I thought you were one of those cultists
        #Oh me i am the captian of the guard he says
        #I run a little shop here would you like to buy something
        #player move = input(1 to go to his shop, 2 to exit it) 
        #if players move == 1:
            #Action promt = 1
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = mh
            #return room,room,looted rooms,finished rooms,action promt
    #if room = ic1 and not in looted rooms:
        #you enter into the hall of the imperial collage
        #First the smell of blood and gunpowerd hits your nose
        #you see the corpses of several guards litteraling the hall 
        #One of them holds a small book
        #You grab it
        #Action promt = 1
        #Then a figure leaps out at you
        #You manage to dodge but get striked in the stomach
        #Hp -= 3
        #The figure wears a massive blue robe
        #return room,room,looted rooms,finished rooms,action promt
    #elif room = ic1
        #you enter into the hall of the imperial collage
        #the smell of blood and gunpowerd is perasive 
        #you see the corpses of several guards moved and damaged from your fight
        #player move = input(1 to go deeper into the imperial collage, 2 to exit it into the mayors hall) 
        #if players move == 1:
            #rooms = ic2
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = mh
            #return room,room,looted rooms,finished rooms,action promt
    #if room = ic2 and not in looted rooms:
        #you hear the sound of battling running through your ear
        #When a grating squeak sounds "Charge-rush rats-things at cultist-thing! Kill-kill them yes-yes!"
        #You see ratling men numbering in the 50-60s charging at 15 men in blue robes
        #When a larger ratmen whereing proper armor and a man whereing a ornate blue robe
        #First the ratmen squeaks That-there is cultist-thing, yes-yes! Their cult-thing,
        # you - you help-aid I. I need-crave you kill-slay them all, yes-yes! Kill-kill! Fine sword-blade is yours-own then, if you do-do!
        #Then suddenly the cloaked man speaks
        #Ah why would you help kill me when a filthy ratmen like him roam the halls
        #So kill them and a magic tomb is yours
        #player move = input(1 To agree to the ratmen, 2 to work with the man in blue robes) 
        #if players move == 1:
            #action promt = 1
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #action promt = 2
            #return room,room,looted rooms,finished rooms,action promt
    #eliif room = ic2
        #Then hall is litted with corpses of ratmen and corpses of blue robed men
        #you see a tunnel and A door to the basement 
        #player move = input(1 to go to the tunnel, 2 to go to the basement, 3 to go to the entrance of imperial collage) 
        #if players move == 1:
            #rooms = uc
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = icb
            #return room,room,looted rooms,finished rooms,action promt
          #if players move == 3:
            #room = ic1
            #return room,room,looted rooms,finished rooms,action promt
    #if room = icb and not in looted rooms:
        #As you enter into what looks like the basement of an imperial collage
        #You see massive stone pilliars engraved with runic symbols
        #Which glows blue
        #A massive headace hits your skull
        #You see figures
        #Your vision becomes blury 
        #It feels as if something breaks
        #The figures come close
        #They reach for you
        #Action promt = 1
        ##return room,room,looted rooms,finished rooms,action promt
    #elif room = icb
        #you are in the basement of the imperial collage
        #The massive stone pilliars engraved with runic symbols are still here
        #They still glow blue but less then before
        #You still have a headace but it is negelable 
        #You see a door with the glowing runes
        #player move = input(1 to Enter into the room, 2 to exit to a tunnel 3 to exit up through the main entrance)
        #if players move == 1:
            #rooms = mcb
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = uc
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 3:
            #room = ic2
            #return room,room,looted rooms,finished rooms,action promt
    #if room == mcb and not in looted rooms
        #You arrive to room with only one man and hundred of corpses of cultists
        #He speaks Ah I did not expect to see you here hunter
        #It is the man in the ornate blue robe
        #He says may we fight now
        #Action prompt = 1
    #elif room == mcb 
        #The room is empty all that remains ae hundred of corpses 
        #and a door in and a door out 
        # player move = input(1 to Enter into the room, 2 to exit)
         #if players move == 1:
            #rooms = gl
            #return room,room,looted rooms,finished rooms,action promt
        #if players move == 2:
            #room = lcb
            #return room,room,looted rooms,finished rooms,action promt
    #if room == gl:
        #All that lies behind that door is a massive libary
        #You walk for what feels like 100 miles
        #There at the end is a cliff 
        #Which has no ending or begining
        #When you hear two voices come from bellow
        #You then see this
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@:-=@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@@@#*===%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@#=+==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@%==###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@##@@@@%=*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@%@@@%%*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@*@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**#@@#+@@@@@@*%@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@%=**=%*#@@#@@%@@@@@@@@@@@@@@@@@@@@@@@%@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-@@@##%+-#@##@@@@#%@@@@@@@@@@@@@@@@@@@@@@%%@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-*+@**+:: -=#@@@@@*@@@@@@@@@@@@@@@@@@@%@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:=**-+#***=#@@%%#@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*#@@%+=++===###**#@@@@@@@@@@@@@@@%%%%%%@@@@@@@@@@@@@%%*%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**#+##@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@**###%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++*=@@@@@@@@@@@@%%%%%%%%#@#@@@@@@@@@%@+*##**%@#%@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@%@@@@@@%%%%%%%*%@@@@@@@@@#+**++**#@%*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@#++==++++#***+**++**#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=@@@@=@@@@@@@*@@@@@@@@@@%*++++===*+===%@#++++++****#%##@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@#@@@@@@@=@@@@@#=+++++++++===+=#%#==++++++++**+*%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#%@@@@%@@@@@@#@@@@@@+++#==++++++==++#*++++++++++##***##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*%@@@@%@@@@@@*@@@@@@=+=+++++++=====+++++++++*#**+*****#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@@@+@@@@@@@@@@@@@*===+++-%@@#===+++++#%@*@**==+**##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*@@@@*@@@@@%@%@@@@@@+=============+*++++==%+=#@#@#+%###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+##@@@@#@@@@@+@@@@@@@=+====++=++===++++++%===+*=**#%*++*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+#+@@@@@@@@@@@@@@@@@@#++=+==+======+++++++*++*+**+++***#%%%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. =+*@@@@@@@@@@@@@@@@@@@+==++=++===+==+++++++++++++++%%##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%%%##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:--@@%@@@@@@@@@@@@@+-=%@+++++==+++===+++++++++++++++++*+=##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=%@*@#%#===:=+#=#+-===++=========++=====+*+++#+*%##%%#**##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@%%%%%%%%+-*@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:-#@#=@#@%@=+*+==%@=%+#*=+===++++=+*%#@%%#*+++++++*****#@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*@@@@@@@@@@@#++@@%#%#.-=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+#@@@@@@%:---%@%@@#%***+*+*@*+==++======+========++=+++++++++*#%@*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+*+=+++==+-=#*#@%%%@+ @+-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@@@@@#=:++%#@@@@=#++=%%@#+++++=++====++=#+++++++++++*%+%#%#+%@@@@#%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+=====+*-+#++#**+%%-:*@+==:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-=+==##%@@@==#+*++%@++===+=+=+++++==++++%+++++++++*+**++#*%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+#=+==+=+===-==+-+=+*+:-=-:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@%-===#@#@%@@:+==*#%*+++=++==+*++++++++#+++++++**%%#***#@#+*%##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#==+=++**+===--=-:-=**@%--:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=-+=@@@@@:===*#@%@@@@:+++*%:#+==++===%#+=*++#+==+==#%*++***##%@@@*%@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+=+==*=+=+===+==-==+**=::::%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@---=*@@@:-=-=+#@-@@#%+==++#+@++++**++====+++=*++=+@###+**%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+*==+============*@=-:-=-:.*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*--+@@@=.=---=*%#@@@@@#*+++@#*=++++*#+*+++++++++++-*##@=#*%@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*=-==============++@=@*:-::.:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:#%-%-.:---=*=##=%=++==+*=@%@@=@*+++##*#+++#+*+*++=#+=%+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*-+==========-+#@@%#.:::.:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:-=-:-*-++:==--*@+@@@@+-=+=#=@#@++**+*++%*+**+**#*###**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++*+==========-=@@@+*---:...*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..:.-:+#-=--:*@@*@@@@@#==**@@+=@#@=#**+++%@*###+%%#@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+++============+**+=:---....+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::---+*.-=.:--@@@%@@@@*=*+-%*@++=-#++#@#*#*+%##%@@##*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**+==+=#==+=====:.+%-::::...=@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@*=-+*-=*---::-=-%@@@@@@@=+++=%@***=#=%*+%+%%@%@+%@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*#+======+===+=-+@*:-::.:..+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=:*=--===::.--=*+@@%@@#@+=+++@++*@*++*******#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+++++++======+==*=+....:...:==@@@*:@@@@@@@@@@@@@@@@@@@@@@@@%:====.:--.:..-=*-+=+#@@@@#=##@@**+=*@**+*%##%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**++**++*-===**==- ...:..::@+.+-::-@@@+#@@@@@@@@@@@@@@@@@@@:-=-..--.-:-:==+*+@%##@@*-*@*+*%**++*++=@#*+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+*+++*=+-=+===*:::-@=.:.@@*+--=@@--=++#@@@@@@@@@#+:::. .-=-=.=.::-::-=++=+**+#@*##%@#*+++*#*###**#+###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=*++++=+-=+==* =#*.+-.@@-=-@=-=**::*@@@@#@=:.:==.:.-==.:=-==-::-:-=+**-*+==@@%%%%%@#=%*+*=%#%##@#*@@#-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+=++**%:=+=++*--++*%@@@@*=@@#++-+++-++#% --:::-:-.:-:-=.:.::--:+=+++**++=*#%@#@%%#%+++**%***#@@@*%#%@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+*+++-==+++=*=:-=+:+@=+=+%#@@@@@%%@@@## :==:.: --#  :.:-.::--:==+=**+=====+#+**+*%%*+*%+*%@@@%@@+%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*#**+*++**-+=--=@%%@*%-@@@@@**@*@@===+..-  %+-:=:-+@@=%::=-*+*+++++++*#@*=*#%+==@##%@@%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+%+*++=+=+-:%#++-#@@%@@@@%***%@++ @#..-@=##**%@*#@*==*++++++===+++*%##*%%@*%%#=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+%=*=#=++%+==--+@#***@@@#%@##%+#%.%*=:-*+-#%@@@*#@=@*:=+=++++*#+*+-#*#++=+=+*=+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+#=++@++-=-:++#*@@@@@@@@@@@@@-#%@% .@=*+@@#@@*#+-:+-==++++++*--**+#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++*%*+*+=*@@@@@@%#@@=-#@@@@:==#*--+#==#@@#**-=*#=--===+=#+#-+*+#*#*+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+++::.=-*@@@@@@@@#%@@#@@@#%%@@@@- -@#%@=@-++#      .-+++#*#*+*-#@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=::=  .@+@@*@@@@*%+%@+-*###@%%@@%=:-%@@@@*#@ ..+::..  -=*:##=++-**=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@==-:#- .:---@@#@@@%*+##    +@@#-@@@#*+-==@@-%%  ..:::-=...::#%+:#=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@%%%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-*==+ .. .  =*:=@@@*##+ ...%@#*@%@@---=+++=.....:   ....:.:-*%-- =-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+:-:=:--.  ::.*%*@@@@@@#= %**@%+@@@@*=:=--===+   : .:....=..:.** + ::=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@%#%%#@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+#---=*-..:=-..-#%@@#%@@@= =-++@@@%@#@#@*-====-:.-=-:**++*+*+##+- =:-+-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@%%*+##%@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:::-=.-=--:#**:::-%%@@@@@@@+=+***=@@@@@#*%@+#@*+*+.:*==+-++++=-@@@@@:@  :#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#%%%%###+@@@@@@@@@@@@@@@@#*@@###*#@*+=++--.:#.+*::#**+*=-:=%%@@%@@@@=-=+*@@@@@@#@@@*#=+++=:-:-====**+#*#@@@@@@: .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%+==*+*@@#%%###@@#*#@-#%*--*#*++.-..   +--=+:+%##+==:.+%@@@@@@%=::+@@@@@@%@@@@@@@@+++=+==:  *##%*@@*@@@@@..:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#+##+#*#=+*#*@@%+=-.+==+=*=+==:::.  .#. --%**%%%#=-=+=--=##@@@@+.:+@@@@@@@@@@@@#@*-=-#=+%+=  -@@@@@@@@@@+=:.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*-+*++#@@##=%%==+*##*=::-.:@=.. @+=::.*--*=*%%%#*++**#%@@#%@%%--=@@@@@@@@@@@@@#@+==++*+=#@@@@@@@@@@@@#=+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##=+..-*.*%#+===-@+@@@@-*+#@@@@-=+*%%%%#+#*#@@@%@@@@@@*#@@@@@@@@@@@@@@@*=-*#+#*@@@@@@@@@@@@@+*-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:+*##@@@@@%#@@#+#@@@@@%=**#%%%%###@#%%%#@@@%+=%@@@@@@@@@@@@@@@@%==@@@@@@@@@@@@@@@@@@++*%+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@====+:#@@@@@++=%+%%%%#+%@@@@@@@%*@@@@@@%#@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@#+=*+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+-.+@@*-=-++%-:.#+%#%%%%%%%%@@@@@@+%@@@@@@@@@@@@@+*@@@@%:#@@@@@@@@@@@@@@@@@@@@@*++**#+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@@##@*@%+%@**%+*-*%==*+:*@%%%#*%#@@@@@@+-*%@@@**%@%#**@@*@@@@+  %#%@@@@@@@@@@@@@@@@@@@@%@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@+=#%@@@%@+*%@@@#%:*@%%#+-.--@%%%%@%@@@@@@-%@%%@@@@@@@@@@@%@=*+:# -%@#@@@@@@@@@@@@@@@@@*#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:***#%*++*%##*%#=@@%@*%@@@@=-:--@%@@@@@@@:-*@@@@@@@@@@@@-@-+==+.@-+:-@@@@@@@@@@@@@@@@@@+#==%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.===++%*@@%@@%**#@@*#@@+%@@@@@@. -*@@@%@@@@@@#:=%+- *+%#+%*@@@@@@@@@@@@@@@@@@@#-+#+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@=:+#*@@@@%@%#*@@@%+#*#=-@@@@@@@:-+ %@@@@@@#@@@#*-%=.=**.-.:@@@@@@@@@@@@@@@@@@@@@--+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%@@@@@@@*-@*+=.**%@@**@@%@@%%#+#*+*@@@@@@@.-:#.%+@%#*+#++%=@#=-@ #*##=#@@%%@@@@@@@@@@@@@@@@@@*.:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+#+@ -##@@%*%*#%@@@##+*=%@=..@@@@@@@#*#-.=#@@=-@*.+==+  *#@@+@#%:+@@@@@@@@@@@@@@@@*@@* :=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+@% #@@@#%#%@@@@@%+-+@@%%@. .@@@@---+-.*@:%=+:@:=-+%  .-#=-:++###@@@@@@@@@@@@@@@@%.@# ::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-#*@@@@@@@@=@@@+%@@@@@@@@@ ..   . -+*.@%#+-*#--=%+:--:-+- ..-=-@@#@@@@@@@@@@@@@@@-:. .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@++#@@@@@@@@.@@@@@@@@@@@+:-=+=:.... -==+:.:-*++.**--=++==+=-.+-..%@@@@@@@@@@@@@@@@@-: :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+@#@@@@@@@@#:#@@@@@@@%-+%=.+=====+##=*+ *#-+:.+=+.*=+*=-=++@=--=-+%@@@@@@@@@@@@@@@@.-.=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@++++%@@@@@@@*+-@@@@%%%%==+=+=+*#%@@@#--*+%%@# .=+-.+-##+--+=#@@-=+-#+@@@@@@@@@@@@@@@.+-:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++=*@@@@@@@@@*+@@@@%@@+=-=:.+=*%@@@@@+*:%#%@@# --+-.+-%@#=:-+=%@@@@*@@#@@@@@@@@@@@@@@%*#-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*#+@%@@+--=::#+=*%@@@@@@=#.#@@@:+ =*==:+:%@@*::*+*+#@@@+@@%@@@@@@@@@@@@@%=-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*%+@@++=+-+#+:=*#%%#++=:==*#@@@-#+++=-: -*@*---+#+#@@@#%%=@@#*@@@@@@@@@###+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*%=%###+=*-=:==*++-:--@@===#@@% ==+=-:= @@*+=::==%@@@@*@*+#@%@@@@@@@@@@%+##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***##*:::=-::.      +@+ @==+=+@@%+%++--==*@@@@-:--:@@@#@+#*+@#@@@@@@@@@@%#=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@*+*:-..=++::-:.#@*-:@@@++++=+-=+%*+=-=#@@@@@#+.:-+%@@@%#%#*=@@@@@@@@@@@%*=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@*=+@@@.=+-+-+=*:@@@@@@@#+++=@:+%@#++:--@@@@@@-*-=*@#=+*@@+===@%@@@@@@@@%#*=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@==*%@#.:====-==+=-@@@@@@@@=++@@*+@+++=--+@@@@@==-*.-+%@@#%%@=-#@#@@@@@@@##%+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@=-=-+.:.:.:-#@@@@@@@@.%=@.. ****==:@@@@@@..-:===+++*-@+=--%@@@@@@@@@#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.:... .:=-@@@  %@@@.=*#+*-:.:=:  *@@@@@@==-=+*=-+#+#+:-=+@@@@@@@#@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=:=-.:-..-= ..@@*:-:- ..:* .-:.  @@@@@@@--=:#@#*#+:+-.=-*@@@@@%##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.===+:..:.-=::-+=-:=*%%#= . :.  *@@@@@@@=--##*+*=+=. %*@@@@*%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+-*-*+=.==-*-*@@*+:.*###*+. ... :@@@@@@@@=.=**-=+=*==%@@@@**%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+-::.:+. .+=:.+%:: -+@%=%+ +.-*+@@@@@@@@@.-:::.--=-:%@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-=-=*+#@-.:=:+@@@@+#:@=@##=:#:-*   @@@@@@@@@  . -:..:#%@@@@@@*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:=*@=@+++#:==@@@@-  .**+%=*=#- ::  =@@@@@@@@@-  -%@@@=:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=+::-*=-@@@@@@@=: ..+@@*%%@.  -  .@@@@@@@@@@@..+%%=-:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@%--%-@@@@@@@==:...:*#*+@*.  =+  #@@@@@@@@@@# .=-:-:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-+.=#-:@@@@@@@@@#=-...-=#*%@+.   +=  =@@@@@@@@@@@%:.:-=+=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***:*--@@@@@@@@@@=-. :-=*+@+@=:   +-  .@@@@@@@@@@@@=---=++@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***#+:@@@@@@@@@#-:  .=++*#@@@=-   +:   @@@@@@@@@@@@@.:-==**:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**++=@@@@@@@@%==: .:=+#++@=@@-:  .+:   %@@@@@@@@@@@@@:=*=++*#@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**=*#+##@@@@@@@@@=+::=*@@@%*#@@*=:  -=.   %@@@@@@@@@@@@@*-**++=*+%@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+*=+***+@@@@@@@@@@-.@@@@@@@@@@:**@@@@@=..+@@@@@@@@@@@@@@@#-=*+=+++@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@++*#=+#*@@@@@@@@@@##+@@@@@@@@@%=+@@@@@@:=#@@@@@@@@@@@@@@@@@:-=+==+*@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+===+*+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*---=+*@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***=+=*=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.:-+++@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@==----=+-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-= =#*=+%@@ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**=====*+==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++ -=+-=*%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***=+=======-+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=+::=++==++*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=+++=-:=++=+. -+===%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..=:  ==  +-==+=..  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=--..==*+=-::+++=@@: -=+-.  @@@@@@@@@@@@@@@@@@@@%%%+**@@@@@@@@@@@@@%: .-:@@+:  *==+=:  %@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.::--.:-.%==  ..-*+=+#  ====@**:-**%*#%*+=*#*%%#%#+#%+@@#=%%#%@@@%*==+.+:-: :. +#*%%**: .. @@%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#:=+-::=++=:: -  =@@##--::==++++*###%##%%#%@@@@@@@#@%@%@%%%%@@%@@@%**@%@%@#*#%#@@@@@%%@@@@%##%%%##@*==+##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++***###%%%%%%###%@%@#%@@%%@%%@#%%%%%%@%%%%%%%%%@%@@%@@@@@@%@@%#@@##@###*#%%%@%#@%#+*#..:.++=+@%@@@#*+*+***#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*******+*****++*****+#**++#*+#%###*+%*##%##%#*%@*%***###@#%%@#+**#%##****#+***#**+**+****++*+*****************#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*************######%%%%%%%%%%%%%%%%%%%%%%%######*##***##****####*######%%%%%%%%%%%%%%%%%%%######***************#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#********#####%%%%%%%%%%%%%@%%%%%%%%%%%%########################%%%%%%%%%%%%%%%%%%%%%%#######*****++*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%#############%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            #action promt = 1

def randomizemarket1(marketsize,itemstobuy,buyingitemscost):
    for x in range (0, marketsize):
        ranval = random.randrange(1,4)
        if ranval == 1 and "flintlock" not in itemstobuy:
                itemstobuy.append("flintlock")
                buyingitemscost.append(50)
        if ranval == 2 and "health potions" not in itemstobuy:
                itemstobuy.append("health potions")
                buyingitemscost.append(25)
        if ranval == 3 and "leather" not in itemstobuy:
                itemstobuy.append("Mana seekers potion")
                buyingitemscost.append(20)
        if ranval == 4 and "Winds of speed" not in itemstobuy:
                itemstobuy.append("Winds of speed")
                buyingitemscost.append(40)
        return(itemstobuy, buyingitemscost,ranval)
def marketbuy(money, itemstobuy, buyingitemscost,marketsize,items):
        print("Hello mercant what goods would you like to purcase")
        time.sleep(0.1)
        for x in range (0, marketsize):
            print(f"Item {x + 1} is {itemstobuy[x-1]} it costs {buyingitemscost[x-1]} coins")
            time.sleep(0.1)
        buying = True
        while buying:
            playeranswer = input("What goods would you like to buy.(Please input the number of the good or type N for no goods.): ")
            time.sleep(0.1)
            isanumber = playeranswer.isdigit()
            if isanumber == True:
                playeranswer = int(playeranswer)
                if playeranswer <= maketsize:
                    money -= buyingitemscost[playeranswer - 1]
                    print(f"You have bought some {itemstobuy[playeranswer - 1]}")
                    time.sleep(0.1)
                    items.append(itemstobuy[playeranswer - 1])
                    print(f"Your iventory now is {items}")
                    time.sleep(0.1)
                    print(f"You now have {money} coins ")
                    time.sleep(0.1)
                    playeranswer = input("Would you like to buy again(type N for no)")
                    time.sleep(0.1)
                    print(playeranswer)
                    if playeranswer == "N":
                        buying == False
            if playeranswer == "N":
                buying == False
            
money = 40
items = []
maketsize = 2
itemstobuy = []
buyingitemscost = []

marketgoods = randomizemarket1(maketsize,itemstobuy,buyingitemscost)
itemstobuy = marketgoods[0]   
buyingitemscost = marketgoods[1]
marketbuy(money,itemstobuy,buyingitemscost, maketsize,items)        












#


#



#Set up the starting stats for the player and the game
#room = "te"
