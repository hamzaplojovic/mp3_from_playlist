import os
import pytube
from pytube import YouTube, Playlist

def get_urls_from_playlist(playlists):
    urls = []
    for playlist in playlists:
        playlist_urls = Playlist(playlist)
        for url in playlist_urls:
            urls.append(url)

    return urls

def main(urls):
    os.mkdir("result")
    os.chdir("result")
    for url in urls:
        name = pytube.extract.video_id(url)
        YouTube(url).streams.filter(only_audio=True).first().download(filename=name)
        os.rename(str(name), str(name)+".mp3")

def get_file_from_url(url):
    try:
        os.chdir("result")
    except FileNotFoundError:
        os.mkdir("result")
        os.chdir("result")
    name = pytube.extract.video_id(url)
    YouTube(url).streams.filter(only_audio=True).first().download(filename=name)
    os.rename(str(name), str(name)+".mp3")
    
if __name__ == '__main__':
    print("Welcome to the Youtube Downloader")
    print("Please enter the type of content you want to download")
    print("1) Playlist")
    print("2) Single Video")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("Please enter the playlist url")
        playlist_url = input()
        main(get_urls_from_playlist([playlist_url]))

    elif choice == "2":
        print("Please enter the video url")
        video_url = input()
        get_file_from_url(video_url)

    else:
        print("Please enter a valid option")
    print("Thank you for using the Youtube Downloader")

