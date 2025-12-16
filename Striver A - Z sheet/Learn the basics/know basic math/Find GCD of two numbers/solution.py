import math

# intrnally it used Euclidean Algorithm i.e gcd(a,b)=gcd(b,amodb)
# TC is O(log(min(num1, num2)))
def gcd_call(a: int, b: int) -> int:
    return math.gcd(a,b)

num1 = int(input("Enter the Number 1 : "))
num2 = int(input("Enter the Number 2 : "))
print(gcd_call(num1, num2))
