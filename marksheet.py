a = int(input("Enter Hindi Marks: "))
b = int(input("Enter Maths Marks: "))
c = int(input("Enter Science Marks: "))
d = int(input("Enter English Marks: "))
e = int(input("Enter SST Marks: "))
sum = a+b+c+d+e
per = sum/5
print(per)
if (per>=60):
    print("First Division")
elif (per >= 45 and per<60):
    print("Second Division")
elif (per >=33 and per<45):
    print("Third Division")
else:
    print("Fail")