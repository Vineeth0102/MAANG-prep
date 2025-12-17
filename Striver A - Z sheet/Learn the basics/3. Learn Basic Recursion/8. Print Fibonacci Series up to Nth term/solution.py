# TC: O(N) because of for loop, SC: O(N) because of array used to store fibonacci series
def fibArr(num: int) -> int:
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, num):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]

# TC: O(N) becuse of for loop, SC: O(1) because of constant space used
def fibIter(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b

# TC: O(2^N) because of recursive calls, SC: O(N) because of recursive stack
def fib(num: int) -> int:
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fib(num - 1) + fib(num - 2)

num = int(input("Enter the Number : "))
print(fibArr(num))