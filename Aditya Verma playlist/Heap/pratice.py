import heapq

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
x = 7

heap = []
res = []
for i in range(len(arr)):
    heapq.heappush(heap, [-1 * abs(x - arr[i]), arr[i]])

    if len(heap) > k:
        heapq.heappop(heap)

while(heap):
    res.append(heapq.heappop(heap)[1])
print(res)