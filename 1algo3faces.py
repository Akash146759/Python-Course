def fun1(n):
    return n * (n + 1) // 2  # Using integer division for consistency

print(fun1(4))  # Output: 10

def fun2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum  # Function should return the sum

print(fun2(4))  # Output: 10

def fun3(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(i, i + 1): 
            sum += 1
    return sum  # Correcting indentation for return statement

print(fun3(4))  # Output: 4
