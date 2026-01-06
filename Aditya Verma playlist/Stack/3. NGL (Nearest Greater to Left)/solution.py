def nextLargerElement(arr: list[int]) -> list[int]:
    n = len(arr)
    res_arr = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if stack:
            res_arr[i] = stack[-1]
        stack.append(arr[i])
    return res_arr

num = int(input("Enter the array size"))
arr = list(map(int, input().split()))
print(nextLargerElement(arr))