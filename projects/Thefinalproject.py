#Jc 2nd final project

#def function combat(php,pd,pmd,ps,pm,mhp,md,mmd,ms,spell list,mn,player items)
#store firstturn as true
#if ps > ms:
#turn = p
#else
#turn = m
#while fighting
    #if turn == p:
        #while turn
            #input player action between 1 and 2 to select basic actions or magic
            #if player action == 1:
                #list player options between basic attacks,defnse and speed boost,and sword swipe via 1-4 options
                #if player action == 1:
                    #Attack doing the sword damage
                    #if sword == weak sword:
                        #Damage = radnom between 3-5 damage
                    #if sword == sword:
                        #Damage = radnom between 5-6 damage
                    #set as physical damage
                #elif player action == 2:
                    #increase defense for the battle
                    #pd += 2
                #elif player action == 3:
                    #increase speed for the battle
                    #ps += 2
                #elif player action == 4 and has flintlock:
                    #increase speed for the battle
                    #Damage = radnom between 4-8 damage
                    #ps -= 1
                #else
                    #display that is not an option
                    #Continue to the top 
            #elif player action == 2:
                #Then list players options asking play to give the spells name
                #The the player imput for spell
                #if spell input == heal and has this is in spell list :
                    #php adds 3
                    #mana subtract 2
                #elif spell input == fire blade and has this is in spell list :
                    #Damage = random between 4-6 damage
                    #mana sumbrtact 2
                    #set as magical damage
                #elif spell input == ice spike and has this is in spell list :
                    #Damage = random between 7-8 damage
                    #mana subrtact 4
                    #set as magical damage
                #else
                    #display that is not an option
                    #Continue to the top 
            #else
                #display that is not an option
                #Continue to the top 
            #turn is false
    #else
        #if mn == ratman
                #damage = 1-3 
                #set damage as physical
                #display the ratman swiped at you
        #if mn == cultist
                #ma = 1-2
                #if ma = 1
                    #damage = 2-6 
                    #set damage as physical
                    #display the cultist stabed you
                #if ma = 2
                    #damage = 3-5 
                    #set damage as magical
                    #display the cultist used a magicak attack on you
        #if mn == Falsehoods
            #if first turn == true
                #set reality stat = 100
            #ma = 1-reality stat
            #if ma < 60
                #damage = 3-5 
                #realaity stat - 5
                #set damage as magical
                #display the Falsehood used a magical attack on you
            #elif ma < 70
                #damage = 2-6 
                #realaity stat - 5
                #set damage as magical
                #display the hoodFalse used a attack magicak on you
            #elif ma > 80
                #damage = 1-8
                #realaity stat - 5
                #set damage as magical
                #display  used attack the on you magical Falsehood a
            #elif ma > 90
                #damage = 0-12
                #realaity stat - 5
                #set damage as magical
                #display warping can you be you longer Reality no the around out make world seems to as
            #else
                #damage = 0-15
                #realaity stat - 5
                #set damage as magical
                #display the and all as and nothing makes non of as laws hear nature warps work turns directions you existant making crazy of sense Nothing around laughter beings 
            #if mn == lord of change
                #if first turn == true
                    #flop = false
                    #grand stats = 0
                #if flop == false
                    #mmd = 999 
                    #md = 1 - grand stats
                    #ma = 1-3
                    #if ma = 1
                        #damage = 1-8 
                        #set damage as physical
                        #display the Lord of change stikes at you
                    #if ma = 2
                        #damage = 0-20
                        #set damage as physical
                        #display the Lord of change two heads bite you
                    #if ma = 3
                        #mhp += 1-12
                        #grand stats += 2
                        #display the Lord of change speaks of the past weakening it to the future
                    #flop = true
                #else
                    #md = 999 
                    #mmd = 1 - grand stats
                    #ma = 1-3
                    #if ma = 1
                        #damage = 1-8 
                        #set damage as magical
                        #display the Lord of change casts arcare secrets at you
                    #if ma = 2
                        #damage = 0-10
                        #pmd += 1
                        #pd -= 1
                        #set damage as magical
                        #display the Lord of change two heads speaks of knowladge out of your comprenction 
                    #if ma = 3
                        #php += 3
                        #grand stats -= 4
                        #display the Lord of change speaks of the future weakening it to the past
                    #flop = false
    #if turn == p
        #if attack type == magical
            #mhp -= damage - mmd
        #else
            #mhp -= damage - md
        #turn = m
    #else
        #if attack type == magical
            #php -= damage - pmd
        #else
            #php -= damage - pd
        #turn = p
    #if php >= 0
        #end game
    #elif mhp >= 0
        #Break the combat and return php

#define function movement(room,looted rooms,finished rooms)
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
                    #room = ic
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








#


#



#Set up the starting stats for the player and the game
#room = "te"
