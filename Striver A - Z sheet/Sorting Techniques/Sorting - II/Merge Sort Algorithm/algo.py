def mergeSort(arr: list[int]) -> None:
    def divide(arr: list[int], lower_bound: int, upper_bound: int):
        if lower_bound >= upper_bound:
            return 
        mid = ((upper_bound - lower_bound) // 2) + lower_bound
        divide(arr, lower_bound, mid)
        divide(arr, mid + 1, upper_bound)
        merge(arr, lower_bound, mid, upper_bound)

    def merge(arr: list[int], lower_bound: int, mid: int, upper_bound: int) -> None:
        temp = []
        left, right = lower_bound, mid + 1

        while left <= mid and right <= upper_bound:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= upper_bound:
            temp.append(arr[right])
            right += 1

        for i in range(lower_bound, upper_bound + 1):
            arr[i] = temp[i - lower_bound]

    n = len(arr)
    divide(arr, 0, n-1)


num = int(input("Enter the number of elemnets : "))
arr = list(map(int,input("Enter the array elements : ").split()))
mergeSort(arr)
print(arr)
