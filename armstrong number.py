number = int(input("Input number:"))
result = 0
temp = number
while temp!=0:
  digit = temp % 10 
  print('Present digit is' ,digit)
  result = result+digit**3
  print('Present result is' ,result)
  temp = temp//10
  print('Present temp is' ,temp)
print(result)
if number == result:
  print(number, "is an armstrong number ")
else:
  print(number, "is not an armstrong number ")


