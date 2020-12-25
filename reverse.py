r=0
a=None
n= int(input("Enter numbers"))
while (n>0):
    a=n%10
    r=(r*10)+a
    n=n//10
else:
    print("After reversing the result is",r)
