def knapscak(weights: list[int], value: list[int], W: int, n: int) -> int:
    dp = [[-1 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if(i==0 or j==0):
                dp[i][j] = 0
            elif weights[i-1] <= j:
               dp[i][j] = max(value[i-1] + dp[i-1][j - weights[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j] 

    return dp[-1][-1]

n = int(input())
weights = list(map(int, input().split()))
value = list(map(int, input().split()))
W = int(input())

print(knapscak(n=n, weights=weights, value=value, W=W))