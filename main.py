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
    
if __name__ == '__main__':
    playlists = []
    number_of_playlists = int(input("How many playlists you want to download: "))
    for i in range(number_of_playlists):
        playlist = input("Enter the Youtube URL of playlist: ")
        playlists.append(playlist)
    video_urls = get_urls_from_playlist(playlists)
    main(video_urls)