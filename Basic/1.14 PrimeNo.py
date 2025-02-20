n = 4
if n > 1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")