def findRotation(arr: list[int]) -> int:
    n = len(arr)
    first, last = 0, len(arr) -1

    while first <= last:
        if arr[first] <= arr[last]:
            return first
        
        mid = first + (last - first) // 2
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        if arr[mid] >= arr[first]:
            first = mid + 1
        else:
            last = mid - 1

arr = list(map(int, input().split()))
print(findRotation(arr))