def knapscak(weights: list[int], value: list[int], W: int, n: int) -> int:

    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]
    if weights[n-1] > W:
        dp[n][W] = knapscak(weights, value, W, n-1)
        return dp[n][W]
    else:
        val =  max(value[n-1] + knapscak(weights, value, W - weights[n-1], n-1), knapscak(weights, value, W, n-1))
        return val

n = int(input())
weights = list(map(int, input().split()))
value = list(map(int, input().split()))
W = int(input())
dp = [[-1]*(W+1)]*(n+1)
print(knapscak(n=n, weights=weights, value=value, W=W))

