#jc 2nd 

foreverloop = 0

nameslist = ()
dictonary_age = {}
dictonary_color = {}
testlist = ()

print("help me")

while foreverloop < 5:

    testvar = input("please help me")
    
    testlist.append(testvar)
    testanswer = t

    if testanswer in testlist:
        print("IT WORKED WHY DID IT WORK")

    name = input("What is your name user: ")
    
    if name in nameslist:
        print("Your name is " + name + " your age is " + dictonary_age[name] + " and your favorite color is " + dictonary_color[name] + ".")
    else:
            age = input("What is your age user: ")
            color = input("What is your favorite color user: ")

            dictonary_age[name] = age
            dictonary_color[name] = color

            print("Your name is " + name + " your age is " + age + " and your favorite color is " + color + ".")

            nameslist.append(name)