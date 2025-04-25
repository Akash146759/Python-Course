# Initialize dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
# printing original dictionary
print("The original dictionary : " +  str(test_dict))
# Initialize value 

# Using loop
# Selective key values in dictionary
count = 0
for i in test_dict:
    if test_dict[i] == 2:
        count = count + 1
# printing result 
print("Frequency is : " + str(count))

