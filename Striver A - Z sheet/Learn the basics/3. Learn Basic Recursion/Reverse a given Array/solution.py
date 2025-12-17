# Brute force apporch with the help of extra array O(N)
def revArrBrute(num: int, arr: list) -> list:
    dummy_arr = []
    for i in range(num-1, -1, -1):
        dummy_arr.append(arr[i])
    return dummy_arr

# a bit optimized approch with the help of two pointer methode O(N/2)
def revArrOpt(num: int, arr: list) -> list:
    left, right = 0, num-1
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# classsic python example for one liner string slicing 
def revArrOneLine(num: int, arr: list) -> list:
    return arr[::-1]

# Reversing the Array with the help of recursion with two pointer approch O(N/2)
def revArrReccur(num: int, arr: list) -> list:
    res = actRecursion(arr, 0, num-1)
    return res

def actRecursion(arr: list, lower_bound: int, upper_bound: int) -> list:
    print(arr)
    if lower_bound > upper_bound :
        return 
    arr[lower_bound], arr[upper_bound] = arr[upper_bound], arr[lower_bound]
    actRecursion(arr, lower_bound+1, upper_bound-1)
    return arr

num = int(input("Enter the size of array : "))
arr = list(map(int,input("Enter array elements : ").split(" ")))
print(revArrReccur(num, arr))

