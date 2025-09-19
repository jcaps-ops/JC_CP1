#JC 2nd user sign in

username = "JohnPork2"
password = "Money"

plyanswer = input("Please input your username:")
if plyanswer == username:
    plyanswer = input("Please input the password:")
    if plyanswer == password:
        print("correct user")
else:
    print("incorrect username")

# or beacuse you want a bad system here
"""
username = "JohnPork2"
password = "Money"

plyanswer = input("Please input your username:")
plyanswer2 = input("Please input the password:")
if plyanswer == username:
    if plyanswer2 == password:
        print("correct user")
else:
    print("incorrect username")

"""