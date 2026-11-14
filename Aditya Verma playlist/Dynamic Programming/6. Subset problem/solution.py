def subSet(arr, n, target):
    if target == 0:
        return True
    elif n == 0 and target != 0:
        return False
    elif target < arr[n-1]:
        return subSet(arr, n-1, target)
    else:
        value = subSet(arr, n-1, target) or subSet(arr, n-1, target-arr[n-1])
        return value

def subSetMemo(arr, n, target):
    if target == 0:
        return True
    elif n == 0:
        return False

    if dp_memo[n][target] is not None:
        return dp_memo[n][target]

    if arr[n-1] > target:
        dp_memo[n][target] = subSet(arr, n-1, target)
    else:
        value = subSet(arr, n-1, target) or subSet(arr, n-1, target-arr[n-1])
        dp_memo[n][target] =  value
    return dp_memo[n][target]

def subSetTab(arr, n, target):
    dp_tab = [[-1 for _ in range(target+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                dp_tab[i][j] = True
            elif i == 0:
                dp_tab[i][j] = False

            if arr[i-1] > j:
                dp_tab[i][j] = dp_tab[i-1][j]
            else:
                dp_tab[i][j] = dp_tab[i-1][j] or dp_tab[i-1][j-arr[i-1]]
    return dp_tab[-1][-1] 
            
            
        
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
dp_memo = [[-1 for _ in range(target+1)] for _ in range(n+1)]
print(subSetMemo(arr, n, target))