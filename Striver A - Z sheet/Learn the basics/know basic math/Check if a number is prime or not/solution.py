import math

def primeCheck(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter the number to be checked : "))
if primeCheck(num):
    print("Given num is Prime")
else:   
    print("Given num is not Prime")