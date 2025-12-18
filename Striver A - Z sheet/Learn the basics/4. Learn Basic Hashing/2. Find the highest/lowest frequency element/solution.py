
# TC: O(N ^ 2) as we used two nested foor loops, SC: O(N) as we used an additional axilary array
import math

def minMaxBrute(arr: list[int]) -> None:
    n = len(arr)
    bool_arr = [False] * n

    min_ele, max_ele, min_freq, max_freq = None, None, math.inf, -math.inf
    for i in range(0, n):
        count = 1
        if bool_arr[i] != True:
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    count += 1
                    bool_arr[j] = True

            if min_freq > count:
                min_ele = arr[i]
                min_freq = count
                
            if max_freq < count:
                max_ele = arr[i]
                max_freq = count
                
    print(min_ele, ":", min_freq)
    print(max_ele, ":", max_freq)

# TC: O(N) as run through the dict, SC: (K or N) depending on uniqness of element
from collections import Counter

def minMaxDict(arr: list[int]) -> None:
    freq_dict = Counter(arr)
    min_ele, max_ele = None, None
    min_freq, max_freq = math.inf, -math.inf

    for key, value in freq_dict.items():
        if min_freq > value:
            min_ele = key
            min_freq = value

        if max_freq < value:
            max_ele = key
            max_freq = value

    print(min_ele, ":", min_freq)
    print(max_ele, ":", max_freq)

arr = list(map(int,input("Enter the array : ").split()))
minMaxBrute(arr)