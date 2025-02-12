n = int(input("Enter a number: "))

if n >= 0:
    sum_of_numbers = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is: {sum_of_numbers}")
else:
    print("Please enter a non-negative integer.")
