def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)

n = int(input("Enter a number: "))

if n >= 0:
    print("The sum of the first",n,"natural numbers is:",sum_of_natural_numbers(n))
else:
    print("Please enter a non-negative integer.")