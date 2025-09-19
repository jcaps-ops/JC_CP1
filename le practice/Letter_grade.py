#JC 2nd What is my grade
grade = 97.6
#grade = input("What is your grade(As a percent)")
grade = float(grade)

if grade >= 97.5:
    print("You have an A+")
elif grade >= 92.5:
    print("You have an A")
elif grade >= 90.0:
    print("You have an A-")
elif grade >= 87.5:
    print("You have an b+")
elif grade >= 82.5:
    print("You have an B")
elif grade >= 80.0:
    print("You have an B-")
elif grade >= 77.5:
    print("You have an C+")
elif grade >= 73.5:
    print("You have an c")
elif grade >= 70.0:
    print("You have an d")
elif grade >= 67.0:
    print("You have an d-")
else:
    print("You have a F")
    