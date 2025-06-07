from tkinter import *
from PIL import ImageTk
from urllib.request import urlopen
import pytube as pt

# Setup window.
window = Tk()
window.geometry("450x350")
window.title("Youtube Video Downloader")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1, 2], weight=0)
window.columnconfigure(0, weight=0)


# Get Movie
def getMovie():
    try:
        if bool(choised.get()):

            # Search entry.
            allList = pt.Search(str(entrySaerch.get()))

            # Counting found for search but later.
            foundCount = 0

            # Customizing index for frames use.
            indexFrame = [i + 1 for i in range(len(allList.results))]
            indexFrame.insert(0, 0)
            indexFrame.pop(-1)

            # Scroll.
            scroll = Scrollbar(frameView, orient=VERTICAL, width=10)

            # Creat empty frame.
            listFrame = Listbox(
                frameView,
                width=72,
                height=18,
                yscrollcommand=scroll.set,
                bg="black"
            )
            listFrame.rowconfigure(indexFrame, weight=0)
            listFrame.columnconfigure(0, weight=0)
            listFrame.grid(row=0, column=0, sticky="snew", padx=2, pady=2)
            listFrame.grid_propagate(0)

            # Griding scroll and add command attribute.
            scroll.config(command=listFrame.yview())
            scroll.grid(row=0, column=1, sticky="sn")

            # I cut the result due to not know how to manage all result.
            # If you want to understand me well change range(5) to allList.results.
            for found in allList.results[:4]:
                foundCount += 1
                videoFrame = Frame(
                    listFrame,
                    width=424,
                    height=68,
                    bg="red"
                )
                videoFrame.rowconfigure([0, 1, 2], weight=0)
                videoFrame.columnconfigure([0, 1, 2], weight=0)
                videoFrame.grid(row=foundCount, column=0, padx=2, pady=2)
                videoFrame.grid_propagate(0)

                # getting video image.
                ulink = urlopen(found.thumbnail_url)
                image = ulink.read()
                ulink.close

                photo = ImageTk.PhotoImage(data=image)
                photoDisplay = Label(videoFrame, image=photo, width=60, height=60, relief=RAISED, borderwidth=2)
                photoDisplay.image = photo
                photoDisplay.grid(row=0, column=0, rowspan=3, padx=2, pady=2, sticky="n")

                # Vidoe title.
                videoTitle = Label(videoFrame, text=f"Name:  {found.title[:50]}...", width=50)
                videoTitle.grid(row=0, column=1, columnspan=3)

                # Video Description.
                length = found.length
                hour = int((length / 60) / 60)
                minute = int(length / 60) % 60
                second = (length % 60) % 60
                videoDes = Label(
                    videoFrame,
                    text=f"Rating:  {found.rating}, Length:  {hour:02d}:{minute:02d}:{second:02d} minutes "
                )
                videoDes.grid(row=1, column=1, columnspan=3, sticky="w")

                # Video Format.
                formats = ["144P", "360P", "720P", "1080P"]
                videoFormatSelected = StringVar()
                videoFormatSelected.set(formats[2])
                videoFormat = OptionMenu(videoFrame, videoFormatSelected, *formats)
                videoFormat.grid(row=2, column=1, sticky="e")

                def downloadByNames():
                    print(videoFormatSelected.get())

                # Download buttun.
                downloadBtn = Button(videoFrame, text="Download", relief=RAISED, command=downloadByNames)
                downloadBtn.grid(row=2, column=2, columnspan=2, sticky="e")
        else:
            # Adding Error Info.
            labelError = Label(window, text="Video Not Found!!!\nMake sure the link is valid.")
            labelError.grid(row=2, column=0, columnspan=3, sticky="new")

            # https://www.youtube.com/watch?v=i0xKsEbdCis try this video link.

            movie = pt.YouTube(entrySaerch.get())

            # Remove Error grid in case of overlap.
            labelError.grid_remove()

            frameMovie = Frame(
                window,
                height=100,
                relief=SUNKEN,
                pady=5,
                padx=5,
            )
            frameMovie.rowconfigure([0, 1, 2], weight=0)
            frameMovie.columnconfigure([0, 1], weight=1)
            frameMovie.grid(row=2, column=0, sticky="snew")

            # getting video image.
            ulink = urlopen(movie.thumbnail_url)
            image = ulink.read()
            ulink.close

            photo = ImageTk.PhotoImage(data=image)
            photoDisplay = Label(frameMovie, image=photo, width=100, height=100)
            photoDisplay.image = photo
            photoDisplay.grid(row=0, column=0, rowspan=3, sticky="w")

            movieTitle = Label(frameMovie, text=f"Name:  {movie.title}", padx=0, pady=0)
            movieTitle.grid(row=0, column=1, sticky="w")

            movieDes = Label(
                frameMovie,
                text=f"Author:  {movie.author}, Rating:  {movie.rating}, Length:  {movie.length}seconds"
            )
            movieDes.grid(row=1, column=1, sticky="w")

            # Download.
            def downloadByLink():
                stream.download("./")
                btnDownload.configure(text="Downloading...")

            stream = movie.streams.first()
            formats = stream.mime_type.split("/")
            btnDownload = Button(frameMovie, text=f"Download {formats[1]}", command=downloadByLink)
            btnDownload.grid(row=2, column=1, sticky="ew")
    except:
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
# Head.
labelSearch = Label(
    frameTop,
    text="Name:",
    width=10
)
labelSearch.grid(row=0, column=0)
entrySaerch = Entry(
    frameTop,
    textvariable=StringVar(),
    relief=SUNKEN,
    borderwidth=0,
    width=50
)
entrySaerch.grid(row=0, column=1, padx=5, pady=5)
btnSearch = Button(
    frameTop,
    text="Search",
    width=7,
    command=getMovie
)
btnSearch.grid(row=0, column=2)

# Second window frame.
choiseFrame = Frame(
    window,
    width=450,
    height=25,
    bg="green"
)
choiseFrame.rowconfigure(0, weight=1)
choiseFrame.columnconfigure([0, 1], weight=1)
choiseFrame.grid(row=1, column=0, sticky="snew")
choiseFrame.grid_propagate(0)

# Third window frame.
frameView = Frame(
    window,
    width=450,
    height=300,
    bg="purple"
)
frameView.grid(row=2, column=0, sticky="snew")
frameView.rowconfigure(0, weight=0)
frameView.columnconfigure([0, 1], weight=0)
frameView.grid_propagate(0)


def choiseSerch():
    if bool(choised.get()):
        labelSearch.configure(text="Name:")
    else:
        labelSearch.configure(text="Link:")


choised = IntVar()
choised.set(0)
nameRadioButton = Radiobutton(
    choiseFrame,
    text="By Name",
    variable=choised,
    value=1,
    command=choiseSerch
)
nameRadioButton.select()
nameRadioButton.grid(row=0, column=0, sticky="e")

linkRadiobutton = Radiobutton(
    choiseFrame,
    text="By Link",
    variable=choised,
    value=0,
    command=choiseSerch
)
linkRadiobutton.grid(row=0, column=1, sticky="w")

window.mainloop()
