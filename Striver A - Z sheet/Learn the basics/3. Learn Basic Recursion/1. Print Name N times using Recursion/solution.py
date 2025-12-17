
# TC : O(N) , SC : O(N) due to recursive stack
def recurName(name: str, val: int) -> None:
    if val < 1:
        print("Invalid Input")
    elif val == 1:
        print(name, end=" ")
    else:
        recurName(name, val-1)
        print(name, end=' ')


name = input("Enter the name : ")
val = int(input("Enter the times it needed to be printed : "))
recurName(name, val)