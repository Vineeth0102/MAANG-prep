def binarySearchRev(arr: list[int], target: int) -> int:
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = first + (last - first) // 2  
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            first = mid + 1
        else:
            last = mid - 1
    return -1

arr = list(map(int, input().split()))
target = int(input())
print(binarySearchRev(arr, target))


