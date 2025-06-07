from tkinter import *
from tkinter.messagebox import *


class passwd_generator:
    store = []

    def __init__(self):
        self.main = Tk()
        self.main.title("Password Generator")
        self.main.geometry("300x100")
        self.main.columnconfigure([0, 61, 2], weight=2)
        self.main.rowconfigure([0, 1, 2], weight=1)
        self.main.configure(bg="lightblue")

        self.label = Label(self.main, text="enter any word to generate password", font="Arial 9", bg='lightblue')
        self.label.grid(row=0, columnspan=3)
        self.entry = Entry(self.main, width=20, font="bold 15", justify=RIGHT)
        self.entry.grid(row=1, columnspan=3, sticky="S")
        self.button = Button(self.main, text="generate", command=self.get_new)
        self.button.grid(row=2, columnspan=3, sticky="N")

        self.main.mainloop()

    def get_new(self):
        global store
        user_pass = self.entry.get()
        new_pass = self.key(user_pass)
        self.entry.delete(0, END)
        if user_pass in self.store and user_pass != "":
            showinfo("Not allowed", "You can reEnter\nGenerated passwd")
        else:
            self.store.append(new_pass)
            self.entry.insert(0, new_pass)

    def key(self, passwd):
        key = {
            "A": "$a", "B": "ddx", "C": "Ed4", "D": "%e",
            "E": "@t", "F": "Th", "G": "1`", "H": "00",
            "I": "Xv", "J": "$j", "K": "4k", "L": "te",
            "M": "r0", "N": "Rt", "O": "!no", "P": "Dy",
            "Q": "&r", "R": "Tc", "S": "4$", "T": "Sb",
            "U": "Ki", "V": "%n", "W": "Ty", "X": "bc",
            "Y": "5x", "Z": "P7", "a": "0F", "b": "8L",
            "c": "%ss", "d": "CO", "e": "FZ", "f": "MU",
            "g": "Y6", "h": "*7", "i": "Bs", "j": "Yk",
            "k": "ad", "l": "Bx", "m": "NN", "n": "@r",
            "o": "&y", "p": "JO", "q": "R9", "r": "%H",
            "s": "#V", "t": "YT", "u": "9x", "v": "T5",
            "w": "FR", "x": "0L", "y": "XT", "z": "Ek"
        }
        new_passwd = ""
        for ch in passwd:
            if ch in key:
                new_passwd += key[ch]
                continue
            new_passwd += ch
        return new_passwd


call = passwd_generator()
