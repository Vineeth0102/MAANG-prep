import heapq

def KSmallestElement(arr:list,k:int)->list:
    if not arr or k < 1:
        return -1
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, -1*arr[i])
        if len(heap)>k:
            heapq.heappop(heap)

    res = []
    while heap:
        res.append(-1*heapq.heappop(heap))
    
    return res
        
arr = list(map(int,input("Enter the list of elements: ").split()))
k = int(input("Enter the k value: "))
print(KSmallestElement(arr=arr,k=k))