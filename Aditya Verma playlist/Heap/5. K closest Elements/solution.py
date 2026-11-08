import heapq

def kClosestElements(arr: list, k: int, x: int)->list:
    if not arr or k < 1:
        return False

    heap = []
    res = []
    for i in range(len(arr)):
        heapq.heappush(heap, [-1 * abs(x-arr[i]), arr[i]])

        if len(heap) > k:
            heapq.heappop(heap)

    while heap:
        res.append(heapq.heappop(heap)[1])
    return res

arr = list(map(int,input("Enter the array: ").split()))
k = int(input("Enter the k value: "))
x = int(input("Enter the x value: "))

print(kClosestElements(arr=arr, k=k, x=x))