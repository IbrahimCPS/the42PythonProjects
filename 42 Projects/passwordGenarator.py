import random
from tkinter import *
from tkinter import messagebox


def main():
    class passwordGen:
        def __init__(self):
            win = Tk()
            win.geometry("250x100")
            win.title("PassGen!")
            win.resizable(width=False, height=False)
            win.rowconfigure([0, 1, 2, 3], weight=0)
            win.columnconfigure([0, 1], weight=1)
            win.grid_propagate(0)

            # Label first
            Label(win, text="PASSWORD GEN!", font=("bold", "10")).grid(row=0, column=0, columnspan=2)

            # Output Label
            Label(win, text="password: ").grid(row=1, column=0, sticky="w")
            self.output = Label(win, text="")
            self.output.grid(row=1, column=1)

            # Input word entry
            Label(win, text="Enter a password: ", width=14).grid(row=2, column=0, sticky="w")
            self.inputs = Entry(win, textvariable=StringVar, width=24)
            self.inputs.grid(row=2, column=1, padx=2)

            # Genrate Btn
            Button(
                win,
                text="GENERATE",
                relief=RAISED,
                bg="black",
                fg="white",
                command=self.genPassword
            ).grid(
                row=3,
                column=0,
                columnspan=2,
                pady=5
            )
            win.mainloop()

        def genPassword(self):
            password = self.inputs.get()
            length = len(password)
            securedCharset = "?!@#$%&*_"

            # Validate input data
            if password == "" or length == 0:
                messagebox.showerror("Input Error!", "Please enter a valid password")
                return

            def getSecureChar():
                return random.choice(securedCharset)

            passwordSecured = []
            for i in range(length):
                passwordSecured.append(random.choice(password))

            passwordSecured.append(getSecureChar())
            passwordSecured.append(getSecureChar())
            self.output.config(text="".join(passwordSecured))

    start = passwordGen()


main()
