def paliRecur(val: str) -> bool:
    return check(val, 0, len(val)-1)

def check(val: str, lower_bound: int, upper_bound: int) -> bool:
    if lower_bound >= upper_bound:
        return True
        
    if val[lower_bound] == val[upper_bound]:
        return check(val, lower_bound + 1, upper_bound - 1)
    return False

val = input("Enter the String : ")
if paliRecur(val):
    print("The Given String is Palindrom")
else:
    print("The Given String is not Palindrom")

