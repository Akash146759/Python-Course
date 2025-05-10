def primeSeive(n):
    prime = [True] * (n + 1)  # Initialize all numbers as prime
    p = 2
    while p * p <= n: 
        if prime[p]:  # If p is still prime
            for i in range(p * p, n + 1, p):  # Mark multiples of p as non-prime
                prime[i] = False
        p += 1

    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

    # Collect and return prime numbers
    return [p for p in range(n + 1) if prime[p]]

# Get user input
n = int(input("Enter a number to find all prime numbers less than or equal to it: "))

# Find primes and print them
primes = primeSeive(n)
print("Following are the prime numbers smaller than or equal to", n)
print(primes)

