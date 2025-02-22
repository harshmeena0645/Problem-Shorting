num = complex(input("Enter a complex number (e.g., 3+4j): "))

real_part = num.real
imaginary_part = num.imag

if real_part > imaginary_part:
    print(f"The real part ({real_part}) is greater than the imaginary part ({imaginary_part}).")
elif imaginary_part > real_part:
    print(f"The imaginary part ({imaginary_part}) is greater than the real part ({real_part}).")
else:
    print(f"The real part ({real_part}) and the imaginary part ({imaginary_part}) are equal.")