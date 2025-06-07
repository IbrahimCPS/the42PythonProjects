import tkinter as tk


class leap_year:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Leap Year Checker")
        self.main.geometry("300x300")
        self.main.columnconfigure( [0,1,2] , weight= 1)
        self.main.rowconfigure([0,1,2], weight= 1)

        self.res = tk.Label(self.main, text="Enter year", font=("Airal", 15))
        self.res.grid(row=0, columnspan=3, sticky= "S")

        self.label = tk.Label(self.main, text=":", font=("Airal", 15))
        self.label.grid(row=1, columnspan=3, sticky= "N")

        self.entry = tk.Entry(self.main, width=10)
        self.entry.grid(row=1, columnspan=3)

        self.button = tk.Button(self.main, text= "Check", command= self.call)
        self.button.grid(row=2, columnspan= 3, sticky= "N")



        self.main.mainloop()

    def call(self):
        years = self.entry.get()
        self.get_leap(years)

    def get_leap(self, years):
            #years = years.get()
            if years.isdigit():
                if (int(years) % 400 == 0) and (int(years) % 100 == 0):
                    self.label.config(text= "True")

                elif (int(years) % 4 == 0) and (int(years) % 100 != 0):
                    self.label.config(text="True")

                else:
                    self.label.config(text="False")
            else:
                self.label.config(text= "invalid")




call = leap_year()