# TC: O(N^2) due to nested loops
# SC: O(1)
def checkSort(arr: list[int]) -> bool:
    n = len(arr)
    for i in range(0,n-1):
        for j in range(i, n):
            if arr[i] > arr[j]:
                return False
    return True

# TC: O(N) due to single traversal
# SC: O(1)
def checkSort1(arr: list[int]) -> bool:
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

n = int(input("Enter the size of the array : "))
arr = list(map(int, input("Enter the array elemets : ").split()))
if checkSort1(arr):
    print("The given array is sorted")
else:
    print("The array is not sorted in acending order")