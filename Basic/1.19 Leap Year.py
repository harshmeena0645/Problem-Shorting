n = int(input("Year:"))
if n %  400 == 0:
    print("leap")
elif n%4==0 and n%100!=0:
    print("Leap")
else:
    print("Not Leap")