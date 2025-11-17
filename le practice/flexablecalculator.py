#jc 2nd flexable calculator

def calc(nums):
    total = 0
    for x in nums:
        x = int(x)
        total += x
    totalsum = sum(nums)
    return(totalsum)


nums = list(int(input("test")))
for x in nums:
    print(x)
    i = nums.index(x)
    if x == " " or x == ",":
        nums.pop(i)


print(nums)
print(calc(nums))