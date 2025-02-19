a=12
b=15
x=a
y=b
while b:
    a,b=b,a%b

HCF=a
print("HCF:", HCF)

LCM = x * y // HCF
print("LCM:", LCM)