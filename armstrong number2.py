# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string and calculate the number of digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return armstrong_sum == number

# Find all Armstrong numbers between 1 and 10,000
armstrong_numbers = [num for num in range(1, 10001) if is_armstrong(num)]

print("Armstrong numbers between 1 and 10,000:")
print(armstrong_numbers)
