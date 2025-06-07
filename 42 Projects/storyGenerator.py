import tkinter as tk

def main():
    #setting windows.
    window = tk.Tk()
    window.title("Story Generator")
    window.rowconfigure([0, 1, 2], weight=1, minsize=10)
    window.columnconfigure([0, 1, 2], weight=1, minsize=10)
    window.resizable(width=False, height=False)

    #Saved words
    words = []
    
    #Getting User inputs.
    label = tk.Label(window, text="Enter your name: ", padx=2, pady=2)
    label.grid(row=0, column=0, sticky="ew")
    entry = tk.Entry(window)
    entry.grid(row=0, column=1, sticky="ew", padx=2, pady=2)

    #Changing question function.
    def changeAsk():
        nonlocal words
        words.append(entry.get())
        entry.delete(0, tk.END)
        if len(words) == 1:
            label.config(text="Enter your best food: ")
        elif len(words) == 2:
            label.config(text="Enter your best color: ")
        elif len(words) == 3:
            label.config(text="Enter your best video game: ")
            btn.config(text="Submit")
        else:
            btn.config(state="disabled")
            entry.config(state="disabled")
            label.config(text="STORY GENERATOR!")
            story(words[0], words[1], words[2], words[3])

    #Story
    def story(name, food, color, game):
        text=f"""
Identify
_________
My name is {name}
My best color is {color}.
My best food is {food}.

STORY
_____
{name} has a new
big house with
a {color} color.

My first time in my new
house my wife cook me a
delicious {food}.

I took my food and went out
to go and meet with my friend
at their home at where we are
playing our best game ever
named: {game}

I played well becouse i scored
more than them, but in reality
they scored me ever! because
they eated all the delicious food.
      They left empty flask \U0001F602.
"""
        story = tk.Text(window, relief=tk.RAISED, yscrollcommand=True, padx=5, pady=5, width=40, height=28)
        story.grid(row=1, column=0, columnspan=3)
        story.insert(tk.END, text)
        story.config(state="disabled")
        
    btn = tk.Button(window, text="Next", relief=tk.RAISED, borderwidth=3, command=changeAsk)
    btn.grid(row=0, column=2, sticky="ew")

    window.mainloop()
    
#Calling main
main()
