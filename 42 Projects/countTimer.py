import time
from tkinter import *
from tkinter import messagebox
import plyer as pl

# Setup window.
window = Tk()
window.geometry("200x180")
window.title("Count Down Timer")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1, 2, 3, 4, 5], weight=0)
window.columnconfigure([0, 1, 2], weight=1)

# Heading.
Label(window, text="T  I  M  E  R", font=("bold", "15")).grid(row=0, column=0, columnspan=3)

# Heading 2
Label(window, text="HOURS").grid(row=1, column=0)
Label(window, text="MINUTES").grid(row=1, column=1)
Label(window, text="SECONDS").grid(row=1, column=2)

# Buttons △:later
# Button(window, text="△", relief=RAISED, height=1).grid(row=2, column=0, sticky="snew")
# Button(window, text="△", relief=RAISED, height=1).grid(row=2, column=1, sticky="snew")
# Button(window, text="△", relief=RAISED, height=1).grid(row=2, column=2, sticky="snew")

# Time entry.
hours = IntVar()
minutes = IntVar()
seconds = IntVar()
hours.set("00")
minutes.set("00")
seconds.set("00")
Entry(window, textvariable=hours, relief=RAISED, justify="center").grid(row=3, column=0)
Entry(window, textvariable=minutes, relief=RAISED, justify="center").grid(row=3, column=1)
Entry(window, textvariable=seconds, relief=RAISED, justify="center").grid(row=3, column=2)

# Button ▽:later
# Button(window, text="▽", relief=RAISED, height=1).grid(row=4, column=0, sticky="snew")
# Button(window, text="▽", relief=RAISED, height=1).grid(row=4, column=1, sticky="snew")
# Button(window, text="▽", relief=RAISED, height=1).grid(row=4, column=2, sticky="snew")

# Frame Button Set and Reset
frameSAR = Frame(window, relief=RAISED, width=200, height=25)
frameSAR.rowconfigure(0, weight=0)
frameSAR.columnconfigure([0, 1], weight=1)
frameSAR.grid_propagate(0)
frameSAR.grid(row=5, column=0, columnspan=3)

stop = False



def setTime():
    try:
        timeInSeconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except:
        hours.set("00")
        minutes.set("00")
        seconds.set("00")
        messagebox.showwarning("Value Error", "Pls enter a valid time", "Okay")

    while timeInSeconds > -1:
        # For stop
        global stop
        if stop:
            stop = False
            break

        mins, secs = divmod(timeInSeconds, 60)
        hour = 0
        # Convert minutes to hours
        if mins > 60:
            hour, mins = divmod(mins, 60)

        # Set up time
        hours.set(f"{hour:02d}")
        minutes.set(f"{mins:02d}")
        seconds.set(f"{secs:02d}")

        # window update for the value
        window.update()
        time.sleep(1)

        if timeInSeconds == 0:
            osAleart = pl.notification
            osAleart.notify(
                title="Python Timer",
                message="Time's up!, Alear!...",
                app_name="Timer Count Down",
                app_icon="",
                timeout=10,
                ticker="New message has arrived",
                toast=True)
            messagebox.showinfo("Timer!", "Time's up!")

        timeInSeconds -= 1


def reset():
    hours.set("00")
    minutes.set("00")
    seconds.set("00")


# Button Set
Button(frameSAR, text="""  SET  """, relief=RAISED, height=1, command=setTime).grid(row=0, column=0, sticky="e")
# Button Reset
Button(frameSAR, text="RESET", relief=RAISED, height=1, command=reset).grid(row=0, column=1, sticky="w")

window.mainloop()
