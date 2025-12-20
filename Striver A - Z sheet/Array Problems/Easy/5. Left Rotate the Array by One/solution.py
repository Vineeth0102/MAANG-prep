def leftRotate(arr: list[int]) -> None:
    dummy_arr = [0] * len(arr)
    for i in range(n):
        dummy_arr[i - 1] = arr[i]
    arr = dummy_arr 
    print(dummy_arr)

def leftRotate1(arr: list[int]) -> None:
    first_element = arr[0]
    n = len(arr)
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = first_element
    print(arr)

n = int(input("Enter the size of the array : "))
arr = list(map(int, input("Enter the arr elements : ").split()))
leftRotate(arr)