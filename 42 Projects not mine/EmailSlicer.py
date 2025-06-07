# Email slicer project 7 out of 42
import tkinter
import tkinter.messagebox
import re
class Email:
    form= r'[\w][\w\d\D\W]+@[\w\.]+'
    def __init__(self):
        self.body= tkinter.Tk()
        self.header=tkinter.Label(self.body,text="Email Slicer: ")
        self.header1=tkinter.Label(self.body,text="By Francis")
        self.header.pack()
        self.header1.pack()
        self.frame1=tkinter.Frame(self.body)
        self.frame2=tkinter.Frame(self.body)
        self.label=tkinter.Label(self.frame1,text="Enter email: ")
        self.enter=tkinter.Entry(self.frame1,width=10)
        self.label.pack(side="left")
        self.enter.pack(side="left")
        self.btn1= tkinter.Button(self.frame2,text="Slice",command=self.slice)
        self.btn2=tkinter.Button(self.frame2,text="Exit",command=self.body.destroy)
        self.btn1.pack(side="left")
        self.btn2.pack(side="left")
        
        self.frame1.pack()
        self.frame2.pack()
        
        tkinter.mainloop()
    def slice(self):
            divide=self.enter.get()
            if re.search(self.form,divide)==None:
                tkinter.messagebox.showinfo("Results","That's not a valid email")
            else:
                email1= re.search(self.form,divide).group()
                email2= email1.split("@")
                tkinter.messagebox.showinfo("Silced","Username: {0} \n Domain: @{1}".format(email2[0],
                email2[1],))
        
        
output= Email()        
        