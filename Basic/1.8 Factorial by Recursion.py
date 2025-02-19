def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))

if n >= 0:
    print(f"The factorial of {n} is: {factorial(n)}")
else:
    print("Factorial is not defined for negative numbers.")
