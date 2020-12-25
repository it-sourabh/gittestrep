sum=0
a=None
n= int(input("Enter numbers"))
while (n>0):
    a=n%10
    sum=sum+a
    n=n//10
else:
    print("After adding the result is",sum)
