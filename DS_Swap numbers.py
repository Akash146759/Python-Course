def swap(a,b):
  a = a^b
  b = a^b
  a = a^b
  print("After swapping: a =",a,"and b =",b)

def swap2(a,b):
  a = (a&b)+(a|b)
  b = a+(~b)+1
  a = a+(~b)+1
  print("After swapping: a =",a,"and b =",b)

swap(10,20)
swap2(10,20)



A = 10 (in binary: 1010) and B = 20 (in binary: 10100).

Perform 10 ^ 20 (XOR operation):
  01010      (A = 10)
^ 10100     (B = 20)
--------
  11110     (A now holds a scrambled mix of both)

b = a ^ b
  11110     (New A, holding a mix)
^ 10100     (Old B = 20)
--------
  01010      (B is now restored to original A = 10)


a = a ^ b
  11110     (A still holds the mix)
^ 01010      (New B = 10)
--------
  10100     (A is now restored to original B = 20)

  