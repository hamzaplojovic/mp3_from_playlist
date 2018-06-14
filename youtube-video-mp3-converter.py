#!/usr/bin/env python3

from pytube import YouTube
from pydub import AudioSegment
import pytube
import os

video_url = input('Enter YouTube video URL: ')

if os.name == 'nt':
    path = os.getcwd() + '\\'
else:
    path = os.getcwd() + '/'

name = pytube.extract.video_id(video_url)
YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
location = path + name + '.mp4'
AudioSegment.from_file(location).export(name + '.mp3', format="mp3")
