import heapq

def sumBetweenK1andK2(arr: list, k1: int, k2: int)-> int:
    if not arr or k1 < 1 or k2 < 1:
        return False
    
    upper_limit = max(k1, k2)
    heap = []
    res = 0

    for i in arr:
        heapq.heappush(heap, -1 * i)

        if len(heap) > upper_limit - 1:
            heapq.heappop(heap)
            
    while len(heap) > abs(k1-k2):
        res += -1 * heapq.heappop(heap)
    return res

arr = list(map(int,input("Enter the arr: ").split()))
k1 = int(input("Enter K1: "))
k2 = int(input("Enter K2: "))

print(sumBetweenK1andK2(arr=arr, k1=k1, k2=k2))
