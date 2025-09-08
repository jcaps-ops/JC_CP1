#JC 2nd Format output notes


name = "John"
age = 24
grade = .75
money = "Debt of 2300"

print("hello {}, Nice to meet you you are {:,}, that is really old! You have a {:%} in this class. You have {} dollars".format(name, age, grade, money))

# better version
print(f"hello {name}, Nice to meet you you are {age:,}, that is really old! You have a {grade:%} in this class. You have {money} dollars")