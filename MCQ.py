from Question import Question

Qs = ["What is the full form of VPN ?\n(a): Virtual Pathetic Network\n(b): Visual Private Network\n(c): Virtual "
      "Private Network\n\n",
      "When was Auto-MDIX launched ?\n(a): 2007\n(b): 2005\n(c): 2009\n\n",
      "Which of the following maintains a CAM table ?\n(a): Hub\n(b): Bridge\n(c): Switch\n\n",
      "What is the ASCII value of 'a' ?\n(a): 127\n(b): 65\n(c): 97\n\n",
      "Which is the strongest type of authorisation control ?\n(a): DAC\n(b): MAC\n(c): RBAC\n\n",
      "Which is stronger protocol for authentication ?\n(a): PAP\n(b): CHAP\n(c): Both are equal\n\n",
      "Which of the following is used for SSO(Single Sign-On) ?\n(a): LDAP\n(b): RADIUS\n(c): Kerberos\n\n",
      "Which of the following is more secure ?\n(a): TACACS+\n(b): DIAMETER\n(c): RADIUS\n\n",]

questions = [
         Question(Qs[0], "c"),
         Question(Qs[1], "a"),
         Question(Qs[2], "c"),
         Question(Qs[3], "c"),
         Question(Qs[4], "b"),
         Question(Qs[5], "b"),
         Question(Qs[6], "c"),
         Question(Qs[7], "a"),
]

questions1 = [
         Question(Qs[2], "c"),
         Question(Qs[1], "a"),
         Question(Qs[7], "a"),
         Question(Qs[6], "c"),
         Question(Qs[3], "c"),
         Question(Qs[5], "b"),
         Question(Qs[4], "b"),
         Question(Qs[0], "c"),
]

def run(questions):
    score = 0
    cor = 0
    wro = 0
    for q in questions:
         ans = input(q.ques)
         if ans == q.ans:
             print("You got this one correct, you get 5 points\n")
             score += 5
             cor +=1
         else:
             print("That is incorrect\n")
             wro += 1
    print(""
          ""
          "                      You got " + str(cor) + " correct and " + str(wro) + " wrong")
    print(""
          ""
          "                      You scored " + str(score) + " out of " + str(len(Qs)*5) + " points\n")
    if score >= 30:
        print("                  You won this game\n\n")
    elif score < 30:
        print("                  You lost this game")
        print("                  You need at least 30 points to win\n\n")

v = 1000
while v != 0:
    if v == 1000:
        run(questions)
        v -= 1
    elif v%2 == 1:
        again = input("                            Do you want to play again ?: ")
        if again == "Yes" or again == "yes":
            run(questions1)
        elif again == "No" or again == "no":
            print("                                    As you wish")
            v = 0
        else:
            print("Please answer in yes or no")
    elif v%2 == 0:
        again = input("                            Do you want to play again ?: ")
        if again == "Yes" or again == "yes":
            run(questions)
        elif again == "No" or again == "no":
            print("                                    As you wish")
            v = 0
        else:
            print("Please answer in yes or no")



