import heapq

def ConnectRopes(arr: list)-> int:
    if not arr:
        return False

    res = 0
    while len(arr) > 1:
        val  = heapq.heappop(arr) + heapq.heappop(arr)
        res += val
        arr.append(val)

    return res

arr = list(map(int,input("Enter the rope sizes: ").split()))
print(ConnectRopes(arr=arr))