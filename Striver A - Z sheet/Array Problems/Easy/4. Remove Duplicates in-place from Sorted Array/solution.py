# TC: O(N)
# SC: O(N) - using set as it grows dynamically
def uinique(arr: list[int]) -> int:
    uniSet = set()
    index = 0
    for i in arr:
        if i not in uniSet:
            uniSet.add(i)
            arr[index] = i
            index += 1
    return index

# TC: O(N)
# SC: O(1)
def uinique1(arr: list[int]) -> int:
    index = 0
    n = len(arr)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            index += 1
            arr[index] = arr[i]
            print(index, i)
    return index

n = int(input("Enter the array size : "))
arr = list(map(int, input("Enter the sorted array : ").split()))
index = uinique1(arr)
print(arr[:index+1])
