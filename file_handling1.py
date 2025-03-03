# open file and store file object in a variable
text = open('file_handling.txt', 'w')

text.write('Hello Student!')
text.write('Welcome to coding classes!')
# read the contents of file
text.close()

a = open('file_handling.txt')
print(a.read())

# close the file
a.close()