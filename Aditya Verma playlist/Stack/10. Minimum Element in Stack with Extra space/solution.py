stack = []
support_stack = []
def push(num: int) -> None:
    stack.append(num)
    if support_stack and support_stack[-1] > num:
        support_stack.append(num)
        return
    support_stack.append(num)

def pop() -> None:
    if stack:
        if stack[-1] == support_stack[-1]:
            stack.pop()
            support_stack.pop()
        elif stack:
            stack.pop()

def getMin() -> int:
    if support_stack:
        return support_stack[-1]
    else:
        return "No min"

while True:
    choice = int(input("Enter the Operations to be performed 1.Push 2.Pop 3.Get Min Element: "))
    if choice == 1:
        push(int(input("Enter the number to be pushed: ")))
    elif choice == 2:
        pop()
    elif choice == 3:
        print("Min ELement ryt now is: ",getMin)
    else:
        break
    
