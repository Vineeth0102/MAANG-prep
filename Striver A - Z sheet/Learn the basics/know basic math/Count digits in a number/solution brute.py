# O(N) - complexity
def num_count1(num: int) -> int :
    count = 0
    while num != 0 :
        count += 1
        num //= 10
    return count

# O(log N) or O(L)	Time depends on the number of digits in the input.
def num_count2(num: int) -> int :
    return len(str(num))    

# O(1) is the time complexity 
import math
def num_count2(num: int) -> int :
    cnt = int(math.log10(num) + 1)
    return cnt

num = int(input("Enter the number : "))
print(num_count(num))