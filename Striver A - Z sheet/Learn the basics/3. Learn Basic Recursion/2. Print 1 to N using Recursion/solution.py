# TC : O(N) , SC : O(N) due to recursive stack

def oneToN(base: int, num: int) -> None:
    if num == 1:
        print(num, end=" ")
    else:
        oneToN(base, num-1)
        print(num, end=" ")

#Forward Recursion
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
