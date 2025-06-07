from tkinter import *
import os
from tkinter.messagebox import *



class website_blocker:

    def __init__(self):
        self.main = Tk()
        self.main.title("Website Blocker")
        self.main.geometry("300x250")

        self.main.columnconfigure([0,1,2,3], weight= 1)
        self.main.rowconfigure([0,1,2], weight= 1)

        self.value = StringVar()

        self.linux = Radiobutton(self.main, text= "Linux", value=r"/etc/hosts", variable= self.value)
        self.linux.grid(row=1, column= 0, sticky= 'WN')
        self.Window = Radiobutton(self.main, text="Window", value=r"C:/Window/System32/drivers/etc/hosts", variable=self.value)
        self.Window.grid(row=1, column= 0, sticky= 'WW')

        self.device_label = Label(self.main, text= "device")
        self.device_label.grid(row=0, columnspan=4, sticky= 'S')

        self.add_bt = Button(self.main, text= "Block", command= self.add)
        self.add_bt.grid(row=2, column=0, columnspan=2, sticky="NE")
        self.remove_bt = Button(self.main, text="UnBlock", command=self.remove)
        self.remove_bt.grid(row=2, column=2, sticky ="WN")

        self.main.mainloop()


    def entry_(self, text, function):
        self.entry = Entry(self.main, width= 20)
        self.entry.grid(row=2, columnspan= 4)
        self.button = Button(self.main, text= text , command= function)
        self.button.grid(row=2, columnspan=4, sticky= "S")


    def add(self):
        if (len(self.value.get()) > 0):
            self.entry_("Add", self.res)



    def res(self):
        path = self.value.get().lower()
        localhost = '127.0.0.1'
        website = self.entry.get()
        try:
           if (len(website) > 0):
                with open(path, "a") as host_dir:
                    host_dir.write(localhost + '      ' + website)
                    showinfo("Successful", website + " Block successfully")
        except:
           if (path == r"/etc/hosts"):
               showinfo("Device Error", "Choose Window\nYour device is Window")
           else:
               showinfo("Device Error", "Choose Linux\nYour device is LinuxOS")

    def rm(self):
        found = False
        temp = open("temp", "w")

        path = self.value.get()
        website = self.entry.get()
        try:
            if (len(website) > 0):
                with open(path, "r") as host_dir:
                    for line in host_dir:
                        line = line.rstrip("\n")
                        lst = line.split()
                        if website in lst:
                            found = True
                            continue
                        temp.write(line + "\n")
                temp.close()

                if found:
                    os.remove(path)
                    os.rename("temp", path)
                if not found:
                    showinfo("Unknow", "Website is Unknow")
        except:
           if (path == r"/etc/hosts"):
               showinfo("Device Error", "Choose Window\nYour device is Window")
           else:
               showinfo("Device Error", "Choose Linux\nYour device is LinuxOS")



        pass

    def remove(self):
        if (len(self.value.get()) > 0):
           self.entry_("remove", self.rm)


my_call = website_blocker()