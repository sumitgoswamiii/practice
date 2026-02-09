n = int(input("Enter the number: "))
for i in range(1,n+1):
    if(i % 2 == 1):
        print("*"*n)
    else:
        for j in range(1, n+1):
            if(j % 2 == 1):
                print("*", end="")
            else:
                print(" ", end="")
        print("")