#!usr/bin/python3
# -*- coding: utf-8 -*-

from pytube import YouTube
import os

def main():
    # input of the URl form the user
    url = input("Add url of the YT video: ")

    try:
        yt = YouTube(url)
    except:
        print("Unvalid video URL")
        return None

    # creating 'Downloads' file
    path = os.getcwd()
    print(path)
    path = os.path.join(path, 'Downloads')
    os.makedirs(path, exist_ok=True)

    video = yt.streams
    all_video = video
    video = video.filter(progressive=True, res='720p')

    # choosing first option
    video = video.first()
    if video is None:
        video = all_video.filter(progressive=True)
        video = video.first()



    # download video
    print(f'Final video: {video}')
    video.download(path)


if __name__ == "__main__":
    main()