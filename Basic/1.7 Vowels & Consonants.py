name=input("Name : ")
v=0
c=0
vowels="aeiouAEIOU"

for char in name:
    if char.isalpha():
        if char in vowels:
            v+=1
        else:
            c+=1

print(v)
print(c)