#jc 2nd flexable calculator

def calc(*values):
    total = 0
    for x in values[0]:
        x = int(x)
        total += x
    totalsum = sum(values[0])
    return(values[0])


nums = list(input("test"))
for x in nums:
    print(x)
    i = nums.index(x)
    if x == " " or x == ",":
        nums.pop(i)
    else:
        int(x)


print(nums)
print(calc(nums))