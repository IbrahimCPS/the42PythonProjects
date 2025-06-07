import math
from tkinter import *

win = Tk()
win.title("Find Fibonacci")
win.geometry("270x50")
win.resizable(height=False, width=False)
win.rowconfigure([0, 1], weight=0)
win.columnconfigure([0, 1, 2], weight=0)

# Status
Label(win, text="Result: ").grid(row=0, column=0)
result = Label(win, text="...")
result.grid(row=0, column=1, columnspan=2, sticky="w")

# Label
Label(win, text="Enter a number: ").grid(row=1, column=0)

# Entry
entry = Entry(win, textvariable=IntVar(), relief=RAISED)
entry.grid(row=1, column=1)


# Engine
def check():
    global entry, result
    try:
        number = int(entry.get())

        # Is Perfect Square?
        def isPerfectSqure(n):
            s = int(math.sqrt((n)))
            return s * s == n

        # Is Fibonacci?
        def isFibonacci(n):
            return isPerfectSqure(5 * n * n + 4) or isPerfectSqure(5 * n * n - 4)

        if isFibonacci(number):
            result.config(text=f"True! {number} is a fibonacci")
        else:
            result.config(text=f"False! {number} is not a fibonacci")
        return
    except:
        result.config(text="Enter a number pls.")


# Btn
Button(win, text="Check", relief=RAISED, command=check).grid(row=1, column=2)

win.mainloop()
