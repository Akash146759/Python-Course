def setOrNot(number, n):
    if number & (1 << n):  # No need for extra conditions
        print("SET")
    else:
        print("NOT SET")

# Taking user input
number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))

setOrNot(number, n)

