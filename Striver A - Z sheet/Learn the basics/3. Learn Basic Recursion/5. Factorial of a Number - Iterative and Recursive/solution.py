# TC : O(N) , SC : O(1)
def factIterator(num: int) -> int:
    if num < 1:
        return "Enter valid Input"
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

# TC : O(N) , SC : O(n) due to recursive stack
def factRecur(num: int) -> int:
    if num < 1:
        return "Entre Valid Input"
    elif num == 1:
        return 1
    else:
        return num * factRecur(num - 1)

num = int(input("Enter the number : "))
print(factRecur(num))