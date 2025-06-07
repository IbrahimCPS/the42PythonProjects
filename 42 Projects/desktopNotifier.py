import plyer as pl
import tkinter as tk

def alert():
    message = pl.notification
    message.notify(title="I'm the title", message="I am the main message, you can write any thing you want to notify", app_name="AppName", app_icon="", timeout=10, ticker="New message has arrived", toast=False)

window = tk.Tk()
window.geometry("280x100")
window.title("Desktop Notifier")
window.rowconfigure([0, 1, 2], weight=1, minsize=10)
window.columnconfigure([0, 1, 2], weight=1, minsize=10)

alertBtn = tk.Button(master=window, text="Send", command=alert, bg="black", fg="white", relief=tk.RAISED).grid(row=1, column=1, sticky="snew")
window.mainloop()
