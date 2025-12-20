# TC: O(N log N) on average, O(N^2) in the worst case => when array is already sorted
# SC: O(log N) due to recursive stack space or O(N) in the worst case
def quickSort(arr: list[int], num: int) -> None:
    def partion(arr: list[int], low: int, high: int):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick(arr: list[int], low: int, high: int):
        if low < high:
            pivotIndex = partion(arr, low, high)
            quick(arr, low, pivotIndex - 1)
            quick(arr, pivotIndex + 1, high)

num = int(input("Enter the number of elemnets : "))
arr = list(map(int,input("Enter the array elements : ").split()))
quickSort(arr, num)
print(arr)