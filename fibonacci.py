f1=0
f2=1
f3=None
n=int(input("Enter terms"))
print(f1)
print(f2)
i=2
while (i<n):
    f3=f1+f2
    i=i+1
    print(f3)
    f1=f2
    f2=f3

