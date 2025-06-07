from urllib.request import urlopen
from tkinter import *
from tkinter import messagebox
import wikipedia as wiki

# Setup window.
window = Tk()
window.geometry("450x350")
window.title("Wikipedia Search Article!")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1], weight=0)
window.columnconfigure(0, weight=0)

# Article list and article info
foundList = []
count = 0


# Getting Selection Index
def getSelectedIndex():
    for i in listFrame.curselection():
        return listFrame.get(i)


# Get Wait for Double click Function
def displaySummary():
    # Check Network Status
    networkStatus()

    # Check count
    global foundList

    page = wiki.page(getSelectedIndex())
    title = page.title
    text = page.content

    class view:
        def __init__(self):
            self.winv = Tk()
            self.winv.title(page.title)
            self.winv.geometry("600x350")
            self.winv.rowconfigure([0, 1, 2], weight=0)
            self.winv.columnconfigure(0, weight=0)
            # self.winv.resizable(width=False, height=False)

            # Heading
            Label(self.winv, text=title, justify="center").grid(row=0, column=0)

            # Body
            body = Text(self.winv, relief=RAISED, yscrollcommand=True, width=73, height=18)
            body.grid(row=1, column=0, pady=1, padx=7)
            body.insert(END, text)
            print(type(text))

            # Footer
            Button(self.winv, text="Close", command=self.destroyWinv).grid(row=2, column=0, pady=3)

            self.winv.mainloop()

        def destroyWinv(self):
            self.winv.destroy()

    start = view()


# Getting Search and make dict for the search
def getSearch():
    # Check Network Status
    networkStatus()

    # Validate Input data
    global search, count, foundList
    find = search.get()
    if find == "":
        messagebox.showerror("Unkown Input", "Pls enter a valid input")
        return

    try:
        searched = wiki.search(find)
        for i in searched:

            # Check count
            if count != 0 and count == len(foundList):
                count -= 1
            print("g", count)

            if count >= 0:
                if foundList:
                    if i in foundList:
                        continue
                    else:
                        listFrame.insert(count, i)
                        foundList.append(i)
                else:
                    listFrame.insert(count, i)
                    foundList.append(i)

            # Attaching funtion on Each selected item
            listFrame.bind("<Double-1>", lambda x: displaySummary())

            # Increase count
            count += 1
    except:
        messagebox.showerror("Unkown Error!", "Try again...")
        raise

    # First window frame.


frameTop = Frame(
    window,
    relief=SUNKEN,
    width=450,
    height=25,
    bg="red"
)
frameTop.rowconfigure(0, weight=0)
frameTop.columnconfigure([0, 1, 2], weight=0)
frameTop.grid(row=0, column=0, sticky="snew")
frameTop.grid_propagate(0)

# Second window frame.
frameDown = Frame(
    window,
    width=450,
    height=325,
    bg="purple"
)
frameDown.grid(row=1, column=0, sticky="snew")
frameDown.rowconfigure([0, 1], weight=0)
frameDown.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=0)
frameDown.grid_propagate(0)

# Scroller for Search list.
scrollListSearch = Scrollbar(frameDown, orient=VERTICAL, width=10)

# Creat empty frame.
listFrame = Listbox(
    frameDown,
    width=72,
    height=18,
    yscrollcommand=scrollListSearch.set
)
listFrame.grid(row=0, column=0, columnspan=7, sticky="snew", padx=2, pady=2)

# Griding scroll and add command attribute.
scrollListSearch.config(command=listFrame.yview)
scrollListSearch.grid(row=0, column=7, sticky="sn")

# Label Search.
Label(
    frameTop,
    text="Search:",
    width=10
).grid(row=0, column=0)

# Search entry.
search = StringVar()
Entry(
    frameTop,
    textvariable=search,
    relief=SUNKEN,
    borderwidth=0,
    width=50
).grid(row=0, column=1, padx=5, pady=5)

# Search Button.
Button(
    frameTop,
    text="Search",
    width=7,
    command=getSearch
).grid(row=0, column=2)

# Network Status.
Label(frameDown, text="Network Status: ").grid(row=1, column=0, sticky="e")
networkStatusTextLabel = Label(frameDown, text="None")
networkStatusTextLabel.grid(row=1, column=1, sticky="w")


# Check Network Status
def networkStatus():
    global networkStatusTextLabel
    host = "https://www.google.ng"
    try:
        urlopen(host)
        networkStatusTextLabel.config(text="Connected")
    except:
        messagebox.showerror("Network Connection Error!", "Please Check your Internet!!!")
        networkStatusTextLabel.config(text="Disconnected")


# Check network
networkStatus()


# clear Listbox
def clear():
    global foundList
    listFrame.delete(0, END)
    foundList = []


# Clear Button.
Button(
    frameDown,
    text="Clear",
    command=clear
).grid(row=1, column=6, columnspan=2, sticky="w")
window.mainloop()
