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

        self.label2 = Label(self.root, text="Introduce the URL", font=("Arial", 11))
        self.label2.pack()
        self.entry1 = Entry(self.root, width=40, highlightcolor="red", 
                            highlightthickness=2, font=("Roboto", 11))
        self.entry1.pack()

        self.label3 = Label(self.root, text="Introduce the download path", 
                            font=("Roboto", 11))
        self.label3.pack()
        self.boton1 = Button(self.root, text="Download path", bg="#F9E79F", 
                             padx=5, pady=5, font=("Roboto", 11))
        self.boton1.pack()

        self.boton2 = Button(self.root, text="Download", bg="#F9E79F", padx=5, pady=5,
                        font=("Roboto", 11), command=self.initialize_download)
        self.boton2.pack(pady=20)

        self.btn = RoundedButton(text="Download", radius=30, width=100, height=50,
                            btnbackground="#0078ff", btnforeground="#ffffff")
        self.btn.pack(padx=20, pady=20)

    def execute(self):
        self.root.mainloop()
    
    def initialize_download(self):
        link = self.entry1.get()
        Video(link, "video").download()
