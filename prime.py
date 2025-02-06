
num = 7
flag = False

for i in range(2,num):
    if (num % i) == 0:
        flag = True
        break
if flag:
     print('it is not a prime number')
else:
     print('it is a prime number')


     

#i = 2 [7 % 2 == 1] --> prime number
#i = 3 [7 % 3 == 1] --> prime number
#i = 4 [7 % 4 == 3] --> prime number
#i = 5 [7 % 5 == 3] --> prime number
#i = 6 [7 % 6 == 1] --> prime number

