#IbrahimCPS

print("""
\t   I'm a bot V1.0
\t Made by IbrahimCPS
""")
#Questions Function
def question():
    #First question.
    while True:
        print("\n\n")
        print("Who am I?", end=" ")
        ans1 = input("a bot! yes/no: ")
        if ans1 == "yes":
            ans1 = "yes"
            
        elif ans1 == "no":
            ans1 = "no"
        else:
            print("\nWrong answer!!!")
            continue
        break

    #Second question.
    while True:
        print("\n\n")
        print("Who made me?", end=" ")
        ans2 = input("IbrahimCPS! yes/no: ")
        if ans2 == "yes":
            ans2 = "yes"
        elif ans2 == "no":
            ans2 = "no"
        else:
            print("\nWrong answer!!!")
            continue
        break

    #Third question.
    while True:
        print("\n\n")
        print("What's my version?", end=" ")
        ans3 = input("V1.2! yes/no: ")
        if ans3 == "yes":
            ans3 = "yes"
        elif ans3 == "no":
            ans3 = "no"
        else:
            print("\nWrong answer!!!")
            continue
        break

    #Results
    print("\n RESULT ")
    print("=" * 10)
    if ans1 == "yes" and ans2 == "yes" and ans3 == "no":
        print("=  Win   =")
        print("=" * 10)
    else:
        print("=  Lose  =")
        print("=" * 10)
              

#Main Start
while True:
    ask_bot = input("Are you ready to answer a question about me? yes/no. : ")
    if ask_bot == "yes":
        question()
    elif ask_bot == "no":
        print("\nYou are not ready GoodBye.")
    else:
        print("\nWrong answer!!!")
        continue
    break
