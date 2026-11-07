import heapq

def kSortArr(arr:list, k:int)->list:
    if not arr or k < 1:
        return False
    sort_arr = []
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])

        if len(heap) > k:
            sort_arr.append(heapq.heappop(heap))
    while heap:
            sort_arr.append(heapq.heappop(heap))
    return sort_arr

arr = list(map(int,input("Enter the array: ").split()))
k = int(input("Enter the k value: "))
print(kSortArr(arr=arr, k=k))