import tkinter as tk
from pytube import Search
from pytube import YouTube as you
from pytube import Playlist as play
import tkinter.messagebox as tm


class Youtube:
    def __init__(self):
        self.num = []
        self.body = tk.Tk()
        self.Megaframe = tk.Frame(self.body)
        self.frame1 = tk.Frame(self.body)
        self.frame2 = tk.Frame(self.body)
        self.frame3 = tk.Frame(self.body)
        self.frame4 = tk.Frame(self.body)

        self.title = tk.Label(self.frame1, text="Makeshift Youtube project 9 out 42")
        self.title.pack()

        self.search = tk.Label(self.frame2, text="Search: ")
        self.enter = tk.Entry(self.frame2, width=20)
        self.search.pack(side="left")
        self.enter.pack(side="left")

        self.btn = tk.Button(self.frame3, text='SEARCH', command=self.stuff)
        self.btn.pack()

        self.video = tk.Label(self.frame4, text="Results: ")
        self.result = tk.Label(self.frame4, text="")
        self.video.pack()
        self.result.pack()

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.Megaframe.pack()

        tk.mainloop()

    def stuff(self):

        searchQuery = self.enter.get()
        s = Search(searchQuery)
        count = ["result" + str(x) for x in range(9)]
        btn = ['btn' + str(x) for x in range(9)]
        frame = ["frame" + str(x) for x in range(9)]
        check = ['check' + str(x) for x in range(4)]
        num0 = tk.IntVar()
        num0.set(-1)
        for x in range(0, 7, 2):
            z = int(x / 2)
            num = ['num' + str(x) for x in range(4)]
            frame[x] = tk.Frame(self.body)
            frame[x + 1] = tk.Frame(self.body)
            count[x] = tk.StringVar()
            count[x + 1] = tk.Label(frame[x], textvariable=count[x])
            count[x].set(s.results[int(x / 2)].title)
            check[int(x / 2)] = tk.Radiobutton(frame[x + 1], variable=num0, value=z)
            btn[x] = tk.Button(frame[x + 1], text="Download Video", command=lambda: self.res(s, num0))
            btn[x + 1] = tk.Button(frame[x + 1], text="Download Audio", command=lambda: self.audio(s, num0))
            count[x + 1].pack()
            check[int(x / 2)].pack(side="left")
            btn[x].pack(side="left")
            btn[x + 1].pack(side="left")
            frame[x].pack()
            frame[x + 1].pack()

    def download(self, aud):
        aud.download()

    def audio(self, s, num0):
        vid = s.results[num0.get()]
        aud = vid.streams.get_by_itag(139)
        frameA1 = tk.Frame(self.body)
        lbl = tk.Label(frameA1, text="Are yoy sure you want to download the audio file of {0}".format(vid.title))
        btn = tk.Button(frameA1, text="Yeah", command=lambda: self.download(aud))
        lbl.pack()
        btn.pack()
        frameA1.pack()

    def res(self, s, num0):
        vid = s.results[num0.get()]
        framed1 = tk.Frame(self.body)
        framed2 = tk.Frame(self.body)
        label = tk.Label(framed1, text="Choose resolution")
        label.pack()
        val = tk.IntVar()
        val.set(0)
        rad1 = tk.Radiobutton(framed2, text="144p", variable=val, value=1)
        rad2 = tk.Radiobutton(framed2, text='360p', variable=val, value=2)
        rad3 = tk.Radiobutton(framed2, text="720p", variable=val, value=3)
        rad4 = tk.Radiobutton(framed2, text='1080p', variable=val, value=4)
        btn = tk.Button(framed2, text='Okay', command=lambda: self.video1(val, vid))
        rad1.pack(side='left')
        rad2.pack(side='left')
        rad3.pack(side="left")
        rad4.pack(side="left")
        btn.pack()
        framed1.pack()
        framed2.pack()

    def video1(self, val, vid):
        if val.get() == 1:
            vid1 = vid.streams.filter(res='1080p', progressive=True)
            vid2 = vid.streams.get_by_itag(17)
            framed3 = tk.Frame(self.body)
            lbl = tk.Label(framed3, text="You want to download {0} in 144p?".format(vid.title))
            conf = tk.Button(framed3, text='Yes', command=vid2.download())
            lbl.pack()
            conf.pack()
            framed3.pack()

        elif val.get() == 2:
            vid1 = vid.streams.filter(res='360p', adaptive=True)
            vid2 = vid.streams.get_by_itag(18)
            framed3 = tk.Frame(self.body)
            lbl = tk.Label(framed3, text="You want to download {0} in 360p?".format(vid.title))
            conf = tk.Button(framed3, text='Yes', command=vid2.download())
            lbl.pack()
            conf.pack()
            framed3.pack()

        elif val.get() == 3:
            vid1 = vid.streams.filter(res='720p', adaptive=True)
            tm.showinfo('res', vid1)
            vid2 = vid.streams.get_by_itag(22)
            framed3 = tk.Frame(self.body)
            lbl = tk.Label(framed3, text="You want to download {0} in 720p?".format(vid.title))
            conf = tk.Button(framed3, text='Yes', command=vid2.download)
            lbl.pack()
            conf.pack()
            framed3.pack()

        if val.get() == 4:
            vid1 = vid.streams.filter(res='1080p', adaptive=True)
            vid2 = vid.streams.get_by_itag(137)
            framed3 = tk.Frame(self.body)
            lbl = tk.Label(framed3, text="You want to download {0} in 1080p?".format(vid.title))
            conf = tk.Button(framed3, text='Yes', command=vid2.download())
            lbl.pack()
            conf.pack()
            framed3.pack()


first = Youtube()
