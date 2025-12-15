n =  int(input("Enter the number : "))

for i in range(n, 0, -1) :
    for j in range(0, i) :
        print(j+1,  end='')
    print()