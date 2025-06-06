def OddOccuring(arr):
  res = 0
  for i in arr:
    res = res ^ i
  return res

arr = []
n = int(input("Enter array size:"))
while(n):
  num = int(input("Enter number:"))
  arr.append(num)
  n-=1

print("OddOccuring number is",OddOccuring(arr))

