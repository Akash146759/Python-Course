# Program to find the ASCII value of a character
character = input("Enter a character: ")


if len(character) == 1:
    # Get the ASCII value using ord()
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is {ascii_value}")
else:
    print("Please enter a single character.")



n1=int(input("enter numerator: "))  
n2=int(input("enter denominator: "))
if n1%n2==0:
    print(str(n1)+" is divisible by  "+str(n2))
else:
    print(str(n1)+" is not divisible by "+str(n2))