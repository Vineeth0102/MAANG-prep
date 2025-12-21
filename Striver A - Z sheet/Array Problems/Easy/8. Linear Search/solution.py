def linearSearch(arr: list[int], num: int) -> int:
    n = len(arr)
    for i in range(n):
        if arr[i] ==  num:
            return i
    return -1

num = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the element to be searched: "))
print(linearSearch(arr, target))