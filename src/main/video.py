from pytube import YouTube
import os
import shutil


class Video:
    def __init__(self, link, type):
        self.link = link
        self.type = type

    def download(self):
        video = YouTube(self.link)
        download = ""
        if self.type == "video":
            download = video.streams.get_highest_resolution()
        elif self.type == "audio":
            download = video.streams.get_audio_only()
        try:
            download.download()
        except:
            print("An error has occurred while downloading the video")
        path = os.path.join(os.environ['USERPROFILE'], "Downloads")
        download_name = download.default_filename
        shutil.move(download_name, path)
