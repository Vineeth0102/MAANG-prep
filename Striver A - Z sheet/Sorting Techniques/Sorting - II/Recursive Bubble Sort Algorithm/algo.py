# TC: O(N^2) in the all case
# SC: O(N) due to recursive stack space
def bubbleRecurSort(arr: list[int], n: int) -> None:
    if n == 1:
        return
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    bubbleRecurSort(arr, n - 1)

# TC: O(N^2) in the worst case, O(N) in the best case
# SC: O(N) due to recursive stack space
def bubbleRecurSortOpt(arr: list[int], n: int) -> None:
    if n == 1:
        return
    is_swap = False
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            is_swap = True
            arr[j], arr[j+1] = arr[j+1], arr[j]
    if not is_swap:
        return

    bubbleRecurSort(arr, n - 1) 

num = int(input("Enter the number of elemnets : "))
arr = list(map(int,input("Enter the array elements : ").split()))
bubbleRecurSortOpt(arr, num)
print(arr)