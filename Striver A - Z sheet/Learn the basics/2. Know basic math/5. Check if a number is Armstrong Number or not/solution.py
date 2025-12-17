import math

def isArmstrong(num: int) -> bool:
    size = int(math.log10(num) + 1) # TC : O(1)
    copy_num = num
    res = 0
    while num != 0 :    # TC : O(log N) or O(L) => depends on the  size of digit
        res += (num%10)**size
        num //= 10
    return copy_num == res

num = int(input("Enter the number to be checked : "))
if isArmstrong(num):
    print("Given num is Armstrong")
else:
    print("Given num is not Armstrong")
