import random 


def main():
	print("Created by Abdulrahmon")
	print()
	
	another = "y"
	while another[0] == "y":
		
		word = get_word()
		M_index = guess_index(word)
		
		question , M_char = get_missing(word, M_index)
		intro(M_char)
		game(word, question, M_char)
		
		print("\nDid you want to play again")
		another = input("(yes/No) : ").lower()
		print()
		
	else:
		print("quiting...")
	

	
# this function return randomly word
# from the list 
def get_word():
	words = ["transition","undergo", "widespread", "vessel", "testimony", "theater", "subsequent"]
	num = random.randint(0,6)
	
	return words[num]	
	
	
	
# this function return index  of missing 
# character's in the word
def guess_index(word):	
	WordLen  = len(word) // 2
	
	missing  = []	
	for count in range(WordLen):
		
		num = random.randint(0, WordLen)		
		while num in missing:
			num = random.randint(0, WordLen)
						
		missing.append(num)
		
	return missing



# this function return two value , question (A__u_rah_o_) and 
# missing characters ([ b, d, l, m, n ])
def get_missing(word, indexs):
	Ques = ""
	missing_ch = []
	
	Counter = 0
	found = False

	for ch in word:
			for num in indexs:
				
				if Counter == num:
					Ques += "_"
					missing_ch.append(word[Counter])
					found = True

			if not found:
				Ques += ch

			Counter += 1
			found = False
	
	return Ques, missing_ch


def intro(M_char):
	XP = len(M_char)+2
	print('''    °°°°°°°°°
    |       |
    |      \U0001F924
    |
    |  Hang-Man 
    |
⁷⁷⁷⁷⁷⁷⁷⁷⁷⁷⁷⁷⁷⁷⁷''')
	print(f"\tyou have {XP}Xp")
	print("   with", len(M_char), "missing characters")
	print("Find the missing characters\n")
		
	
								

	
		
				
def game(word, question, M_char):
	
	Xp = len(M_char) +2	
	for trys in range(Xp):
		
# delete the 👇"#" for cheet 
		#print(word)
		print(question)
		text = input("Enter any letter from (a|z) : ").lower()
		
		while len(text) > 1:
			print("\nOne character per Trys")
			text = input("Enter another letter from (a|z) : ").lower()
			
		if text in M_char:
			Xp -= 1
			
			print("\nMatch Found")
			print(f"You have {Xp}Xp")
			print(f"and {len(M_char)-1} missing character left\n")
				
			position = word.index(text)
			word = add_char(word, position)			
			question = add_char(question, position, text)	
			M_char.remove(text)
			
		else:
			Xp -= 1
			
			print('\noops "', text, '" not among missing character')
			print(f"You have {Xp}Xp")
			print(f"and {len(M_char)} missing character left\n")
			
		if "_" not in question:
			print("**congrats**")
			print("You've found  the Missing  character")
			print("Word :", question.upper())
			break
			
		
			
	else:
		print("oops seem like the word is difficult")
		print()




def add_char(word,  index, char="_"):
		count = 0
		new_word = ""
		for ch in word:
				if count == index:
						new_word += char
				else:
				        new_word += ch
				count += 1
		return new_word 
	
		
			
					
main()
	
