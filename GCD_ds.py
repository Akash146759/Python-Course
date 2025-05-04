HCF (Highest Common Factor) is another name for GCD (Greatest Common Divisor)!

It simply means the biggest number that can evenly divide two or more numbers.

Let’s take an example: Find the HCF of 20 and 30.

Step 1: List the factors of each number.

Factors of 20 → 1, 2, 4, 5, 10, 20

Factors of 30 → 1, 2, 3, 5, 6, 10, 15, 30

Step 2: Find the common factors → 1, 2, 5, 10

Step 3: The highest common factor is 10! So, HCF(20, 30) = 10

numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)
