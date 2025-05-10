def isEvenOdd(n):
  if(n ^ 1 == n + 1 ):
    return True;
  else:
    return False;

number = int(input("Enter your number: "))
if isEvenOdd(number) is True:
  print(number, "is even")

else:
  print(number, "is odd")


def isEven(n):
    return (n & 1) == 0  # If last bit is 0, it's even

number = int(input("Enter your number: "))
if isEven(number):
    print(number, "is even")
else:
    print(number, "is odd")

  
  