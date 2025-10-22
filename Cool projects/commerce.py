#jc 2nd logicstical chains
town1resources = []
town1resourcesnumbers = []
town1pull = []
town1pullnumber = []
town1production = "wheat"
while True:
    pint = input("What would you like to do ()")
    if town1production in town1resources:
        print("Uh")
    else:
        town1resources.append(town1production)
        town1resourcesnumbers.append("1")
    print(town1resources)
    print(town1resourcesnumbers)
