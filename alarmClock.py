import time
from tkinter import *
from tkinter import messagebox, ttk
import plyer
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst as gst
from gi.repository import GObject as gobject

# Set-up text file database.
while True:
    try:
        with open("./database.txt", "r+") as file:
            if file.read() == "":
                file.write("link\n")
                break
            else:
                break
    except:
        # Creat file.
        open("./database.txt", "x")
        continue
# Time for next movie in second
timeInSec = 0


# Get time for next movies.
def Timer():
    # Setup window.
    win = Tk()
    win.geometry("200x180")
    win.title("Set Timer")
    win.resizable(width=False, height=False)
    win.rowconfigure([0, 1, 2, 3, 4, 5], weight=0)
    win.columnconfigure([0, 1, 2], weight=1)

    # Heading.
    Label(win, text="SET TIME", font=("bold", "15")).grid(row=0, column=0, columnspan=3)

    # Heading 2.
    Label(win, text="HOURS").grid(row=1, column=0)
    Label(win, text="MINUTES").grid(row=1, column=1)
    Label(win, text="SECONDS").grid(row=1, column=2)

    # Time entry.
    hours = IntVar()
    minutes = IntVar()
    seconds = IntVar()
    hours.set("00")
    minutes.set("00")
    seconds.set("00")
    Entry(win, textvariable=hours, relief=RAISED, justify="center").grid(row=3, column=0)
    Entry(win, textvariable=minutes, relief=RAISED, justify="center").grid(row=3, column=1)
    Entry(win, textvariable=seconds, relief=RAISED, justify="center").grid(row=3, column=2)

    # Frame Button Set and Reset.
    frameSAR = Frame(win, relief=RAISED, width=200, height=25)
    frameSAR.rowconfigure(0, weight=0)
    frameSAR.columnconfigure([0, 1], weight=1)
    frameSAR.grid_propagate(0)
    frameSAR.grid(row=5, column=0, columnspan=3)

    def reset():
        hours.set("00")
        minutes.set("00")
        seconds.set("00")
        global timeInSec
        timeInSec = 0

    def setTime():
        try:
            timeInSeconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
            if timeInSeconds == 0:
                EXCEPTION()
            global timeInSec
            timeInSec = timeInSeconds
            win.destroy()
        except:
            hours.set("00")
            minutes.set("00")
            seconds.set("00")
            messagebox.showwarning("Value Error", "Pls enter a valid time")

    def ifClose():
        global timeInSec
        if timeInSec == 0:
            timeInSec = 10
            messagebox.showerror("Zero Value", "Goint to use 10secs for next movies.")
            win.destroy()
        else:
            win.destroy()

    # Disable close win.
    win.protocol("WM_DELETE_WINDOW", ifClose)

    # Button Set.
    Button(
        frameSAR,
        text="""  SET  """,
        relief=RAISED,
        height=1,
        command=setTime
    ).grid(row=0, column=0, sticky="e")
    # Button Reset.
    Button(
        frameSAR,
        text="RESET",
        relief=RAISED,
        height=1,
        command=reset
    ).grid(row=0, column=1, sticky="w")

    win.mainloop()
    return True


class main:
    # Initiallization time.
    Timer()

    def __init__(self):
        global timeInSec

        # Setup window.
        window = Tk()
        window.title("Alarm Clock")
        window.resizable(width=False, height=False)
        window.rowconfigure([0, 1], weight=0)
        window.columnconfigure(0, weight=0)

        # Timer-display frame.
        timerFrame = Frame(window, height=20)
        timerFrame.rowconfigure(0, weight=0)
        timerFrame.columnconfigure([0, 1], weight=0)
        timerFrame.grid(row=0, column=0, sticky="we")

        Label(timerFrame, text="Next Movie in:  ").grid(row=0, column=0)
        # Progressbar.
        pgbar = ttk.Progressbar(
            timerFrame,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        pgbar.grid(row=0, column=1, padx=5, pady=5)
        pgbarTextInSecs = Label(timerFrame, text=timeInSec)
        pgbarTextInSecs.grid(row=0, column=1, sticky="w")

        # Video Frame no control.
        movieFrame = Frame(window, bg="black", height=300)
        movieFrame.grid(row=1, column=0, sticky="nesw")

        while timeInSec > -1:

            # window update for the value
            window.update()
            time.sleep(1)

            # Set up time.
            pgbarTextInSecs.config(text=str(timeInSec))

            # Alert.
            if timeInSec == 0:
                osAleart = plyer.notification
                osAleart.notify(
                    title="Playing next movie",
                    message="Time's up!, Nest Movie!...",
                    app_name="Alarm Clock",
                    app_icon="",
                    timeout=10,
                    ticker="New message has arrived",
                    toast=True
                )
                # Time Up.
                messagebox.showinfo("Timer!", "Time's up!")

            timeInSec -= 1
        window.mainloop()


main()
