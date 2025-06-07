import tkinter as tk
import tkinter.messagebox as tm

class email_slicer:
	

	def __init__(self):
		self.main_window = tk.Tk()
		self.main_window.title("Email Slicer")
		self.main_window.geometry("300x400")
		
		self.value = tk.StringVar()
		self.light = tk.Radiobutton(self.main_window, text="light", variable=self.value, value="Light", command=self.mood)
		self.light.grid(row=0, column=2)
		self.dark = tk.Radiobutton(self.main_window, text="dark", variable=self.value, value= "Dark", command=self.mood)
		self.dark.grid(row=0, column=3)			

		self.user_value = tk.StringVar()
		self.domain_value = tk.StringVar()
		
		self.email_label = tk.Label(self.main_window, text="Email")
		self.email_label.grid(row=3, column=0, padx=5, pady=5)
		
		self.email_entry = tk.Entry(self.main_window)
		self.email_entry.grid(row=3, column=1, pady=5, columnspan=5)

		self.user_label = tk.Label(self.main_window, text="Username :  ", bg="gray")
		self.user_label.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
		
		self.user_ans = tk.Label(self.main_window, textvariable=self.user_value)
		self.user_ans.grid(row=4, column=1, padx=5, pady=5, columnspan=3)

		self.domain_label = tk.Label(self.main_window, text="Domain :  ", bg="gray")
		self.domain_label.grid(row=5, column=0, padx=5, pady=5)

		self.domain_ans = tk.Label(self.main_window, textvariable=self.domain_value)
		self.domain_ans.grid(row=5, column=1, padx=5, pady=5, columnspan=3)

		self.slice_button = tk.Button(self.main_window, text="Slice" , command = self.get_slice)
		self.slice_button.grid(row=6, column=2, padx=5, pady=5)

		self.quit_button = tk.Button(self.main_window, text="Quit", command = self.main_window.destroy)
		self.quit_button.grid(row=6, column=3, padx=5, pady=5)
		
		tk.mainloop()
		
	def get_slice(self):
		email = self.email_entry.get()
		if "@" in email:
			username = email[ :email.index("@")]
			domain = email[(email.index("@")+1): ]
			
			self.user_value.set(username.upper())
			self.domain_value.set(domain.upper())
		else:
			tm.showinfo("recheck", "Invalid Email Address")
			
	def  mood(self):
			tm.showinfo(str(self.value.get())+" mood", "You're in "+self.value.get()+" mood")
			if self.value.get() == "Dark":
				self.main_window.config(bg="black")
			else:
				self.main_window.config(bg="lightgray")
	

		
get = email_slicer()





	
