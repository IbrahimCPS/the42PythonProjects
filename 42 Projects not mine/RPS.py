import random as rn
import tkinter as tk
import tkinter.messagebox as tm

player_value = 0
computer_value = 0
lst = ["rock", 'paper', 'scissor']

class RPS:
    value = 0
    num = rn.randint(0, 2)
    def __init__(self):
        global computer_value ,value


        self.main = tk.Tk()
        self.value = tk.StringVar()
        self.main.title("Rock Paper scissors")
        self.main.geometry("500x400")

        self.frame = tk.Frame(self.main)
        self.frame.grid()

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        self.frame.rowconfigure(0, weight=2)
        self.frame.rowconfigure(1, weight=2)
        self.frame.rowconfigure(2, weight=2)
        self.frame.rowconfigure(3, weight=1)

        self.rock_RB = tk.Radiobutton(self.frame, text= "Rock",value="rock", variable= self.value, font= ('bold', 17))
        self.rock_RB.grid(row=2, column=0, sticky= "S")

        self.paper_RB = tk.Radiobutton(self.frame, text= "paper", value= 'paper', variable= self.value, font= ("bold", 17))
        self.paper_RB.grid(row=2, column=1, sticky= "S")

        self.scissor_RB = tk.Radiobutton(self.frame, text= 'scissor', variable= self.value, value= 'scissor', font= ("bold", 17))
        self.scissor_RB.grid(row=2, column=2, sticky= 'S')

        self.label_Bt = tk.Button(self.frame, text='Click',  command= self.get_value, font= ('bold', 15))
        self.label_Bt.grid(row= 3, column= 1, sticky= "S", padx=20, pady= 20)

        self.computer_label = tk.Label(self.frame, text= 'Computer XP', font= ("Arial", 20))
        self.computer_label.grid(row=1, column= 0, sticky= "N", padx=20, pady=20)

        self.player_label = tk.Label(self.frame, text= 'Player Xp', font= ("Arial", 20))
        self.player_label.grid(row=1, column= 2, sticky= "N", padx=20 , pady= 20)

        self.intro = tk.Label(self.frame, text= "Welcome To Abdulrahmon\nRock Paper scissor \nproject", font = ("bold", 20))
        self.intro.grid(row=0, columnspan=3, padx=50, pady=50)

        self.main.mainloop()


    def get_value(self):
        global lst
        num = rn.randint(0, 2)
        computer = lst[num]
        player = self.value.get()
        self.game(player, computer)
        num = rn.randint(0, 2)


    def won(self):
        global player_value
        player_value += 1
        tm.showinfo("Player", "You won the round")
        self.player_label.config(text="Player Xp"+ str(player_value))


    def equal(self):
        tm.showinfo("Equal", "Equal you choose the same weapon")

    def com(self):
        global computer_value , value

        if len(self.value.get()) > 0:
            computer_value += 1
            tm.showinfo("Computer", "Computer won the round")
            self.computer_label.config(text= "Computer Xp"+ str(computer_value))
        if not len(self.value.get()) > 0:
            tm.showinfo("empty", 'Choose a weapon')


    def game(self, player, computer):
        if player == "scissor" and computer == "paper":
            self.won()
        elif player == "paper" and computer == "rock":
            self.won()
        elif player == "rock" and computer == "scissor":
            self.won()
        elif player == computer:
            self.equal()
        else:
            self.com()


me = RPS()





























