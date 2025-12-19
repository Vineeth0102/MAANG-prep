# TC: O(N ^ 2) in all cases
# SC: O(1) as we are not using any extra space
def selectionSort(arr: list[int]) -> list:
    n = len(arr)
    for i in range(0, n):
        lest = arr[i]
        index = i
        for j in range(i+1, n):
            if lest > arr[j]:
                lest = arr[j]
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

n = int(input("Enter the size of the array : "))
arr = list(map(int,input("Enter the array elemnts : ").split()))
print(selectionSort(arr))

