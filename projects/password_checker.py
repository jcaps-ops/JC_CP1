#JC 2nd password checker

#store players input and store the score of the value also the possible inputs being capitlased or lowercase
letterlists = "qwertyuiopasdfghjklzxcvbnm"
capitalletters = "QWERTYUIOPASDFGHJKLZXCVBNM"
speciallist = "!@#$%^&*()_+{};:,<>."
score = 0

#while True loop
while True:
    score = 0
    player = input("What is your password:")

#if length of the players input then plus 1 on score

    if len(player) >= 8:
        score += 1

#if the players input is a captilize or lowercase then check it
    #loop throughout the string check if one letter is upper or lowercase or if it uses a special character
    # checkin the Lowercase by comparing it to a list of values
    for x in letterlists:
        if x in player:
            score += 1
            break
    for x in capitalletters:
        if x in player:
            score += 1
            break
    #checks for the special lists
    for x in speciallist:
        if x in player:
            score += 1
            break
       

#checks if the value is inbetween the 0-9 value
#   score plus 1

    if "1" in player or "2" in player or "3" in player or "4" in player or "5" in player or "6" in player or "7" in player or "8" in player or "9" in player or "0" in player:
       score += 1

    print(f"Your score is {score}")

    #it will check the stength of the password and will give 5 diffrent outputs depending on it
    if score == 5:
        print("You have a strong password")
    elif score == 4:
        print("you have a somewhat strong password")
    elif score == 3:
        print("You have a mild password loser")
    elif score == 2:
        print("You have a weak password like yourself")
    else:
        print("Your password is a disgrace just like you.This is why nobody likes you")
    
    #checking if the players want to do it again
    playerint = input("Do you want to check again (y or n)")
    if playerint == "y":
        continue
    elif playerint == "n":
        break
    else:
        print("that is not a accepted answer")

