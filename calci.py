j = input("Enter the operation that you want to perform: ")
d = int(input("Enter the first no "))
e = int(input("Enter the second no "))
def calc(i, a, b):
    if (i == '+'):
        print(a + b)
    elif (i == '-'):
        print(a - b)
    elif (i == '*'):
        print(a * b)
    elif (i == '/'):
        print(a / b)
    else:
        print("Enter correctly")
calc(j, d, e)







