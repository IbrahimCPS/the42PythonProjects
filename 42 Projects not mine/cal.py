from tkinter import *
from tkinter.messagebox import *

class calculator:
    index = 0
    div = False
    def __init__(self):
        self.main = Tk()
        self.main.title("Calculator")
        self.main.geometry("350x500")
        self.main.configure(bg= "black")
        self.cal_button = StringVar()

        self.main.columnconfigure([0,1,2,3], weight=1)
        self.main.rowconfigure([0,1,2,3,4,5,6], weight=1)

        self.entry = Entry(self.main, width= 38, justify=RIGHT , bd=5, font= ("bold", 24), bg="lightyellow")
        self.entry.grid(row=0, rowspan= 2, column=0, columnspa=4)

        self.bt_mc = Button(self.main, text="MC", command= self.clear_  , width= 5, height=3 , bg="gray"  ,)
        self.bt_mc.grid(row=2, column=0)
        self.bt_div = Button(self.main, text="÷", command=lambda: self.return_("/"), width= 5, height=3 , bg="gray", font ="bold")
        self.bt_div.grid(row=2, column=1)
        self.bt_muti = Button(self.main, text="x", command=lambda: self.return_("*"), width= 5, height=3 , bg="gray", font ="bold")
        self.bt_muti.grid(row=2, column=2)
        self.bt_mplus = Button(self.main, text="del", command=self.add_data, width= 5, height=3 , bg="gray", font ="bold")
        self.bt_mplus.grid(row=2, column=3)

        self.bt7 = Button(self.main, text= "7", command= lambda:self.return_("7") , width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt7.grid(row=3, column=0)
        self.bt8= Button(self.main, text="8", command=lambda: self.return_("8"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt8.grid(row=3, column=1)
        self.bt9= Button(self.main, text="9", command=lambda: self.return_("9"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt9.grid(row=3, column=2)
        self.bt_minus = Button(self.main, text="-", command=lambda: self.return_("-"), width= 5, height=3 , bg="gray", font ="bold")
        self.bt_minus.grid(row=3, column=3)

        self.bt4= Button(self.main, text="4", command=lambda: self.return_("4"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt4.grid(row=4, column=0)
        self.bt5= Button(self.main, text="5", command=lambda: self.return_("5"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt5.grid(row=4, column=1)
        self.bt6 = Button(self.main, text="6", command=lambda: self.return_("6"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt6.grid(row=4, column=2)
        self.bt_plus = Button(self.main, text="+", command=lambda: self.return_("+"), width= 5, height=3 , bg="gray", font ="bold")
        self.bt_plus.grid(row=4, column=3)

        self.bt1 = Button(self.main, text="1", command=lambda: self.return_("1"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt1.grid(row=5, column=0)
        self.bt2= Button(self.main, text="2", command=lambda: self.return_("2"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt2.grid(row=5, column=1)
        self.bt3 = Button(self.main, text="3", command=lambda: self.return_("3"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt3.grid(row=5, column=2)


        self.bt_rem = Button(self.main, text="%", command= lambda:self.return_("%"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt_rem.grid(row=6, column=0)
        self.bt0 = Button(self.main, text="0", command=lambda: self.return_("0"), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt0.grid(row=6, column=1)
        self.bt_dot = Button(self.main, text=".", command=lambda: self.return_("."), width= 5, height=3 , bg="lightgray", font ="bold")
        self.bt_dot.grid(row=6, column=2)
        self.bt_equal = Button(self.main, text="=", command= self.get_res, width= 5, height= 7, bg="gray", font ="bold")
        self.bt_equal.grid(row=5, column=3, rowspan=2)



        self.main.mainloop()

    def return_(self, num):
        global index
        self.entry.insert(self.index, num)
        self.index += 1

    def clear_(self):
        self.entry.delete(0, END)

    def add_data(self):
        entry = self.entry.get()
        self.entry.delete(len(entry)-1)



    def get_res(self):
            global index, div
            try:
                    operator = ["*", "+", "-", "/", "%"]
                    temp = ""
                    num = []
                    entry = self.entry.get()

                    for char in entry:
                        if char.isdigit() or char == ".":
                            temp += char
                        elif char in operator:
                            if temp.isdigit():
                                num.append(float(temp))
                            else:
                                num.append(temp)
                            num.append(char)
                            temp = ""
                        else:
                            showinfo("Invalid", "non numeric\ninput")
                            num = []
                            break
                    if temp.isdigit():
                         num.append(float(temp))
                    else:
                        num = []

                    while len(num) >= 3:
                        res = self.calcu(num[0], num[1], num[2])
                        num.pop(0), num.pop(0), num.pop(0)
                        num.insert(0, res)

                    self.entry.delete(0, END)
                    self.index = len(str(num[0]))
                    if "." in entry or self.div:
                        self.entry.insert(0, num[0])
                        self.div = False
                    else:
                        self.entry.insert(0, int(num[0]))

            except:
                pass



    def calcu(self, first, operate, second):
        global div
        try:

            if operate == "/":
                self.div = True
            opr = {
               "+":lambda x, y: (x + y),
                "-":lambda x, y: (x - y),
               "/":lambda x, y: (x / y),
               "*":lambda x, y: (x * y)  ,
                "%":lambda x, y: (x%y) }
            return opr[operate](first, second)

        except ValueError:
            showinfo("invalid", "double operator")
            quit()






















































































my = calculator()