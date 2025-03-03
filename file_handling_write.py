# open the file in write mode
# r = read
# w = file_write
# a = append

file_write = open('file_handling.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am teacher. \n I am 2 yr old. \nand i love french fries and biryani and jollof rice \n Nice to meet you \n you earned a punctual techie badge\ngood job!")
file_write.close()