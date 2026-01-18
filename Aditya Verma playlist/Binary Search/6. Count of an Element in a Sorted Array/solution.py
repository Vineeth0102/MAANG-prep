def binarySearchFirst(arr: list[int], target: int) -> list[int]:
    res = len(arr)
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = first + (last - first) // 2  
        if arr[mid] == target:
            res =  min(mid, res)
            last = mid - 1
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    if res == len(arr):
        return -1
    else:
        return res
    
def binarySearchLast(arr: list[int], target: int) -> list[int]:
    res = -1
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = first + (last - first) // 2  
        if arr[mid] == target:
            res =  max(mid, res)
            first = mid + 1
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    if res == len(arr):
        return -1
    else:
        return res

arr = list(map(int, input().split()))
target = int(input())
first_occur, last_occur = binarySearchFirst(arr, target), binarySearchLast(arr, target)
if first_occur == -1 and last_occur == -1:
    print(0)
else:
    print(last_occur - first_occur + 1)


