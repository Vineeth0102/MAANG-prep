def missing(arr, N):
    for i in range(1, N+1):
        if i not in arr:
            return i
    return -1

def missing1(arr, N):
    return (N * (N + 1))//2 - sum(arr)

def missing2(arr, N):
        xor1 = 0
        xor2 = 0

        for i in range(N - 1):
            xor2 ^= arr[i]      
            xor1 ^= (i + 1)

        return xor1 ^ xor2 ^ N

N = int(input("Enter the N value: "))
arr = list(map(int, input("Enter the array elements: ").split()))
print(missing2(arr, N))