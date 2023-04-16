from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import shutil


class Video:
    def __init__(self, link, type):
        self.link = link
        self.type = type

    def download(self):
        video = YouTube(self.link)
        descarga = ""
        if self.type == "video":
            descarga = video.streams.get_highest_resolution()
        elif self.type == "audio":
            descarga = video.streams.get_audio_only()
        try:
            descarga.download()
        except:
            print("An error has occurred while downloading the video")

        path = os.path.join(os.environ['USERPROFILE'], "Downloads")
        shutil.move(descarga, path)


if __name__ == "__main__":
    link = input("Enter the link: ")
    type = input("Enter the type of download (video or audio): ")
    Video.download(link, type)
