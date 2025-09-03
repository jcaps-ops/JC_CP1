#Jc 2nd puzzle

puzzlesym = ["a", "b", "c", "d", "e", "f"]
selectedsection = 1
selectedsection1 = 0
selectedsection2 = 0
selectedsection3 = 0
section1 = puzzlesym[selectedsection1]
section2 = puzzlesym[selectedsection2]
section3 = puzzlesym[selectedsection3]

print(" type A and D to move between sections. Use W to change lock part")
for x in range(100):
    if selectedsection == 1:
        print("-------|--------------------------")
        print("-------" + section1 + "-------" + section2 + "-------" + section3 + "----------")
        print("-------|--------------------------")
        answered = input("what would you like to do: ")
    
    if selectedsection == 2:
        print("---------------|------------------")
        print("-------" + section1 + "-------" + section2 + "-------" + section3 + "----------")
        print("---------------|------------------")
        answered = input("what would you like to do: ")
    
    if selectedsection == 3:
        print("-----------------------|----------")
        print("-------" + section1 + "-------" + section2 + "-------" + section3 + "----------")
        print("-----------------------|----------")
        answered = input("what would you like to do: ")

    if answered == "d":
            selectedsection += 1
            if selectedsection == 4:
                selectedsection =0
    
    if answered == "a":
            selectedsection -= 1
            if selectedsection == -1:
                selectedsection =3
    
    if answered == "w":
        if selectedsection == 1:
            selectedsection1 += 1
            
            section1 = puzzlesym[selectedsection1]
            if selectedsection1 == 5:
                 selectedsection1 = -1

    if answered == "w":
        if selectedsection == 2:
            selectedsection2 += 1
            
            section2 = puzzlesym[selectedsection2]
            if selectedsection2 == 5:
                 selectedsection2 = -1
    
    if answered == "w":
        if selectedsection == 3:
            selectedsection3 += 1
            
            section3 = puzzlesym[selectedsection3]
            if selectedsection3 == 5:
                 selectedsection3 = -1
            