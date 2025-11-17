#JC 2nd notes
"""
def hello(name, age):
    return f"Hello {name}! you are {age} years old"

print(hello("john", 230))
"""
#args are when we dont know how many positional ones
"""
    
def hello(*names, last ,vlast):
    print(type(names))
    if names == "john":
        print(f"hello {names} {vlast}")
    for names in names:
        print(f"hello {names} {last}")

hello("alex", "john","pork","james","donetelli", last = "porkitin" ,vlast = "vatican")    
    
"""

def hello(*names, **last):
    print(type(names))
    print(last)
    
    for names in names:
        if names == "john":
            print(f"hello {names} {last['alast']} {last['vlast']}")
        else:
            print(f"hello {names} {last['alast']}")

hello("alex", "john","pork","james","donetelli", alast = "porkitin" ,vlast = "vatican")    