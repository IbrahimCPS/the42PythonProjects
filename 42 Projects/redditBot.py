from urllib.request import urlopen
from tkinter import *
from tkinter import messagebox
import praw

# SETUP WINDOW..
window = Tk()
window.title("Reddit Bot!")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1, 2, 3], weight=0)
window.columnconfigure([0, 1, 2, 3], weight=0)

# NETWORK STATUS INFORMATION.
Label(window, text="NETWORK: ").grid(row=3, column=0)
networkStatusTextLabel = Label(window, text="")
networkStatusTextLabel.grid(row=3, column=1, sticky="w")


# CHECK NETWORK STATUS.
def networkStatus():
    host = "https://www.google.ng"
    try:
        urlopen(host)
        networkStatusTextLabel.config(text="Connected")
        return True
    except:
        networkStatusTextLabel.config(text="Disconnected")
        messagebox.showerror("Network Connection Error!", "Please Check your Internet!!!")
        return False


# FOR DO NOT CLOSE ON NEW WINDOW PROTOCOL.
def closeNo():
    pass


# FOR DO CLOSE ON NEW WINDOW PROTOCOL.
def closeYes():
    window.destroy()
    pass


# REDDIT INITIALLIZATION AND CONTENT LINE 43 TO 71.
# READ-ONLY INSTANCE.
redditReadOnly = praw.Reddit(
    client_id="JwxPWmj8DQcR22DcrPEBEA",
    client_secret="52ycD25HAm3enbgBGH6wLhOuBDB3Vg",
    user_agent="myBot22"
)

# REDDITS POST DICS FOR ALL.
redditPostDict = {
    "Title": [],
    "Post Text": [],
    "ID": [],
    "Score": [],
    "Total Comments": [],
    "Post URL": []
}

# REDDITS SAVED POST DICS FOR ALL.
redditSavedPostDict = {
    "Title": [],
    "Post Text": [],
    "ID": [],
    "Score": [],
    "Total Comments": [],
    "Post URL": []
}
foundedRedditCount = 0
saveRedditCount = 0
redditSearchKeyword = ""

# CHECK NETWORK.
networkStatus()


# GETTING SELECTED ITEM AND IT'S INDEX.
# IF X == 0 # NOT SAVE INIT.
# IF X == 1 # SAVE INIT.
def getSelected():
    index = redditList.curselection()
    selected = redditList.get(index)
    return int(index[0]), selected


# DISPLAYING REDDITS.
# IF X == 0 # NOT SAVE INIT.
# IF X == 1 # SAVE INIT.
def displayReddit(x):
    # INITIALLISING POST FOR SCRAPING.
    if x == 0:
        index, postShort = getSelected()
        title = redditPostDict["Title"][index]
        postText = redditPostDict["Post Text"][index]
        uniqueId = index
        score = redditPostDict["Score"][index]
        totalComments = redditPostDict["Total Comments"][index]
        postLink = redditPostDict["Post URL"][index]
    else:
        index, postShort = getSelected()
        title = redditPostDict["Title"][index]
        postText = redditPostDict["Post Text"][index]
        uniqueId = index
        score = redditPostDict["Score"][index]
        totalComments = redditPostDict["Total Comments"][index]
        postLink = redditPostDict["Post URL"][index]

    # DISABLE BACK FRAMES FUNCTIONS FOR !DO NOT PRESS AGAIN.
    getSearchBtn.config(state=DISABLED)
    clearBtn.config(state=DISABLED)
    redditList.config(state=DISABLED)
    newPostBtn.config(state=DISABLED)
    oldPostBtn.config(state=DISABLED)
    viewSavedBtn.config(state=DISABLED)

    # DISABLE CLOSE WINDOWS BUTTON.
    window.protocol("WM_DELETE_WINDOW", closeNo)

    # SETUP WINDOW..
    win = Tk()
    win.title(postShort)
    win.resizable(width=False, height=False)
    win.rowconfigure([0, 1, 2, 3], weight=1)
    win.columnconfigure([0, 1, 2, 3, 4], weight=1)
    win.attributes("-topmost", True)

    # CONTROLLING CLOSE KEY BETWEEN TWO WINDOWS, window and win.
    def controlClose():
        # ENABLE BUTTON TO NORMAL.
        getSearchBtn.config(state=NORMAL)
        clearBtn.config(state=NORMAL)
        redditList.config(state=NORMAL)
        newPostBtn.config(state=NORMAL)
        oldPostBtn.config(state=NORMAL)
        viewSavedBtn.config(state=NORMAL)

        window.protocol("WM_DELETE_WINDOW", closeYes)
        win.destroy()
        pass

    win.protocol("WM_DELETE_WINDOW", controlClose)

    # FIRST ROW
    topFrame = Frame(win, height=20, borderwidth=3, relief=RAISED)
    topFrame.grid(row=0, column=0, columnspan=5, sticky="snew")
    topFrame.rowconfigure(0, weight=1)
    topFrame.columnconfigure(0, weight=1)
    Label(topFrame, text=postShort, justify="center").grid(row=0, column=0)

    # SECOND ROW
    for i in range(3):
        loofFrame = Frame(win, height=20, borderwidth=3, relief=RAISED)
        loofFrame.grid(row=1, column=i, sticky="snew")
        loofFrame.rowconfigure(0, weight=1)
        loofFrame.columnconfigure(0, weight=1)

        textValue = ""
        if i == 0:
            textValue = f"ID: {uniqueId}"
        elif i == 1:
            textValue = f"Score: {score}"
        elif i == 2:
            textValue = f"Comments: {totalComments}"
        Label(loofFrame, text=textValue, justify="center").grid(row=0, column=0)

    # SEE LINK.
    def seeMe():
        messagebox.showinfo("LINK...", f"LINK: {postLink}")

    # LINK BUTTON.
    Button(
        win,
        text="POST LINK",
        bg="black",
        fg="white",
        relief=RAISED,
        command=seeMe
    ).grid(row=1, column=3, columnspan=2, sticky="snew")

    # THIRD ROW.
    # POST TEXT SCROLLER.
    postTextScroller = Scrollbar(win, orient=VERTICAL, width=10)
    postTextScroller.grid(row=2, column=4, sticky="sn")

    # POST TEXT
    postTexts = Text(win, width=50, height=18, borderwidth=3, relief=RAISED, yscrollcommand=postTextScroller.set)
    postTexts.grid(row=2, column=0, columnspan=4)

    # INSERT TEXT AND SIABLE FOCUS READONLY.
    # CHECK TEXT IF EMPTY.
    if postText == "":
        postText = f"{title}\n\nNO TEXT FOUND FOR THIS POST!"
    else:
        postText = f"{title}\n\n{postText}"

    postTexts.insert(END, postText)
    postTexts.config(state=DISABLED)

    # ADDING COMMAND TO POST TEXT SCROLLBAR.
    postTextScroller.config(command=postTexts.yview)

    # SAVE POST
    def savePost():
        global saveRedditCount
        # TITLE.
        redditSavedPostDict["Title"].append(title)
        # TEXT.
        redditSavedPostDict["Post Text"].append(postText)
        # UNIQUE ID.
        redditSavedPostDict["ID"].append(saveRedditCount)
        saveRedditCount += 1
        # THE SOCORE OF THE POST.
        redditSavedPostDict["Score"].append(score)
        # TOTAL NUMBER OF COMMENTS
        redditSavedPostDict["Total Comments"].append(totalComments)
        # URL OF EACH POST
        redditSavedPostDict["Post URL"].append(postLink)

        messagebox.showinfo("SAVE POST", "SAVE POST... POST SAVED.")
        pass

    # FOUTH ROW
    saveBtn = Button(win, text="SAVE POST", relief=RAISED, command=savePost)
    saveBtn.grid(row=3, column=2)
    # DISABLE ABOVE BUTTON FOR SAVED POST
    if x != 0:
        saveBtn.config(state=DISABLED)

    Button(win, text="CLOSE", relief=RAISED, command=controlClose).grid(row=3, column=3, columnspan=2, sticky="w")

    # POST LINK MESSAGE HINT.
    messagebox.showinfo("HINT...", "CLICK POST LINK TO REVEAL THE POST LINK.")
    win.mainloop()
    pass


# GET SEARCH BY NEW OR OLD POST FUNCTION.
def getSearch(x):
    # CHECK NETWORK.
    if not networkStatus():
        return

    global foundedRedditCount

    # FOF UNKOWN SEARCH! OR NOT FOUND! OR NETWORK DISCONNECT UNEXPECTED!
    # WHEN GETTING REDDIT.
    try:
        subreddit = redditReadOnly.subreddit(redditSearchKeyword)

        if x == 1:
            # NEW POST ALL DAY, WEEK, MONTH AND YEAR.
            newPosts = subreddit.new()

            # CLEAR LIST BOX.
            redditList.delete(0, END)

            for post in newPosts:
                redditList.insert(foundedRedditCount, f"{post.title[:35]}...")
                # TITLE.
                redditPostDict["Title"].append(post.title)
                # TEXT.
                redditPostDict["Post Text"].append(post.selftext)
                # UNIQUE ID.
                redditPostDict["ID"].append(post.id)
                # THE SOCORE OF THE POST.
                redditPostDict["Score"].append(post.score)
                # TOTAL NUMBER OF COMMENTS
                redditPostDict["Total Comments"].append(post.num_comments)
                # URL OF EACH POST
                redditPostDict["Post URL"].append(post.url)

                # INCREASE COUNT.
                foundedRedditCount += 1
        else:
            # OLD POST ALL DAY, WEEK, MONTH AND YEAR.
            oldPost = subreddit.top()

            # CLEAR LIST BOX.
            redditList.delete(0, END)

            for post in oldPost:
                redditList.insert(foundedRedditCount, f"{post.title[:35]}...")
                # TITLE.
                redditPostDict["Title"].append(post.title)
                # TEXT.
                redditPostDict["Post Text"].append(post.selftext)
                # UNIQUE ID.
                redditPostDict["ID"].append(post.id)
                # THE SOCORE OF THE POST.
                redditPostDict["Score"].append(post.score)
                # TOTAL NUMBER OF COMMENTS
                redditPostDict["Total Comments"].append(post.num_comments)
                # URL OF EACH POST
                redditPostDict["Post URL"].append(post.url)

                # INCREASE INCREASE COUNT.
                foundedRedditCount += 1
        # ATTACHING FUNCTION ON LISTBOX DOUBLE CLICK ITEM.
        redditList.bind("<Double-1>", lambda fun: displayReddit(0))
    except:
        # CHECK NETWORK.
        if not networkStatus():
            return
        messagebox.showerror("UNKOWN SEARCH KEYWORD", "PLEASE CHANGE SEARCH KEYWORD ERROR!")
    pass


# DISPLAY SAVED REDDITS
def addSavedList():
    global foundedRedditCount

    # CLEAR LIST BOX.
    redditList.delete(0, END)
    foundedRedditCount = 0

    for post in redditSavedPostDict["Title"]:
        redditList.insert(foundedRedditCount, f"{post[:35]}...")

        # ATTACHING FUNCTION ON LISTBOX DOUBLE CLICK ITEM.
        redditList.bind("<Double-1>", lambda fun: displayReddit(1))


# FIRST ROW.
# TOP BUTTONS.
newPostBtn = Button(window, text="NEW POST", relief=RAISED, command=lambda x=1: getSearch(x), state=DISABLED)
oldPostBtn = Button(window, text="OLD POST", relief=RAISED, command=lambda x=2: getSearch(x), state=DISABLED)
newPostBtn.grid(row=0, column=0, padx=2, pady=2)
oldPostBtn.grid(row=0, column=1, padx=2, pady=2)


# GET SEARCH ENTRY FUNCTION.
def getSearchByEntry():
    # CHECK NETWORK.
    if not networkStatus():
        return

    # DISABLE BACK FRAMES FUNCTIONS FOR !DO NOT PRESS AGAIN.V1
    getSearchBtn.config(state=DISABLED)
    clearBtn.config(state=DISABLED)
    redditList.config(state=DISABLED)
    viewSavedBtn.config(state=DISABLED)

    # DISABLE BACK FRAMES FUNCTIONS FOR !DO NOT PRESS AGAIN.V2
    # CHECKING IF IT WAS CHANGE SEARCH ROUND!
    if getSearchBtn["text"] == "Change Search":
        newPostBtn.config(state=DISABLED)
        oldPostBtn.config(state=DISABLED)

    # DISABLE CLOSE WINDOWS BUTTON.
    window.protocol("WM_DELETE_WINDOW", closeNo)

    # SETUP WINDOW..
    win = Tk()
    win.title("GET SEARCH!")
    win.resizable(width=False, height=False)
    win.rowconfigure([0, 1, 2], weight=1)
    win.columnconfigure(0, weight=1)
    win.attributes("-topmost", True)

    # CONTROLLING CLOSE KEY BETWEEN TWO WINDOWS, window and win.
    def controlClose():
        # ENABLE BUTTON TO NORMAL.V1
        getSearchBtn.config(state=NORMAL)
        clearBtn.config(state=NORMAL)
        redditList.config(state=NORMAL)
        viewSavedBtn.config(state=NORMAL)

        # ENABLE BUTTON TO NORMAL.V2
        if getSearchBtn["text"] == "Change Search":
            newPostBtn.config(state=NORMAL)
            oldPostBtn.config(state=NORMAL)

        window.protocol("WM_DELETE_WINDOW", closeYes)
        win.destroy()
        pass

    win.protocol("WM_DELETE_WINDOW", controlClose)

    # LABEL.
    Label(win, text="ENTER THE SEARCH KEYWORD!").grid(row=0, column=0)

    # ENTRY SEARCH.
    entrySearch = Entry(win, textvariable=StringVar)
    entrySearch.grid(row=1, column=0, sticky="ew", padx=2, pady=2)

    # SUBMIT SEARCH FUNCTION.
    def submitSearch():
        entryData = entrySearch.get()

        # VALIDATE SEARCH NOT TO BE EMPTY.
        if entryData == "":
            messagebox.showerror("Empty Input!", "PLEASE ENTER A VALID DATA.")
            return

        # THIS FOR CHANGING SEARCH KEYWORDS!
        clearList()

        # SETTING ENTRY.
        global redditSearchKeyword
        redditSearchKeyword = entryData

        # ENABLE BACK FRAMES FUNCTIONS TO NORMAL.
        getSearchBtn.config(state=NORMAL)
        clearBtn.config(state=NORMAL)
        redditList.config(state=NORMAL)
        newPostBtn.config(state=NORMAL)
        oldPostBtn.config(state=NORMAL)
        viewSavedBtn.config(state=NORMAL)

        # CHANGE BUTTON BTN FOR USER SATISFACTION.
        getSearchBtn.config(text="Change Search")

        # MESSAGE TO USER FOR NEXT.
        messagebox.showinfo("DONE....", "CLICK NEW POST OR OLD POST BUTTON")

        # DESTROYING GET SEARCH WINDOWS.
        win.destroy()

        # ENABLE WINDOW CLOSE BUTTON.
        window.protocol("WM_DELETE_WINDOW", closeYes)
        pass

    # SUBMIT SEARCH BUTTON.
    Button(win, text="SEARCH REDDIT'S", command=submitSearch).grid(row=2, column=0)

    # MESSAGE USER AND OFFER HIM FOR RANDOM POST.
    messagebox.showinfo("HINT...", "ENTER 'random' WORD FOR RANDOM SEARCH.")
    win.mainloop()


# GET SEARCH ENTRY WINDOW ENABLE BUTTON.
getSearchBtn = Button(
    window,
    text="ENTER SEARCH",
    relief=RAISED,
    command=getSearchByEntry
)
getSearchBtn.grid(
    row=0,
    column=2,
    columnspan=2,
    padx=6,
    pady=2
)

# SECOND ROW.

# REDDIT LIST SCROLLER.
redditListScroller = Scrollbar(window, orient=VERTICAL, width=10)
redditListScroller.grid(row=1, column=3, columnspan=2, sticky="sn")

# CREATING LIST FRAME.
redditList = Listbox(
    window,
    relief=RAISED,
    width=38,
    height=18,
    yscrollcommand=redditListScroller.set
)
redditList.grid(row=1, column=0, columnspan=3)

# ADDING COMMAND TO REDDIT SCROLLBAR.
redditListScroller.config(command=redditList.yview)


# CLEAR LIST ENTRIES.
def clearList():
    # CHECK NETWORK.
    if not networkStatus():
        return

    global foundedRedditCount

    # RESETING EVERYTHINGS!
    redditPostDict["Title"] = []
    redditPostDict["Post Text"] = []
    redditPostDict["ID"] = []
    redditPostDict["Score"] = []
    redditPostDict["Total Comments"] = []
    redditPostDict["Post URL"] = []
    newPostBtn.config(state=DISABLED)
    oldPostBtn.config(state=DISABLED)
    foundedRedditCount = 0
    redditList.delete(0, END)
    getSearchBtn.config(text="ENTER SEARCH")


# CLEAR BUTTON.
clearBtn = Button(window, text="CLEAR", relief=RAISED, command=clearList)
clearBtn.grid(row=2, column=2, columnspan=2, sticky="e")

# VIEW SAVED LIST BUTTON.
viewSavedBtn = Button(window, text="VIEW SAVED REDDIT'S", command=addSavedList)
viewSavedBtn.grid(row=2, column=0, columnspan=2, sticky="w")

window.mainloop()
