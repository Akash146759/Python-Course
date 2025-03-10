# write in file using with()function
with open('Codingal.txt', 'w') as file:
  file.write("Damra Damra bamba Bamba rumba rumba")
file.close()

# split file into words
with open('Codingal.txt', 'r') as f:
  data = file.readlines()
  print("Words in this file are....")
  for i in data:
    word = i.split()
    print (word)
f.close()

