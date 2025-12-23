def largeSub(nums: list[int], k: int) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
        subsum = nums[i]
        for j in range(i + 1, n):
            subsum += nums[j]
            if subsum > k:
                break
            elif subsum == k:
                res = max(res, j - i + 1)
    return 0 if res == 0 else res


nums = list(map(int, input().split()))
k = int(input())
print(largeSub(nums, k))