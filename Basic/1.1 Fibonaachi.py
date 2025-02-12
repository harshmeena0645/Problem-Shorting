n=10
a=0
b=1
arr=[]
arr.append(a)
arr.append(b)
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    arr.append(c)
print(arr)