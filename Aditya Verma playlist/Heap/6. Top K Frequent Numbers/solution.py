import heapq

def TopKFeqNumber(arr: list, k: int)-> list:
    if not arr or k < 1:
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
        heapq.heappush(heap, [feq_dict[i], i])

        if len(heap) > k:
            heapq.heappop(heap)

    while heap:
        res.append(heapq.heappop(heap)[1])

    return res


arr = list(map(int,input("Enter the arr: ").split()))
k = int(input("Enter the value of k: "))
print(TopKFeqNumber(arr=arr, k=k))