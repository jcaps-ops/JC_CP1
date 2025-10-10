#JC 2nd password checker

#store players input and store the score of the value also the possible inputs
letterlists = "qwertyuiopasdfghjklzxcvbnm"
speciallists = "!@#$%^&*(){}_+|:<>?,./;[]"

#while True loop
while True:
    score = 0
    player = input("What is your password:")

#if length of the players input then plus 1 on score

    if len(player) >= 8:
        score += 1

#if the players input is a captilize then check it
    #loop throughout the string check if one letter is upper
    for x in letterlists:
        if x in player:
            score += 1
            break
    for x in letterlists:
        
        if letterlists[x].isupper:
            score += 1
            break
    for x in speciallists:
        if x in player:
            score += 1
            break
       

#if 1 in player or 2 in player or 3 in player or 4 in player or 5 in player or 6 in player or 7 in player or 8 in player or 9 in player or 10 in player
#   score plus 1
    if "1" in player or "2" in player or "3" in player or "4" in player or "5" in player or "6" in player or "7" in player or "8" in player or "9" in player or "0" in player:
       score += 1
# checkin the Lowercase by comparing it to a list of values
    print(f"Your score is {score}")
