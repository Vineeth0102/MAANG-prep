def bubbleSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubbleSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1, -1, -1):
        is_swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swap = True
        if not is_swap:
            return arr
    return arr


num = int(input("Enter the size of the array : "))
arr = list(map(int,input("Enter the array elemnts : ").split()))
print(bubbleSort(arr))