#Input the value of terms
n = int(input("Enter the value of terms: "))
sum = 0  #initialise
i = 0  #initialise
while i<=n: #loop will run from 1 to n
  sum = sum+i
  print('present value of sum is : ',sum)
  print('present iteration is : ',i)
  i = i + 2
print("\nSum of all natural numbers till",n,'is : ', sum)