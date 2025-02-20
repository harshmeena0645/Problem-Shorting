def swap(a, b):
    a, b = b, a
    return a, b

x = 5
y = 10

print("Before swap: x =", x, ", y =", y)

# Call the swap function
x, y = swap(x, y)

print("After swap: x =", x, ", y =", y)
