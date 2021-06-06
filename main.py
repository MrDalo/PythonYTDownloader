#!usr/bin/python3
# -*- coding: utf-8 -*-

from pytube import YouTube


def main():
    # input of the URl form the user
    url = input("Add url of the YT video: ")

    try:
        yt = YouTube(url)
    except:
        print("Unvalid video URL")
        return None

    video = yt.streams
    video = video.filter(progressive=True, res='720p')
    for i in video:
        print(i)

    # choosing first option
    video = video.first()

    # download video
    # video.download()


if __name__ == "__main__":
    main()