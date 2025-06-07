from tkinter import *
import wikipedia
import random as rn
from tkinter.messagebox import *


class wikipedia_article:

    artic = ""
    def __init__(self):
        self.main = Tk()
        self.main.title("Wiki article")
        self.main.geometry("300x200")
        self.main.columnconfigure([0,1,2], weight= 1)
        self.main.rowconfigure([0,1,2], weight=1)
        self.label = Label(self.main, text= "", font="Arial 15")
        self.choose_article()
        self.main.mainloop()

    def choose_article(self):
        global artic
        lst = ["java programming","python programming","Abraham Lincon", "islamic","Gold","take off (rapper)", "Martin luther king", "Covid-19", "Guido van Rossum"]
        art = rn.choice(lst)
        self.label.config(text="did you want to read\nabout  : " + art)
        self.label.grid(row=0, columnspan=3, sticky="S")
        self.artic = art
        self.bt1 = Button(self.main, text="Yes", command= self.get_article, font= "bold 15")
        self.bt1.grid(row=1, column=0, columnspan=2)
        self.bt2 = Button(self.main, text="No", command= self.choose_article, font = "bold 15")
        self.bt2.grid(row=1, column=2, sticky= "W")
        self.bt3 = Button(self.main, text= "Quit", command= self.main.destroy, font= "bold 15")
        self.bt3.grid(row=2, columnspan=3, sticky="N")



    def get_article(self):
        global artic
        try:
            self.article = wikipedia.summary(self.artic)
            pharagrah = self.article.split("\n")
            self.new_window(pharagrah, self.artic)
        except:
            showinfo("Connection", "No Internet\nConnection")


    def new_window(self, pharagrah, title):
        lst = [i for i in range(len(pharagrah)+2)]
        self.new = Toplevel(self.main)
        self.new.title(title)
        self.new.rowconfigure(lst, weight=1)
        self.article_name = Label(self.new, text= title, font= "Arial 20")
        self.article_name.grid(row=0, columnspan=3)

        for para, row in zip(pharagrah, lst):
            if len(para) <5:
                continue
            self.window_label = Label(self.new, text= self.lines(para), font= "bold")
            self.window_label.grid(row= row+1, column=0)
        self.ending = Label(self.new, text= "\narticle by abdulrahmon", font="Times 12")
        self.ending.grid(row= len(lst) +1 )


    def lines(self, line):
        new_line= ''
        count = 0
        for i in line:
            count += 1
            new_line += i
            if count > 70 and i == ' ':
                new_line += '\n'
                count = 0
        return new_line


call = wikipedia_article()