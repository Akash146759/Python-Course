def swap(a, b):
    print("before swapping: a =", a, "and b =", b)
    a, b = b, a  # Pythonic tuple unpacking for swapping
    print("After swapping: a =", a, "and b =", b)


swap(10,20)