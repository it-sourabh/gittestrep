i = input("Do you use tiktok: ")
j = int(input("What is your height in centimetres ?: "))
if (j >= 165):
    istall = True
else:
    istall = False
if (i == "Yes" or i == "yes" or i == "YES"):
    ismale = False
elif (i == "No" or i == "no" or i =="NO"):
    ismale = True
if ismale and istall:
    print("You are a tall male")
elif ismale and not(istall):
    print("You are a short male")
elif istall and not(ismale):
    print("You are not a male but you are tall")
else:
    print("You are not a male and your height is short")






