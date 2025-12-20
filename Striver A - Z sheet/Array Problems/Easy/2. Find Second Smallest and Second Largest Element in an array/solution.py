# TC: O(N log N) due to sorting
# SC: O(1) if we don't consider the sorting space
def secLargeSecSmall(arr: list[int]) -> list[int]:
    n = len(arr)
    if n == 1:
        return [-1, -1]
    arr = sorted(arr)
    return [arr[1], arr[-2]]

# TC: O(N) due to single traversal but it take 3 * N as we are using min and max functions
# SC: O(1)
def secLargeSecSmall1(arr: list[int]) -> list[int]:
    n = len(arr)
    if n < 2:
        return [-1, -1]
    small = min(arr)
    large = max(arr)

    secLarge, secSmall = -math.inf, math.inf
    for i in arr:
        if i != small and i < secSmall:
            secSmall = i
        if i != large and i > secLarge:
            secLarge = i
    return [secLarge, secSmall]

# TC: O(N) due to single traversal
# SC: O(1)
import math
def secLargeSecSmall2(arr: list[int]) -> list[int]:
    n = len(arr)
    if n < 2:
        return [-1, -1]
    
    largeFirst = largeSec = -math.inf
    smallFirst = smallSec = math.inf

    for i in arr:
        if i < smallFirst:
            smallSec = smallFirst
            smallFirst = i
        elif i < smallSec and i != smallFirst:
            smallSec = i

        if i > largeFirst:
            largeSec = largeFirst
            largeFirst = i
        elif i != largeFirst and i > largeSec:
            largeSec = i

    return [largeSec, smallSec]

n = int(input("Enter the size of the array : "))
arr = list(map(int, input("Enter the array elements : ").split()))
res = secLargeSecSmall1(arr)
print("2nd Largest elemnet is : ", res[0])
print("2nd Smallest elemnet is : ", res[1])