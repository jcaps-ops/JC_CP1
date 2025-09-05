#Jc 2nd Idiot proofing

age = input("what is your full name:").strip()
phone = input("what is your phone#:")

phonedash = phone.find("-")
phone = str(phone.replace("-", " "))
#print(phone)

gpa = float(input("what is your GPA:"))
roundedgpa = round(gpa, 1)
print("hello " + age + " your phone number is " + phone + "your gpa is " + str(roundedgpa))

