try:
    b = 4/0
    a = int(input("Write here: "))
    print(a)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err:
    print(err)