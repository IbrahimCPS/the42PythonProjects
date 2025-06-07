from tkinter import *

# Setup window.
window = Tk()
window.geometry("200x250")
window.title("Calculator")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1], weight=0)
window.columnconfigure(0, weight=0)
window["bg"] = "#9c978c"
window.grid_propagate(0)

# Screen Frames.
bgScreen = "#9c978c"
fgScreen = "white"
frameScreen = Frame(window, relief=RAISED, width=200, height=50, borderwidth=5, bg=bgScreen)
frameScreen.rowconfigure([0, 1], weight=1)
frameScreen.columnconfigure(0, weight=1)
frameScreen.grid_propagate(0)
frameScreen.grid(row=0, column=0)

# Display.
# Accept 31 character including space is found.
displayIn = Label(frameScreen, text="", bg=bgScreen, fg=fgScreen)
displayOut = Label(frameScreen, text="= 0", bg=bgScreen, fg=fgScreen)
displayIn.grid(row=0, column=0, sticky="se")
displayOut.grid(row=2, column=0, sticky="se")

# Keys Frames.
frameKeys = Frame(window, relief=RAISED, width=200, height=200, borderwidth=5)
frameKeys.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=36)
frameKeys.columnconfigure([0, 1, 2, 3], weight=1, minsize=46)
frameKeys.grid_propagate(0)
frameKeys.grid(row=1, column=0)


# Keys Buttons And Functions
def clear():
    text = displayIn["text"]
    length = len(text)

    if length == 0:
        displayOut.config(text="= 0")
    else:
        displayIn.config(text=text[:length - 1])


def braces():
    text = displayIn["text"]
    length = len(text)
    openBracket = 0
    closeBracket = 0

    for i in text:
        if i == "(":
            openBracket += 1
        elif i == ")":
            closeBracket += 1

    if openBracket == closeBracket or openBracket == length:
        text += "("
        displayIn.config(text=text)
    else:
        text += ")"
        displayIn.config(text=text)

    # Check if two braces is front and back like )( and replaced with )*( for eval funtion.
    if ")(" in text:
        changed = text.replace(")(", ")*(")
        displayIn.config(text=changed)
    bracesLaw()


# check braces if ...( or )... and replaced with *( or )*
def bracesLaw():
    text = displayIn["text"]
    for i in range(10):
        if f"{i}(" in text:
            changed = text.replace(f"{i}(", f"{i}*(")
            displayIn.config(text=changed)
        elif f"){i}" in text:
            changed = text.replace(f"){i}", f")*{i}")
            displayIn.config(text=changed)

    if ".(" in text:
        changed = text.replace(".(", ".*(")
        displayIn.config(text=changed)
    elif ")." in text:
        changed = text.replace(").", ")*0.")
        displayIn.config(text=changed)


def perc():
    text = displayIn["text"]
    text += "%"
    displayIn.config(text=text)


def devide():
    text = displayIn["text"]
    text += "/"
    displayIn.config(text=text)


def seven():
    text = displayIn["text"]
    text += "7"
    displayIn.config(text=text)
    bracesLaw()


def eight():
    text = displayIn["text"]
    text += "8"
    displayIn.config(text=text)
    bracesLaw()


def nine():
    text = displayIn["text"]
    text += "9"
    displayIn.config(text=text)
    bracesLaw()


def multiply():
    text = displayIn["text"]
    text += "*"
    displayIn.config(text=text)


def four():
    text = displayIn["text"]
    text += "4"
    displayIn.config(text=text)
    bracesLaw()


def five():
    text = displayIn["text"]
    text += "5"
    displayIn.config(text=text)
    bracesLaw()


def six():
    text = displayIn["text"]
    text += "6"
    displayIn.config(text=text)
    bracesLaw()


def minus():
    text = displayIn["text"]
    text += "-"
    displayIn.config(text=text)


def one():
    text = displayIn["text"]
    text += "1"
    displayIn.config(text=text)
    bracesLaw()


def two():
    text = displayIn["text"]
    text += "2"
    displayIn.config(text=text)
    bracesLaw()


def three():
    text = displayIn["text"]
    text += "3"
    displayIn.config(text=text)
    bracesLaw()


def addition():
    text = displayIn["text"]
    text += "+"
    displayIn.config(text=text)


def zero():
    text = displayIn["text"]
    text += "0"
    displayIn.config(text=text)
    bracesLaw()


def dot():
    text = displayIn["text"]
    text += "."
    displayIn.config(text=text)
    bracesLaw()


def equal():
    text = displayIn["text"]
    try:
        evaluate = eval(text)
    except:
        evaluate = "Error"
    customizeAdd = f"= {evaluate}"
    displayOut.config(text=customizeAdd)


# First Row.
specialBtnColor = "#808080"
remainBtnColor = "#9c978c"
Button(
    frameKeys,
    text="C",
    relief=RAISED,
    fg="red",
    font=("italic", "25"),
    bg=specialBtnColor,
    command=clear
).grid(row=0, column=0, sticky="snew")
Button(
    frameKeys,
    text="()",
    relief=RAISED,
    font=("normal", "10"),
    bg=specialBtnColor,
    command=braces
).grid(row=0, column=1, sticky="snew")
Button(
    frameKeys,
    text="%",
    relief=RAISED,
    font=("normal", "10"),
    bg=specialBtnColor,
    command=perc
).grid(row=0, column=2, sticky="snew")
Button(
    frameKeys,
    text="/",
    relief=RAISED,
    font=("normal", "10"),
    bg=specialBtnColor,
    command=devide
).grid(row=0, column=3, sticky="snew")

# Second Column.
Button(
    frameKeys,
    text="7",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=seven
).grid(row=1, column=0, sticky="snew")
Button(
    frameKeys,
    text="8",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=eight
).grid(row=1, column=1, sticky="snew")
Button(
    frameKeys,
    text="9",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=nine
).grid(row=1, column=2, sticky="snew")
Button(
    frameKeys,
    text="*",
    relief=RAISED,
    font=("normal", "10"),
    bg=specialBtnColor,
    command=multiply
).grid(row=1, column=3, sticky="snew")

# Third Column.
Button(
    frameKeys,
    text="4", relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=four
).grid(row=2, column=0, sticky="snew")
Button(
    frameKeys,
    text="5",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=five
).grid(row=2, column=1, sticky="snew")
Button(
    frameKeys,
    text="6",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=six
).grid(row=2, column=2, sticky="snew")
Button(
    frameKeys,
    text="-",
    relief=RAISED,
    font=("normal", "10"),
    bg=specialBtnColor,
    command=minus
).grid(row=2, column=3, sticky="snew")

# Fourth Column.
Button(
    frameKeys,
    text="1",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=one
).grid(row=3, column=0, sticky="snew")
Button(
    frameKeys,
    text="2",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=two
).grid(row=3, column=1, sticky="snew")
Button(
    frameKeys,
    text="3",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=three
).grid(row=3, column=2, sticky="snew")
Button(
    frameKeys,
    text="=",
    relief=RAISED,
    font=("normal", "10"),
    bg=specialBtnColor,
    command=equal
).grid(row=3, column=3, rowspan=2, sticky="snew")

# Fivth Column.
Button(
    frameKeys,
    text="0",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=zero
).grid(row=4, column=0, sticky="snew")
Button(
    frameKeys,
    text=".",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=dot
).grid(row=4, column=1, sticky="snew")
Button(
    frameKeys,
    text="+",
    relief=RAISED,
    font=("normal", "10"),
    bg=remainBtnColor,
    command=addition
).grid(row=4, column=2, sticky="snew")

window.mainloop()
