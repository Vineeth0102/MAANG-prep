
# TC: O(N^2) as we use two for loops, SC: O(N) as we used an additonal array to store bool value
def freqCount(arr: list[int]) -> None:
    n = len(arr)
    bool_arr = [False] * n
    for i in range(0, n):
        count = 1
        if bool_arr[i] != True:
            for j in range(i+1, n):
                if arr[i] == arr[j]:
                    count += 1
                    bool_arr[j] = True
            print(arr[i], ":", count)

#TC: O(N) as we interete throug array, SC: O(min(K, N)) depends on size of dict if all elements are unique then N or else K 
from collections import Counter 
def freqCountDict(arr: list[int])  -> None:
    freq_dict = Counter(arr)
    print(freq_dict)

arr = list(map(int,input("Enter the array : ").split()))
freqCountDict(arr)