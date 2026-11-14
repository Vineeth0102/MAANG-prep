def knapscak(weights: list[int], value: list[int], W: int, n: int) -> int:

    if n == 0 or W == 0:
        return 0

    if weights[n-1] > W:
        return knapscak(weights, value, W, n-1)
    else:
        return max(value[n-1] + knapscak(weights, value, W - weights[n-1], n-1), knapscak(weights, value, W, n-1))

n = int(input())
weights = list(map(int, input().split()))
value = list(map(int, input().split()))
W = int(input())
print(knapscak(n=n, weights=weights, value=value, W=W))
