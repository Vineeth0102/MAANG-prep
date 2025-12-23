def appearOnceBrute(arr: list[int]) -> int:
    n = len(arr)
    is_visited = [False] * n
    for i in range(0, n):
        if is_visited[i] == True:
            continue
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                is_visited[j] = True
                is_visited[i] = True
        if is_visited[i] == False:
            return arr[i]

def appearOnceBetter(arr: list[int]) -> int:
    occure_map = {}
    for i in arr:
        if i not in occure_map:
            occure_map[i] = 1
        else:
            occure_map[i] += 1

    for key, value in occure_map.items():
        if value == 1:
            return key



def appearOnceBest(arr: list[int]) -> int:
    res = 0
    for i in arr:
        res ^= i
    return res


arr = list(map(int, input().split()))
print(appearOnce(arr))