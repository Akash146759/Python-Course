file = open('file_handling.txt','r')

print("\n Read in lines \n")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())


print("\n Read in parts \n")
print(file.read(100))
file.close()