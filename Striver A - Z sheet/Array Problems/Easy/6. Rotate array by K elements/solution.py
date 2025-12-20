# Time Complexity: O(n), We are performing a constant number of linear operations copying `k` elements and shifting up to `n-k` elements.
#Space Complexity: O(k) ,A temporary array of size `k` is used to store either the first `k` or last `k` elements depending on the direction of rotation.
def rotate_array(arr: list[int], k:int, direction: str) -> None:
    if direction == 'right':
        move = 1
    else:
        move = -1
    n = len(arr)
    dummy_arr = [0] * n
    for i in range(0, n):
        dummy_arr[(i + (move * k)) % n] = arr[i]
    print(dummy_arr)

# Time Complexity: O(N), We reverse parts of the array each reverse takes linear time. So total work is 3 × O(N) = O(N).
# Space Complexity: O(1) All modifications are done in-place, using only a few temporary variables.
def rotate_array1(arr: list[int], k:int, direction: str) -> None:
    def revserse(arr: list[int], start: int, end: int):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start + 1, end - 1
    n = len(arr)
    if n == 0 or n == 1:
        return
    if direction == 'right':
        revserse(arr, 0, n - 1)
        revserse(arr, 0, k - 1)
        revserse(arr, k, n - 1)
    else:
        revserse(arr, 0, k - 1)
        revserse(arr, k, n - 1)
        revserse(arr, 0, n - 1)
    
    print(arr)

num = int(input("Enter number of elements in array: "))
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter the rotation factor K: "))
direction = input("Enter rotation direction (right/left):")
rotate_array1(arr, k, direction)
