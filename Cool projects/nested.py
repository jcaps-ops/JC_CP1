def test():
    pa = input("y/n")
    if pa == "n":
        return()
    elif pa == "t":
        diffrent()
        test()
    else:
        test()
def diffrent():
    print("john")

test()