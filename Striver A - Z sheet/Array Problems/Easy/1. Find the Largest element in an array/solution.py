# TC: O(N log N) due to sorting
# SC: O(1) if we don't consider the sorting space
def largeEle(arr: list[int]) -> int:
    arr = sorted(arr)
    return arr[-1]

# TC: O(N) due to single traversal
# SC: O(1)
import math
def largeEle2(arr: list[int]) -> int:
    largest = -math.inf
    for i in arr:
        if i > largest:
            largest = i
    return largest

n = int(input("Enter the size of the array : "))
arr = list(map(int, input("Enter the array elements : ").split()))
print("Largest elemnet is : ", largeEle2(arr))