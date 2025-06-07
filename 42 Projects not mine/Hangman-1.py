#Guessing word game, project 6 out of 42
import random as r
def ran():
                    k = r.randint(0,4)
                    words=["somethings", "apple","houses","nigeria","bag"]
                    return words[k]
word= ran()
words1= [word]
count= len(word)+3
guess= []
for x in range(len(word)):
    guess.append('_')
def main():
    guessLetter = input("Enter any letter: ")
    if len(guessLetter) != 1:
        print("\nInput must be a single letter")
        main()
    else:
        if guessLetter in word:
            ind= doubles(guessLetter)
            for y in ind:
                guess[y]=guessLetter
            str= "\t"
            for x in guess:
                str+=" {0}".format(x)
            print("\n\tCorrect!!!")
            print(str.upper())
        else:
            print("\nletter not found try again")
            return True
            
def doubles(x):
        count=0
        index = []
        for y in word:
            if x == y:
                index.append(count)
            count+=1
        return index   

         
while True:
    main()
    if count == 0:
            print("\tYou failed to guess the letter, You lose")
            print("The answer was {0}".format(words1[0].upper()))
            x=input("\t Do you want to play again (Yes or No): ").upper()
            if x == "YES":
                word= ran()
                count += len(word)+3
                guess = []
                for x in range (len(word)):
                    guess.append("_")
                main()
            else:
                print("Thanks for playing")
                break
    elif not "_" in guess:
        print ("You did it, you guessed the word")
        x=input("\t Do you want to play again (Yes or No): ").upper()
        if x == "YES":
                word = ran()
                count += len(word)+3
                guess = []
                for x in range(len(word)):
                    guess.append("_")
                main()
        else:
                print("Thanks for playing")
                break
    else:
            if main():
                count -= 2
            
    
