def insertionSortRecur(arr: list[int], num: int) -> None:
    if num == 1:
        return
    insertionSortRecur(arr, num - 1)
    key = arr[num-1]
    j = num - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

num = int(input("Enter the number of elemnets : "))
arr = list(map(int,input("Enter the array elements : ").split()))
insertionSortRecur(arr, num)
print(arr)