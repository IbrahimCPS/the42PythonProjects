import io
import requests
import tkinter as tk
from pytube import YouTube
import tkinter.messagebox as tm
from PIL import Image, ImageTk





try:
	url = "https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678098-social-youtube-1024.png"
	raw_data = requests.get(url).content
	im = Image.open(io.BytesIO(raw_data), mod)
	im = im.resize((500, 500))
except:
	tm.showerror("network error", "Connection \nError!!")
	quit()


class downloader:
	
	def __init__(self):
		self.main = tk.Tk()
		self.main.title("YouTube Downloader")
		self.main.geometry("1000x1500")
		tm.showinfo("welcome", "welcome to Abdulrahmon \nYouTube Downloader\nPaste your link\nand download videos free")
		self.value = tk.StringVar()
		
		self.main.columnconfigure(0, weight=1)
		self.main.rowconfigure(0, weight= 1)
		self.main.rowconfigure(1, weight= 80)
		self.main.rowconfigure(2, weight= 19)
		
		self.top_frame= tk.Frame(self.main)
		self.middle_frame = tk.Frame(self.main)
		self.bottom_frame = tk.Frame(self.main)
		
		self.top_frame.grid(row=0, column=0, sticky="WENS")
		self.middle_frame.grid(row=1, column=0, sticky="WENS")
		self.bottom_frame.grid(row=2, column=0, sticky="WENS")
		
		self.top_label = tk.Label(self.middle_frame, font=("bold", 14), text="YouTube downloader\nCreated by Abdulrahmon")
		self.top_label.grid(row=0, column=0, columnspan=3 )
		
		self.middle_frame.columnconfigure(0, weight=1)
		self.middle_frame.columnconfigure(1, weight=1)
		self.middle_frame.columnconfigure(2, weight=1)
		
		self.middle_frame.rowconfigure(0, weight=1)
		self.middle_frame.rowconfigure(1, weight=1)
		self.middle_frame.rowconfigure(2, weight=1)
		
		self.image = ImageTk.PhotoImage(im)
		self.image_label = tk.Label(self.middle_frame , image=self.image)
		self.image_label.grid(row=1, column=0, columnspan=3)
		
		self.url_label = tk.Label(self.middle_frame , text="Link", font=("bold", 10))
		self.url_label.grid(row=2, column=0, sticky="W", padx=50)
		
		self.user_entry = tk.Entry(self.middle_frame , width=22, font=("bold", 10))
		self.user_entry.grid(row=2, column=0, columnspan=3)
		
		self.Click_label = tk.Button(self.middle_frame , text="Click", command=self.get_link , font=("bold", 6))
		self.Click_label.grid(row=2, column=0, columnspan=3,  sticky="E")
		tk.mainloop()
		
	def get_link(self):
			link = self.user_entry.get()
			if len(link) > 0:
							try:
								video = YouTube(link)
								self.user_entry.config(state="disabled")
								self.Click_label.config(state="disabled")
								self.MP4 = tk.Radiobutton(self.middle_frame, text="MP4", variable=self.value, value="A", command="", font= ("bold", 5))
								self.MPEG = tk.Radiobutton(self.middle_frame, text="MPEG", variable=self.value, value="B", command="", font= ("bold", 5))
								self.AUDIO = tk.Radiobutton(self.middle_frame, text="Audio", variable=self.value, value="C", command="", font= ("bold", 5))
								self.MP4.grid(row=2, column=0, sticky="NE")
								self.MPEG.grid(row=2, column=1, sticky="N")
								self.AUDIO.grid(row=2, column=2, sticky="NW")
								self.download= tk.Button(self.middle_frame, command=self.check_avail, text="Download", bg="lightblue", font= ("bold", 10))
								self.download.grid(row=2, column=0, columnspan=3, sticky="S")
								
							except:
								tm.showerror("Invalid link", "404 Error\nLink Not available")
								

			else:
				tm.showwarning("empty", "Enter link below")
				
	def check_avail(self):
		try:
			check = self.value.get()
			if len(check) > 0:
				if check == "A":
					yt = YouTube(self.user_entry.get())
					res = yt.streams.get_highest_resolution()
					tm.showinfo("process...", "Downloading in\n"+str(format(res.filesize /1000, '.2f'))+"mb")
					res.download("/storage/emulated/0/Download")
					tm.showinfo("successful", "Downloading Complete\nVideo saved to /Download")
					
				elif check == "B":
					yt = YouTube(self.user_entry.get())
					res = yt.streams.get_lowest_resolution()			
					tm.showinfo("process...", "Downloading in\n"+str(format(res.filesize /1000, '.2f'))+"mb")
					res.download("/storage/emulated/0/Download")
					tm.showinfo("successful", "Downloading Complete\nVideos save to /Download")
					
				else:
					yt = YouTube(self.user_entry.get())
					res = yt.streams.get_audio_only()
					tm.showinfo("process...", "Downloading in\n"+str(format(res.filesize /1000,'.2f'))+"mb")
					res.download("/storage/emulated/0/Download")
					tm.showinfo("successful", "Downloading Complete\nAudio saved to /Download")
			else:
					tm.showinfo("resolution", "Choose resolution\nMp4 , MPEG  Audio")
		except :
			tm.showerror("network", "No internet connection")
			
	
		

# https://m.youtube.com/watch?v=UPXK3AeRvKE				
				
		

				
				
				
			
			
		
me = downloader()
