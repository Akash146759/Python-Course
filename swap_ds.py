def swap(a, b):
    print("before swapping: a =", a, "and b =", b)
    a, b = b, a  # Pythonic tuple unpacking for swapping
    print("After swapping: a =", a, "and b =", b)

def swap2(a, b):
    a = (a & b) + (a | b)  # Bitwise and arithmetic swap step
    b = a - b  # Compute new b
    a = a - b  # Compute new a
    print("After swapping: a =", a, "and b =", b)

# Testing swaps
swap(10, 20)
swap2(10, 20)
