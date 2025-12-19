# TC: O(N ^ 2) in worst case, as well as in the best case
# SC: O(1) as we are not using any extra space
def inserstionSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

num = int(input("Enter the size of the array : "))
arr = list(map(int,input("Enter the array elemnts : ").split()))
print(inserstionSort(arr))
