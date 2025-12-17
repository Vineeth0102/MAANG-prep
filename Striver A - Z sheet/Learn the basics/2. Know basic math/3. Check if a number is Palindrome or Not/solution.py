
# TC : O(log N) or O(L) => depends on the  size of digit
def pali_check(num: int) -> int:
    rev = 0
    copy = num
    while num != 0:
        rev = rev * 10 + num % 10
        num //= 10

    return rev == copy

num = int(input("Enter the numbr : "))
if pali_check(num):
    print("The given number is pali")
else:
    print("The given number is not pali")

