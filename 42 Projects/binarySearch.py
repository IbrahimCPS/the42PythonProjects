import tkinter as tk

def find(lists, lower, higher, search):
    global count
    #Check count in case of funtion re-call
    if count != 0:
        count = 0
    while lower <= higher:
        count += 1

        mid = lower + (higher - lower)//2

        if lists[mid] == search:
            return mid
        elif lists[mid] < search:
            lower = mid + 1
        else:
            higher = mid - 1
    return 0
count = 0
#find(lists, 0, , search)

def main():
    global count
    lists = [i for i in range(1, 200001)]
    entryNumber.grid()
    result = find(lists, 0, len(lists)-1, int(entryNumber.get()))

    labelIndexResults = tk.Label(master=window, text="")
    labelCountsResuts = tk.Label(master=window, text="")
    labelNumberResuts = tk.Label(master=window, text="")
    
    #Result checks!
    if result != 0:
        #Index
        labelIndexResults["text"] = str(result)
        labelIndexResults.grid(row=0, column=1, sticky="w", padx=1, pady=1, columnspan=2)

        #Count
        labelCountsResuts["text"] = str(count)
        labelCountsResuts.grid(row=1, column=1, sticky="w", padx=1, pady=1, columnspan=2)

        #Number
        labelNumberResuts["text"] = ""
        labelNumberResuts.grid(row=2, column=1, sticky="w", padx=1, pady=1, columnspan=2)
        labelNumberResuts["text"] = str(entryNumber.get())
    else:
        #Number
        labelNumberResuts["text"] = ""
        labelNumberResuts.grid(row=2, column=1, sticky="w", padx=1, pady=1, columnspan=2)
        labelNumberResuts["text"] = "Not Found!"
window = tk.Tk()
window.geometry("250x200")
window.title("""  Binary Search  """)
window.columnconfigure([0, 1, 2], weight=1, minsize=10)
window.rowconfigure([0, 1, 2, 4, 5], weight=1, minsize=10)
labelIndex = tk.Label(master=window, text="Index: ").grid(row=0, column=0, sticky="e", padx=1, pady=1)
labelCount = tk.Label(master=window, text="Count: ").grid(row=1, column=0, sticky="e", padx=1, pady=1)
labelNumber = tk.Label(master=window, text="Number: ").grid(row=2, column=0, sticky="e", padx=1, pady=1)
labelEntry = tk.Label(master=window, text="Enter number:").grid(row=4, column=0, sticky="e")
entryNumber = tk.Entry()
entryNumber.grid(row=4, column=1, columnspan=2)
submitBtn = tk.Button(fg="white", bg="black", text="Search", relief=tk.RAISED, command=main).grid(row=5, column=2)
window.mainloop()
