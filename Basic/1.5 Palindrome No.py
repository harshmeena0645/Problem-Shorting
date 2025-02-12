n = 453
b = n
ans = 0

while b > 0:
    a = b % 10
    ans = ans * 10 + a
    b = b // 10

print(ans)
if ans==n:
    print("Palindrome")
else:
    print("Not Palindrome")