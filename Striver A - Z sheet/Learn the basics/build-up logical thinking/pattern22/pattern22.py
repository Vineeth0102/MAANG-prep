org_n = int(input("Enter the number : "))
n = (org_n - 1) * 2 + 1

for i in range(0, n) :
    for j in range(0, n) :
        print(org_n - min(abs(i-0), abs(j-0), abs(i-n+1), abs(j-n+1)), end='')
    print()
    
