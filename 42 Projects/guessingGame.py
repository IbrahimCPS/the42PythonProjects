#IbrahimCPS

import random


name = str(input('Your name pls: '))
print(f"""
      
      \t You are welcome Mr {name}.
      
""")

def game():
    number = random.randint(1, 10) #Generating random number from 1 to 10.
    tries = 3
    
    while True:
        print(f'You have {tries} left.')
        print('Guess a number from 1 to 10: ', end='')
        guess = input('') #Taking user guess number.

        #Input check to be valid as number
        if not guess.isdigit():
            print('\nWrong Number!')
            continue

        #Input check to be valid range
        if int(guess) < 1 or int(guess) > 10:
            print('\nNumber out of range')
            continue
        
        #Game Over.
        if tries == 1:
            while True:
                print(f'\nGame Over 0 left')
                tries = 3
                print('Did you want to play again y/n: ', end='')
                ask = input('')
                print()
                if ask == 'y':
                    break
                elif ask == 'n':
                    print('\nThank you. \nExisting...')
                else:
                    print('\nUnkown answer!')
                    continue
            continue
        
        #when number is not guessed.
        if int(guess) != number:
            if int(guess) > number:
                tries -= 1
                print(f"""
\n\n
Guess is hight.
Decrease the guess number: """)
                continue
            else:
                tries -= 1
                
                print(f"""
\n\n
Guess is low.
Increase the guess number: """)
                continue
        break
    
    #Last run after guessed the number. 
    print(f'\nYou guess the number in {tries} tries.!')
        
while True:
    print('\t Are you ready to start y/n. : ', end='')
    ask = input('')
    if ask == 'y':
        game()
    elif ask == 'n':
        print('Come back when ready!')
        exit()
    else:
        print('\nUnkown answer!')
        continue
