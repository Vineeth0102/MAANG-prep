def fib(num: int) -> int:
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


num = int(input("Enter the Number : "))
print(fib(num))