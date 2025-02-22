n=153
temp=n
sum=0
c=str(temp)
l=len(c)

# while temp!=0:
#     a=temp%10
#     sum=sum+(a**l)
#     temp//=10
for i in c:
    sum=sum+int(i)**l

if sum==n:
    print("Armstrong")
else:
    print("No Armstrong")