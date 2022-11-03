from pytube import YouTube, Playlist
import pytube
import os

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
    video_urls = get_urls_from_playlist(['https://www.youtube.com/playlist?list=PLflqtq8EOGAKIqL700Mav0jQsWAIGCVkd'])
    main(video_urls)