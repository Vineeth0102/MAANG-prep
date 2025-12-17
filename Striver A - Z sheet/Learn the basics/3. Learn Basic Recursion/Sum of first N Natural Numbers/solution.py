def sumNBrute(num: int) -> int:
    res = 0
    for i in range(1, num + 1):
        res += i
    return res

def sumN(num: int) -> int:
    res = (num * (num+1)) // 2
    return res

def sumNRecur(num: int) -> int:
    if num == 1:
        return 1
    else:
        return num + sumNRecur(num-1)

num = int(input("Enter the number : "))
print(sumNRecur(num))


