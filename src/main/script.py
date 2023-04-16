from pytube import YouTube


def download(link, type):
    video = YouTube(link)
    descarga = ""
    if type == "video":
        descarga = video.streams.get_highest_resolution()
    elif type == "audio":
        descarga = video.streams.get_audio_only()
    try:
        descarga.download()
    except:
        print("An error has occurred while downloading the video")


if __name__ == "__main__":
    link = input("Enter the link: ")
    type = input("Enter the type of download (video or audio): ")
    download(link, type)
