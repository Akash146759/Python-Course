def factorial(n):
    # Base case: Stop when n = 1
    if n == 1:
        return 1
    else:
        # Recursive case: Call the function itself
        return n * factorial(n - 1)

# Testing the function
number = 4
print("Factorial of", number, "is", factorial(number))
