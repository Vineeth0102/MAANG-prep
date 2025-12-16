import math

def isArmstrong(num: int) -> bool:
    size = int(math.log10(num) + 1)
    copy_num = num
    res = 0
    while num != 0 :
        res += (num%10)**size
        num //= 10
    return copy_num == res

num = int(input("Enter the number to be checked : "))
if isArmstrong(num):
    print("Given num is Armstrong")
else:
    print("Given num is not Armstrong")
