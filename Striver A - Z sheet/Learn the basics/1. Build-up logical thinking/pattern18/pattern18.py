n =  int(input("Enter the number : "))

for i in range(n, 0, -1) :
    for j in range(i, n + 1) :
        print(chr(65 + j - 1), end=' ')
    print()