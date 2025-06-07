import praw
import praw.exceptions
import time
from tkinter import *
from tkinter.messagebox import *

class main:
    reddit = None
    def __init__(self):
        self.root = Tk()
        self.root.title('Reddit bot')
        self.root.geometry('340x300')
        self.root.columnconfigure([0,1,2],weight=1)
        self.root.rowconfigure([0,1,2,3,4,5],weight=1)
        self.root.resizable(width=False,height=False)
        id=StringVar(); secret=StringVar(); username=StringVar(); passwd=StringVar()

        self.id_label = Label(self.root, text="ID")
        self.id_label.grid(row=1, column=0, sticky="S")
        self.id = Entry(self.root, width=20,textvariable=id,font="Arial 15")
        self.id.grid(row=1, column=1, columnspan=2, sticky="WS")

        self.secret_label = Label(self.root, text="Secret ID")
        self.secret_label.grid(row=2, column=0, sticky="S")
        self.secret_id = Entry(self.root, width=20, textvariable=secret,font="Arial 15")
        self.secret_id.grid(row=2, column=1, columnspan=2, sticky="WS")

        self.un_label = Label(self.root, text="UserName")
        self.un_label.grid(row=3, column=0, sticky="S")
        self.username = Entry(self.root, width=20, textvariable=username, font="Arial 15")
        self.username.grid(row=3, column=1, columnspan=2, sticky="WS")

        self.pw_label = Label(self.root, text="PassWord")
        self.pw_label.grid(row=4, column=0, sticky="S")
        self.passwd = Entry(self.root, width=20, textvariable=passwd, font="Arial 15")
        self.passwd.grid(row=4, column=1, columnspan=2, sticky="WS")

        def user_entry(ID= id, SC=secret, UN=username, PW=passwd):
            try:
                r = praw.Reddit(
                    client_id=ID.get(),
                    client_secret=SC.get(),
                    username=UN.get(),
                    password=PW.get(),
                    user_agent='monitor by /u/Abdulrahmon'
                )
                if (not r.read_only):
                    global reddit
                    self.reddit = r
                    time.sleep(2)
                    self.clear()
                    self.get_search()
            except:
                showerror("Connnection", "login error\nOr\nConnection error")
        self.bt = Button(self.root, text='Login', command=user_entry)
        self.bt.grid(row=5, columnspan=3)
        self.root.mainloop()

    def clear(self):
        list = self.root.grid_slaves()
        for l in list:
            l.destroy()

    def get_search(self, text=''):
          if (len(text) > 0):
              new = Toplevel(self.root)
              new.title("Search specify")
              new.geometry("340x300")
              root = new
          else:
              root = self.root

          user_entry = StringVar()
          self.lb = Label(root, text="Search for specify reddit",font="Arial 15")
          self.lb.grid(row=0,rowspan=2,columnspan=3 ,sticky="WENS")
          self.entry = Entry(root, width=25,textvariable=user_entry,font="Times 20")
          self.entry.grid(row=2, sticky="N", columnspan=3,rowspan=2)

          def get_input(search=user_entry):
              if (len(user_entry.get()) > 0):
                  self.show_result(user_entry)

          self.Search = Button(root, text='Search',command=get_input)
          self.Search.grid(row=4, columnspan=3, sticky="N")
          if (self.reddit == None):
              main()

          if (len(text) > 0):
             new.mainloop()

    def get(self):
        self.clear()
        top = "new window"
        self.get_search(text=top)

    def show_result(self, search):
        try:
            self.root.title('Double Tap')
            self.clear()
            lst= [i.display_name for i in self.reddit.subreddits.search(search.get(),limit=100)]
            first = Frame(self.root).pack(side=BOTTOM)
            second = Frame(self.root).pack(side=TOP)

            s = Button(self.root, text="Search another", command=self.get, font='bold 5').pack()
            lb = Label(self.root, text=str(len(lst)) +" Result found", font="bold 15").pack()

            listbox = Listbox(first, width=29, font=('Arial 15'))
            listbox.pack(side=LEFT, fill=BOTH)
            scrollbar = Scrollbar(first, orient='vertical')
            scrollbar.pack(side=RIGHT, fill=BOTH)

            for values in lst:
               listbox.insert(END, ' '+ values)

            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            def get_index(event):
                clicked = lst[list(listbox.curselection())[0]]
                self.check_clicked(clicked)

            listbox.bind('<Double-1>', get_index)
        except:
            showerror("Error occur", "login error \nOr\nConnection error")
            self.clear()
            self.get_search()

    def word_(self, text):
       new = '';count = 0
       for ch in text:
           count += 1; new += ch
           if (count >= 15) and (ch == " "):
               new += '\n';count = 0
       new += '\n';new += "_"*18
       return new


    def check_clicked(self, clicked):
        new = Toplevel()
        new.title(clicked + " Subreddits")
        new.geometry("340x300")
        note = ''

        for i in self.reddit.subreddit(clicked).hot(limit=100):
               note += self.word_(i.title)
               note += '\n\n'
        v = Scrollbar(new, orient='vertical')
        v.pack(side=RIGHT, fill=BOTH)

        body = Text(new, relief=RAISED, yscrollcommand=v.set, font="bold 15")
        body.pack(side=LEFT, fill=BOTH)
        v.config(command=body.yview)
        body.insert(END, note)


main()