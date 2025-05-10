
num = 10000
flag = False

for i in range(2,num):
    if (num % i) == 0:
        flag = True
        break
if flag:
     print('it is not a prime number')
else:
     print('it is a prime number')


     


