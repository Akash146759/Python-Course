#Input a word or sentence
string = str(input("Please enter your own String : "))

string2 = ('')
#loop for printing in reverse 
for i in string:
    print(i)
    string2 = i + string2  
    
print("\nThe Original String = ", string)
print("The Reversed String2 = ", string2)

string3 = string[::-1]
print(string3)



