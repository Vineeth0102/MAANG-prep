# TC : O(N) , SC : O(N) due to recursive stack
def NtoOne(val: int, base: int) -> None:
    if base == 1:
        return
    NtoOne(val-1, 1)
    print(val,end=" ")
    
val = int(input("Enter the Number : "))
NtoOne(val, 1)