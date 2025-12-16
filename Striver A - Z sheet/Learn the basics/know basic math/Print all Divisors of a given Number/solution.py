import math
def diviors(num: int) -> list:
    res = []
    for i in range(1, int(math.isqrt(num)) + 1):
        if num % i == 0:
            res.append(i)
            if i != num // i:
                res.append(num // i)
    return res

num = int(input("Enter the number: "))
print(diviors(num))