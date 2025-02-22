num = int(input("num:"))
s=0
while num!=0:
    r = num % 10
    num = num//10
    s += r
print(s)