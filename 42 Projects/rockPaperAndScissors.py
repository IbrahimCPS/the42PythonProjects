import random
from tkinter import *

window = Tk()
window.title("ROCK,PAPER AND SCISSOR")
window.geometry("200x150")
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=0)
window.columnconfigure([0, 1, 2], weight=1)
window.resizable(width=False, height=False)
window.grid_propagate(0)


# PC choise
def letsee():
    choises = ["rock", "paper", "scissor"]
    return random.choice(choises)


# rock
def rock():
    pc = letsee()
    me = "rock"
    pcChoise.config(text=pc)
    meChoise.config(text=me)
    check(me, pc)
    return


# paper
def paper():
    pc = letsee()
    me = "paper"
    pcChoise.config(text=pc)
    meChoise.config(text=me)
    check(me, pc)
    return


# scissor
def scissor():
    pc = letsee()
    me = "scissor"
    pcChoise.config(text=pc)
    meChoise.config(text=me)
    check(me, pc)
    return


# check wins
def check(m, p):
    global mval, pval
    if m == p:
        status.config(text="Tie.")
    elif m == "rock":
        if p == "scissor":
            status.config(text="Rock smash scissor! You win.")
            mval += 1
            meScore.config(text=mval)
        else:
            status.config(text="Paper cover rock! You lose.")
            pval += 1
            pcScore.config(text=pval)
    elif m == "paper":
        if p == "rock":
            status.config(text="Paper cover rock! You win.")
            mval += 1
            meScore.config(text=mval)
        else:
            status.config(text="Scissor cuts paper! You lose.")
            pval += 1
            pcScore.config(text=pval)
    elif m == "scissor":
        if p == "paper":
            status.config(text="Scissor cuts paper! You win.")
            mval += 1
            meScore.config(text=mval)
        else:
            status.config(text="Rock smash scissor! You lose.")
            pval += 1
            pcScore.config(text=pval)
    return


# Head
Label(window, text="ROCK, PAPER AND SCISSOR", justify="center").grid(row=0, column=0, columnspan=3)

# Me
mval = 0
Label(window, text="Me").grid(row=1, column=1)
meScore = Label(window, text=mval)
meScore.grid(row=2, column=1)

# PC
pval = 0
Label(window, text="PC").grid(row=1, column=2)
pcScore = Label(window, text=pval)
pcScore.grid(row=2, column=2)

# Scores
Label(window, text="Score: ").grid(row=2, column=0)

# Choises
Label(window, text="Choises: ").grid(row=3, column=0)
meChoise = Label(window, text="...")
pcChoise = Label(window, text="...")
meChoise.grid(row=3, column=1)
pcChoise.grid(row=3, column=2)

# Status
status = Label(window, text="let's play! have U'r Choise")
status.grid(row=4, column=0, columnspan=3)

# Middle belt
Frame(window, relief=RAISED, height=10, bg="black").grid(row=5, column=0, columnspan=3, sticky="snew")

# Btns
Button(window, text="Rock", relief=RAISED, command=rock).grid(row=6, column=0)
Button(window, text="Paper", relief=RAISED, command=paper).grid(row=6, column=1)
Button(window, text="Scissor", relief=RAISED, command=scissor).grid(row=6, column=2)

window.mainloop()
