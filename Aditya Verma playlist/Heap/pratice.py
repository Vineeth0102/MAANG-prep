import heapq

arr = [1, 2, 1, 3, 4, 1, 2, 5, 5, 5]
k = 2

heap = []
res = []
feq_map = {}
for i in range(len(arr)):
    if arr[i] not in feq_map:
        feq_map[arr[i]] = 1
    else:
        feq_map[arr[i]] += 1

for i in feq_map:
    heapq.heappush(heap,[feq_map[i], i])

    if len(heap) > k:
        heapq.heappop(heap)

while heap:
    res.append(heapq.heappop(heap)[1])
print(res)