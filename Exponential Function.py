j = int(input("Enter the number: "))
k = int(input("Enter the power: "))
def expo(num, power):
    ans = 1
    for i in range(power):
        ans *= num
    return ans

print("The result after raising " + str(j) + " to " + str(k) + " is", expo(j, k))
