from tkinter import *

window = Tk()
window.title("Python Website Blocker")
window.geometry("450x102")
window.rowconfigure([0, 1, 2, 3], weight=0)
window.columnconfigure([0, 1, 2], weight=0)
window.resizable(width=False, height=False)
window.grid_propagate(0)

devicesFrame = Frame(window, width=450, relief=RAISED, borderwidth=3, height=30)
devicesFrame.rowconfigure(0, weight=0)
devicesFrame.columnconfigure([0, 1, 3], weight=1)
devicesFrame.grid_propagate(0)
devicesFrame.grid(row=0, column=0, columnspan=2)

Label(devicesFrame, text="Choose Operating system: ").grid(row=0, column=0)
device = IntVar()
device.set(0)
targetLocation = ""

winOs = Radiobutton(devicesFrame, text="Window", value=0, variable=device)
linuxOs = Radiobutton(devicesFrame, text="Linux", value=1, variable=device)
winOs.grid(row=0, column=1)
linuxOs.grid(row=0, column=2)

Label(window, text="STATUS: ", width=12).grid(row=1, column=0)
status = Label(window, text="", width=51)
status.grid(row=1, column=1)

Label(window, text="Domain Name: ", width=12).grid(row=2, column=0)
domainName = Entry(window, textvariable=StringVar())
domainName.grid(row=2, column=1, sticky="ew")

btnFrames = Frame(window, width=450, relief=RAISED, borderwidth=3, bg="red", height=30)
btnFrames.rowconfigure(0, weight=0)
btnFrames.columnconfigure([0, 1], weight=1)
btnFrames.grid_propagate(0)
btnFrames.grid(row=3, column=0, columnspan=2)


def setLocation():
    global targetLocation
    # check device
    if bool(device.get()):
        targetLocation = r"/etc/hosts"
    else:
        targetLocation = r"C:/Windows/System32/drivers/etc/hosts"
    return


def block():
    # Setting Target Location.
    global targetLocation
    setLocation()

    # check empty entry
    if domainName.get() == "":
        status.config(text="Domain name cannot be empty!")
        return

    # C:/Windows/System32/drivers/etc/hosts, I don't have permition to edit systerm file
    # So I copied the file to the same loction.
    web = domainName.get()
    ipaddress = "127.0.0.1"
    allSets = ipaddress + " " + web
    with open(targetLocation, "r+") as file:
        if allSets in file:
            status.config(text="Website Already Blocked")
        else:
            file.write("\n" + allSets)
            status.config(text="Website Blocked")


def unblock():
    # Setting Target Location.
    global targetLocation
    setLocation()

    # check empty entry
    if domainName.get() == "":
        status.config(text="Domain name cannot be empty!")
        return

    web = domainName.get()
    ipaddress = "127.0.0.1"
    allSets = ipaddress + " " + web

    with open(targetLocation, "r") as file:
        tempFile = file.readlines()

    if allSets not in tempFile:
        status.config(text="Website is not blocked")
        return

    with open(targetLocation, "w") as file:
        for line in tempFile:
            if line != allSets:
                file.write(line)
        status.config(text="Website Unblocked")


blcokBtn = Button(btnFrames, text="Block", command=block)
blcokBtn.grid(row=0, column=0, sticky="e")
unblcokBtn = Button(btnFrames, text="Unblock", command=unblock)
unblcokBtn.grid(row=0, column=1, sticky="w")

window.mainloop()
