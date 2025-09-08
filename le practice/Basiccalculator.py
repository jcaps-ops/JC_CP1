#Jc 2nd Basic calculator

cont = "yes"

for I in (100, 1):
        
    if cont == "yes":   
        num1 = input("Give me the first number:")
        num1 = int(num1)

        num2 = input("Gib me 2nd number:")
        num2 = int(num2)

        num3 = num1 + num2
        print(f"{num1:.2f} + {num2:.2f} = {num3:.2f}")

        num3 = num1 - num2
        print(f"{num1:.2f} - {num2:.2f} = {num3:.2f}")

        num3 = num1 * num2
        print(f"{num1:.2f} * {num2:.2f} = {num3:.2f}")

        num3 = num1 / num2
        print(f"{num1:.2f} / {num2:.2f} = {num3:.2f}")

        num3 = num1 ** num2
        print(f"{num1:.2f} ** {num2:.2f} = {num3:.2f}")

        num3 = num1 % num2
        print(f"{num1:.2f} % {num2:.2f} = {num3:.2f}")

        num3 = num1 // num2
        print(f"{num1:.2f} // {num2:.2f} = {num3:.2f}")

        cont1 = input("Do you want to keep going:")