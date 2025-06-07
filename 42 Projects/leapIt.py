from tkinter import *

win = Tk()
win.title("Leap It")
win.geometry("270x50")
win.resizable(height=False, width=False)
win.rowconfigure([0, 1], weight=0)
win.columnconfigure([0, 1, 2], weight=0)

# Status
Label(win, text="Result: ").grid(row=0, column=0)
result = Label(win, text="...")
result.grid(row=0, column=1, columnspan=2, sticky="w")

# Label
Label(win, text="Enter Year YYYY: ").grid(row=1, column=0)

# Entry
date = Entry(win, textvariable=IntVar(), relief=RAISED)
date.grid(row=1, column=1)


# Engine
def check():
    global date, result
    try:
        year = int(date.get())

        # Validate year
        if year <= 0:
            raise EXCEPTION

        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            result.config(text=f"True! {year} is a leap year")
        else:
            result.config(text=f"False! {year} is not a leap year")
        return
    except:
        result.config(text="Enter a valid Year YYYY.")


# Btn
Button(win, text="Check", relief=RAISED, command=check).grid(row=1, column=2)

win.mainloop()
