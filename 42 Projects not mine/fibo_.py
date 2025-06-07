from tkinter import *


class fibonacci:

    def __init__(self):
        self.main = Tk()
        self.main.title("Fibonacci Sequence")
        self.main.geometry("300x100")
        self.main.columnconfigure([0,1,2,3], weight=1)
        self.main.rowconfigure([0,1], weight=1)

        self.label = Label(self.main, text= "Input", font= ("Arial", 20))
        self.label.grid(row=1, column=0, sticky= "W")

        self.entry = Entry(self.main, width= 20)
        self.entry.grid(row=1, column= 1, columnspan=2)

        self.res_label = Label(self.main, text= "Result : ", font= "bold")
        self.res_label.grid(row=0, column=0, sticky="S")

        self.button = Button(self.main, text="Check", command= self.get)
        self.button.grid(row=1, column=4, sticky="W")


        self.main.mainloop()

    def result_(self, n):
        self.result = Label(self.main, text= n, font = ("bold",20))
        self.result.grid(row=0, columnspan=3, sticky= "S")

    def get(self):
        num = self.entry.get()
        if num.isdigit():
            self.fibo_(int(num))


    def fibo_(self, n):
        first_num = 0
        second_num = 1
        for count in range(n):
            fibo = first_num + second_num

            if (n == first_num) or (n == second_num) or (n == fibo):
                return self.result_("True")

            elif fibo <=n:
                first_num , second_num = second_num, first_num + second_num
            else:
                return self.result_("False")

call = fibonacci()


