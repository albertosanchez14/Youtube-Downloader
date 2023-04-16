from tkinter import *
from src.ui.round_button import RoundButton
from src.ui.rounded_button import RoundedButton
from src.main.video import Video


class Screen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Youtube Downloader")
        self.root.iconbitmap("assets/youtube.ico")
        
        self.logo = PhotoImage(file="assets/logo.png")
        self.logo = self.logo.subsample(2, 2)

        self.label = Label(self.root, image=self.logo)
        self.label.pack(padx=40)

        self.label2 = Label(self.root, text="Please insert a valid YouTube video URL", 
                            font=("Arial", 11))
        self.label2.pack()
        self.url = Entry(self.root, width=40, highlightcolor="red", 
                            highlightthickness=2, font=("Roboto", 11))
        self.url.pack()

        self.v = StringVar()
        self.v.set(" ")
        self.radiobutton_frame = Frame(self.root)
        self.radiobutton_frame.pack(pady=10)
        self.video = Radiobutton(self.radiobutton_frame, variable=self.v,
                                text="Video", value="video", borderwidth = 10)
        self.video.grid(row=0, column=0, sticky = W)
        self.audio = Radiobutton(self.radiobutton_frame, variable=self.v,
                                text="Audio", value="audio", borderwidth = 10)
        self.audio.grid(row=0, column=1, sticky = W)

        self.download_button = Button(self.root, text="Download", bg="#F9E79F", 
                                      padx=5, pady=5,
                        font=("Roboto", 11), command=self.initialize_download)
        self.download_button.pack(pady=10)

        """self.btn = RoundedButton(text="Download", radius=30, width=100, height=50,
                            btnbackground="#0078ff", btnforeground="#ffffff")
        self.btn.pack(padx=20, pady=20)"""

    def initialize_download(self):
        link = self.url.get()
        type = self.v.get()
        Video(link, type).download()

    def execute(self):
        self.root.mainloop()
