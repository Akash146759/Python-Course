file1 = open('file_handling.txt','r')
file2 = open('file_handling2.txt','w')
for line in file1.readlines():
	if not (line.startswith('Coding')):
		print(line)
		file2.write(line)
file2.close()
file1.close()
