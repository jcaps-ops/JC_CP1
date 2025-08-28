# JC 2nd Avarge grades

numclasses = int(input("How many classes do you have: "))
numcount = 0
gradelist = [] 
gradetotal = 0

for i in range(0, numclasses):
    numcount += 1
    gradelist.append(float(input("what is the grade in your " + str(numcount) + " class: ")))

numcount = 0
for i in range(0, numclasses):
       gradetotal += gradelist[numcount]
       numcount += 1

grade_avg = round(gradetotal / len(gradelist),2)
print("your avarge grade is", grade_avg)
    