num = 3
flag = False

    # check for factors i = [2,3,4,5,6,7,8,.....,29]
for i in range(2, num):
    if (num % i) == 0:
        flag = True
        break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")