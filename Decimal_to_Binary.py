number = int(input("Enter number: "))
str1 = ""
while (number > 0):
    str1 = str1 + str(number % 2)
    number = number // 2
str1 = str1[::-1]
n = 8 - len(str1)
print((n * "0") + str1)



