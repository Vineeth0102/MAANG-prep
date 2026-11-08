import heapq

def FeqSort(arr: list) -> list:
    if not arr:
        return False

    feq_dict = {}
    heap = []
    res = []
    for i in range(len(arr)):
        if arr[i] not in feq_dict:
            feq_dict[arr[i]] = 1
        else:
            feq_dict[arr[i]] += 1

    for i in feq_dict:
        heapq.heappush(heap, [-1 * feq_dict[i], i])

    while heap:
        val = heapq.heappop(heap)
        for i in range(-1 * val[0]):
            res.append(val[1])

    return res

arr = list(map(int,input("Enter the arr: ").split()))
print(FeqSort(arr=arr))