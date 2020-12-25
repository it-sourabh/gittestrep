ask = input("Do you want to to enter phrase yourself: ")
if ask == "yes":
    pphrase = input("Enter it: ")
    print(pphrase)
else:
    pphrase = "Hi There, How are ya doing"
    print(pphrase)
p = input("Enter the letter to replace: ")
m = input("Enter the letter with which it will be replaced: ")
def transl(phrase, l, k):
    translation = ""
    for letter in phrase:
        if letter in k:
            if letter.isupper():
                translation = translation + l.upper()
            else:
                translation = translation +l.lower()
        else:
            translation = translation + letter
    return translation


print(transl(pphrase, m, p))
exit = input("Please press anything to quit: ")
