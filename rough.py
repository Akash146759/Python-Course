def swap_xor(a, b):
    a = a ^ b
    print(a,b)
    b = a ^ b
    print(a,b)
    a = a ^ b
    print(a,b)
    print("After swapping: a =", a, "and b =", b)

swap_xor(10, 20)


