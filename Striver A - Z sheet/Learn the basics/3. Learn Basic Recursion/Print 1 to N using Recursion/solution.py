def oneToN(base: int, num: int) -> None:
    if num == 1:
        print(num, end=" ")
    else:
        oneToN(base, num-1)
        print(num, end=" ")

#FOrward Recursion
def oneToN(current, n):
        if current > n:
            return
        print(current, end=' ')
        oneToN(current + 1, n)

#Backtrack Recursion
def oneToN(current, n):
        if current > n:
            return
        oneToN(current + 1, n)
        print(current, end=' ')

num = int(input("Enter the number : "))
oneToN(1, num)
