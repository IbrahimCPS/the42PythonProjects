#IbrahimCPS
from random import randint
print('\t','=' * 15, sep='')
print("""\t= Lets's Play =\n\t=  Dice Role  =""")
print('\t','=' * 15, sep='')
def main():
    rolls = 0
    #Rolling function
    def roll():
        return randint(1, 6)

    #game engine.
    while True:
        ask = input("Enter r to roll or e to exit! : ")
        if ask == "r":
            rolls += 1
            print("\nRoll #: " + str(rolls))
            print("Result : " + str(roll()))
        elif ask == "e":
            print("\nExiting...")
            exit()
        else:
            print("\nUnkwon Answer!!!")
#calling main function.
main()
