
def trap(height: List[int]) -> int:
    n = len(height)
    ref = 0
    left_big = [0] * n

    for i in range(1, n):
        ref = max(ref, height[i -1])
        left_big[i] = ref

    ref = 0
    right_big = [0] * n
    for i in range(n -2, -1, -1):
        ref = max(ref, height[i+1])
        right_big[i] = ref

    water_unit = 0
    for i in range(1, n-1):
        min_height = min(left_big[i], right_big[i])
        if height[i] < min_height:
            water_unit += min_height - height[i]
    return water_unit

height = list(map(int, input().split()))
print(trap(height))