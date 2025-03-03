# open file and store file object in a variable
text = open('file_handling.txt', 'a')

text.write('To open a new text file on a Mac, open the "TextEdit" application, then click "File" > "New" in the menu bar; you can also use the keyboard shortcut Command + N to quickly create a new text document. ')
# read the contents of file
text.close()

a = open('file_handling.txt')
print(a.read())

# close the file
a.close()

Hashim