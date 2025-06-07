import tkinter as tk

def slice():
    entryE.grid()
    email = entryE.get()
    
    if "@" not in email or "." not in email:
        labelRr["text"] = "email is invalid!"
        return
    
    at = 0
    for i in email:
        if i == "@":
            at += 1
            
    if at > 1:
        labelRr["text"] = "Single @ is require!"
        return
    
        
    cuts = email.split("@")
    labelRr["text"] = f"Username: {cuts[0]}.\nDomain-name: {cuts[1]}."
    
window = tk.Tk()

window.columnconfigure([0, 1, 3], minsize=20, weight=1)
window.rowconfigure([0, 1], minsize=30, weight=1)

labelE = tk.Label(master=window, text="Emails Add: ").grid(row=0, column=0, sticky="e")

entryE = tk.Entry(master=window, text="", width=50)
entryE.grid(row=0, column=1)

labelR = tk.Label(master=window, text="Results: ").grid(row=1, column=0, sticky="e")
labelRr = tk.Label()

btnE= tk.Button(master=window, text="Slice", command=slice).grid(row=0, column=3, sticky="w")
labelRr.grid(row=1, column=1, sticky="w")

window.mainloop()
