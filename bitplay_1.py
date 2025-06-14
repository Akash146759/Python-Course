def power4(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0 and (number & 0x55555555) != 0

n = int(input("Enter a number: "))
if power4(n):
    print("\nThe number is a power of 4")
else:
    print("\nThe number is not a power of 4")


