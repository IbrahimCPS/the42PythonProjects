#IbrahimCPS
def main():
    print("""
\t Have a nice day!
\t RULE: Guess the first unknwon before next one!
\n
""")
    
    #game function:
    def game():
        
        """
        Words!
            Unordered!     Ordered!
        1: Fra_cis.     = Francis.
        2: Ibra_i_CPS.  = IbrahimCPS.
        3: Ab_ulr_hm_n. = Abdulrahmon.
        """
        #My words variable list.
        unOrdered = ["Fra_cis", "Ibra_i_CPS", "Ab_ulr_hm_n"]
        ordered = ["Francis", "IbrahimCPS", "Abdulrahmon"]

        #Checking weather the answer is correct or no.
        def check(q, v, a):
            #q = question no#.
            #v = values steps.
            #a = answers.
            if int(q) == 0:
                cuts = unOrdered[0].split("_")
                if cuts[0] + a + cuts[1] == ordered[0]:
                    return True
                else:
                    return False
            elif int(q) == 1:
                cuts = unOrdered[1].split("_")
                if int(v) == 0:
                    if cuts[0] + a + cuts[1] + "m" + cuts[2] == ordered[1]:
                        return True
                    else:
                        return False
                else:
                    if cuts[0] + a + cuts[1] == ordered[1]:
                        return True
                    else:
                        return False
            else:
                cuts = unOrdered[2].split("_")
                if int(v) == 0:
                    if cuts[0] + a + cuts[1] + "a" + cuts[2] + "o" + cuts[3] == ordered[2]:
                        return True
                    else:
                        return False
                elif int(v) == 1:
                    if cuts[0] + a + cuts[1] + "o" + cuts[2] == ordered[2]:
                        return True
                    else:
                        return False
                else:
                    if cuts[0] + a + cuts[1] == ordered[2]:
                        return True
                    else:
                        return False

                
        #main game engine.
        while True:
            question = 0
            values = 0
            leftTries = 5
            
            #level 1
            while True:
                print("\nLevel #1")
                print(f"Tries {leftTries} lefts ")
                print(f"Target word: {unOrdered[0]}")
                print("Guess a letter from a-z: ", end="")
                guess = input("")
                
                #check if guess not an alphabet.
                if not guess.isalpha():
                    print("\nWrong answer!!!")
                    continue
                
                #if guess is morethan one.
                if len(guess) > 1:
                    print("\nPls one alphabet is allowed.")
                    continue

                #check tries lefts if 1 left gameOver it cancel next run.
                if leftTries == 1:
                    print(f"""
\n
Tries {leftTries} lefts 
Game Over!!!
""")
                    print("Did you want play again yes/no: ", end="")
                    ask = input("")
                    if ask == "yes":
                        play("yes")
                    elif ask == "no":
                        play("no")
                    else:
                        print("\nUnkown answer!!!")
                        print("Replay...")
                        play("yes")
                        
                if check(question, values, guess) == True and int(values) == 0:
                    cuts = unOrdered[0].split("_")
                    unOrdered[0] = cuts[0] + "n" + cuts[1]
                    print(f"\nTarget word: {unOrdered[0]}")
                    print("You won!")
                    print("Congratulation...")
                    print("Next level...")
                    question = 1
                    break
                else:
                    print("\nAlphabet wrong!!!")
                    leftTries -= 1
                    continue


            #level 2
            while True:
                print("\nLevel #2")
                print(f"Tries {leftTries} lefts ")
                print(f"Target word: {unOrdered[1]}")
                print("Guess a letter from a-z: ", end="")
                guess = input("")
                
                #check if guess not an alphabet.
                if not guess.isalpha():
                    print("\nWrong answer!!!")
                    continue
                
                #if guess is morethan one.
                if len(guess) > 1:
                    print("\nPls one alphabet is allowed.")
                    continue

                #check tries lefts if 1 left gameOver it cancel next run.
                if leftTries == 1:
                    print(f"""
\n
Tries {leftTries} lefts 
Game Over!!!
""")
                    print("Did you want play again yes/no: ", end="")
                    ask = input("")
                    if ask == "yes":
                        play("yes")
                    elif ask == "no":
                        play("no")
                    else:
                        print("\nUnkown answer!!!")
                        print("Replay...")
                        play("yes")
                        
                if check(question, values, guess) == True and int(values) == 0:
                    cuts = unOrdered[1].split("_")
                    unOrdered[1] = cuts[0] + "h" + cuts[1] + "_" + cuts[2]
                    print(f"\nTarget word: {unOrdered[1]}")
                    print("You won!")
                    print("Congratulation...")
                    print("Next level...")
                    values = 1
                    continue
                elif check(question, values, guess) == True and int(values) == 1:
                    cuts = unOrdered[1].split("_")
                    unOrdered[1] = cuts[0] + "m" + cuts[1]
                    print(f"\nTarget word: {unOrdered[1]}")
                    print("You won!")
                    print("Congratulation...")
                    print("Next level...")
                    question = 3
                    values = 0
                    break
                else:
                    print("\nAlphabet wrong!!!")
                    leftTries -= 1
                    continue

            #level 3
            while True:
                print("\nLevel #3")
                print(f"Tries {leftTries} lefts ")
                print(f"Target word: {unOrdered[2]}")
                print("Guess a letter from a-z: ", end="")
                guess = input("")
                
                #check if guess not an alphabet.
                if not guess.isalpha():
                    print("\nWrong answer!!!")
                    continue
                
                #if guess is morethan one.
                if len(guess) > 1:
                    print("\nPls one alphabet is allowed.")
                    continue

                #check tries lefts if 1 left gameOver it cancel next run.
                if leftTries == 1:
                    print(f"""
\n
Tries {leftTries} lefts 
Game Over!!!
""")
                    print("Did you want play again yes/no: ", end="")
                    ask = input("")
                    if ask == "yes":
                        play("yes")
                    elif ask == "no":
                        play("no")
                    else:
                        print("\nUnkown answer!!!")
                        print("Replay...")
                        play("yes")
                        
                if check(question, values, guess) == True and int(values) == 0:
                    cuts = unOrdered[2].split("_")
                    unOrdered[2] = cuts[0] + "d" + cuts[1] + "_" + cuts[2] + "_" + cuts[3]
                    print(f"\nTarget word: {unOrdered[2]}")
                    print("You won!")
                    print("Congratulation...")
                    print("Next level...")
                    question = 3
                    values = 1
                    continue
                elif check(question, values, guess) == True and int(values) == 1:
                    cuts = unOrdered[2].split("_")
                    unOrdered[2] = cuts[0] + "a" + cuts[1] + "_" + cuts[2]
                    print(f"\nTarget word: {unOrdered[2]}")
                    print("You won!")
                    print("Congratulation...")
                    print("Next level...")
                    question = 3
                    values = 2
                    continue
                elif check(question, values, guess) == True and int(values) == 2:
                    cuts = unOrdered[2].split("_")
                    unOrdered[2] = cuts[0] + "o" + cuts[1]
                    print(f"\nTarget word: {unOrdered[2]}")
                    print("You won!")
                    print("Congratulation...")
                    print("Next level...")
                    question = 0
                    values = 0
                    break
                else:
                    print("\nAlphabet wrong!!!")
                    leftTries -= 1
                    continue
            break
        print("======")
        print("=Done=")
        print("======")

                
                
    
    #play and replay.
    def play(x):
        if x == "yes":
            game()
        else:
            print("\nExiting...")
            exit()
    play("yes")
    
#Calling main function.
main()
