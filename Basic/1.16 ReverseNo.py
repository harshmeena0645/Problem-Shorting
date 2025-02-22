x = int(input("num: "))
num=abs(x)
s=0
while num != 0:
    r = num % 10
    s = 10*s + r
    num = num // 10

if x<0:
    s = -s

# if num < -2**31 or num > 2**31 - 1:
#     print(0)

print(s)