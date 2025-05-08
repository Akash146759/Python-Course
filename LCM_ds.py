def find_lcm(x, y):
    # Choose the greater number
    greater = max(x, y)
    
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    
    return lcm

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display LCM
print(f"The LCM of {num1} and {num2} is {find_lcm(num1, num2)}")
