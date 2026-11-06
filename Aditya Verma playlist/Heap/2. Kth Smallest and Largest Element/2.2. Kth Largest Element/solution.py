import heapq

def KthLargestElement(arr: list, k: int)->int:
    if not arr or k < 1:
        return False
    
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])

        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap)


arr = list(map(int,input("Enter array of element: ").split()))
k = int(input("Enter the K value: "))
print(KthLargestElement(arr=arr, k=k))