# TC : O(log N) or O(L) => depends on the  size of digit 
# it more resource intense as converstion takes place
def rev_num1(num :int) :
    return int(str(num)[::-1])

# TC : O(log N) or O(L) => depends on the  size of digit 
# its more faster as its just arithmatic operation 
def rev_num2(num :int) ->int :
    res = 0
    while num != 0 :
        res = res*10 + num % 10
        num //= 10
    return res

num = int(input("Enter the number : "))
print(rev_num(num))