
print('enter your subject marks :')
a = int(input('Enter Maths :'))
b = int(input('Enter English :'))
c = int(input('Enter Geography :'))
d = int(input('Enter History :'))

avg = (a+b+c+d)/4

if avg > 80:
    print('Excellent')
elif avg > 60:
    print('Good')
elif avg > 40:
    print('Average marks')
else:
    print('Better luck next time!')
