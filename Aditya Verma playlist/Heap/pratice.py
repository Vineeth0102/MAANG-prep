import heapq

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
sort_arr = []
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, arr[i])
    if len(heap) > k+1:
        sort_arr.append(heapq.heappop(heap))
    print(heap,sort_arr)
while heap:
    sort_arr.append(heapq.heappop(heap))
print(sort_arr)

# heapq.heapify(arr)
# print(arr)