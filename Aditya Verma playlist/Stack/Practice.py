def NGR(arr: list)->list:
    if not arr:
        return []
    stack = []
    NGR_arr = [-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack:
            if stack[-1] > arr[i]:
                NGR_arr[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(arr[i])
    return NGR_arr

def NSR(arr: list)->list:
    if not arr:
        return []
    stack = []
    NGR_arr = [-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack:
            if stack[-1] < arr[i]:
                NGR_arr[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(arr[i])
    return NGR_arr

def NGL(arr: list)->list:
    if not arr:
        return []
    stack = []
    NGR_arr = [-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack:
            if stack[-1] < arr[i]:
                NGR_arr[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(arr[i])
    return NGR_arr




arr = list(map(int,input("Enter the array : ").split()))
print(NGR(arr=arr))
print(NSR(arr=arr))
