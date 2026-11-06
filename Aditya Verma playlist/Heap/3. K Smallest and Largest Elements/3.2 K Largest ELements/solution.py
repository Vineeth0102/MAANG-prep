import heapq

def KthLargestElement(arr: list, k: int)->list:
    if not arr or k < 1:
        return False
    
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])

        if len(heap) > k:
            heapq.heappop(heap)

    return heap


arr = list(map(int,input("Enter array of element: ").split()))
k = int(input("Enter the K value: "))
print(KthLargestElement(arr=arr, k=k))