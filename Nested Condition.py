#Take input of a word
string = input("Please enter your own word : ")
#take input of a character
char = input("Please enter your own Character : ")
i = 1
count = 0
#loop will to find the occurence of character
for i in range(len(string)): #string operation

    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1

#Display the result
print("The total Number of Times ", char, " has Occurred = " , count)

