def moveZero(arr: list[int]) -> list[int]:
    n = len(arr)
    dummy_arr = [0] * n
    index = 0
    for i in arr:
        if i != 0:
            dummy_arr[index] = i
            index += 1
        
    arr = dummy_arr
    return arr

def moveZero1(arr: list[int]) -> list[int]:
    n = len(arr)
    zero_pointer = 0
    while zero_pointer < n:
        if arr[zero_pointer] != 0:
            zero_pointer += 1
        break

    non_zero_pointer = zero_pointer + 1
    
    while(non_zero_pointer != n or zero_pointer != n):
        if arr[non_zero_pointer] == 0:
            non_zero_pointer += 1
        elif arr[zero_pointer] != 0:
            zero_pointer += 1
        else:
            arr[zero_pointer], arr[non_zero_pointer] = arr[non_zero_pointer], arr[zero_pointer]
            non_zero_pointer += 1
            zero_pointer += 1
        if non_zero_pointer >= n or zero_pointer >= n:
            break
    return(arr)

def moveZero2(nums: list[int]) -> list[int]:
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
    if j == -1:
        return nums
    
    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

num = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))
print(moveZero1(arr))