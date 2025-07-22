valid = False
i = 1

while not valid:
  try:
    n = int(input("Enter a number: "))
    #enter a even number
    while n%2 == 0:
      print(i)
      i+=1
      valid = True
  except ValueError:
    print("Invalid")

