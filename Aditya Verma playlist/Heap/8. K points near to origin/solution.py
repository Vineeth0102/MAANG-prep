import heapq  
import math 

def KPointsNearOrgini(arr: list[list], k: int):
    if not arr or k < 1:
        return False

    heap = []
    for i in arr:
        # distance = math.sqrt(i[0]**2 + i[1]**2)
        distance = i[0]**2 + i[1]**2 # more cleaner approch
        heapq.heappush(heap, [-1 * distance, i])

        if len(heap) > k:
            heapq.heappop(heap)
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])

    return res

rows = int(input("Enter number of cordiantes: "))
arr = []
print("Enter cordiantes one after the other: ")
for i in range(rows):
    arr.append(list(map(int,input().split())))
k = int(input("Enter the k value: "))

print(KPointsNearOrgini(arr=arr, k=k))
