n=int(input("enter the number of rows:"))
for i in range(1-1,n,1):
    for j in range(0,i):
        print("*",end="")
    print()

for i in range(0, n, 1):
    print(" " * (n - i) + "*" * i)