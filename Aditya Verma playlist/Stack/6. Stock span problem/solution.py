def stockSpan(arr: list[int]) -> list[int]:
    n = len(arr)
    index_stack = []
    res_arr = []

    for i in range(n):
        while index_stack and arr[i] >= arr[index_stack[-1]]:
            index_stack.pop()
        if index_stack:
            res_arr.append(i - index_stack[-1])
        else:
            res_arr.append(i + 1)
        index_stack.append(i)
    return res_arr

arr = list(map(int, input().split()))
print(stockSpan(arr))