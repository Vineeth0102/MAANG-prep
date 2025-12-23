def consOnes(arr: list[int]) -> int:
    count = maxone = 0
    for i in arr:
        if i == 0:
            maxone = max(maxone, count)
            count = 0
        else:
            count += 1

    return maxone

prices = list(map(int, input("Enter the prices : ").split()))
print(consOnes(prices))

