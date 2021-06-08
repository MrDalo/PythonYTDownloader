#!usr/bin/python3
# -*- coding: utf-8 -*-

from pytube import YouTube
import os
from PyQt5 import QtWidgets, QtCore
from gui import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5.QtGui import *


class Downloader(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.readyToDownload = False
        self.folderPath = None
        self.fileSize = 0
        self.yt = None

        self.buttonPath.clicked.connect(self.findPath)
        self.lineEditLink.textChanged.connect(self.signalFun)

        self.buttonDownload.clicked.connect(self.download)



    def findPath(self):
        self.folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEditPath.setText(self.folderPath)

        #TODO dopisanie cesty rucne


    def signalFun(self):
        #TODO dorob namapovanie videa
        #namapovanie videa a zsitenie jeho dostupnosti
        url = self.lineEditLink.text()

        try:
            self.yt = YouTube(url, on_progress_callback=self.progressBar)
            self.readyToDownload = True
        except:
            self.labelError.setText("Unvalid video URL")
            self.labelVideoTitle.setText('')
            self.readyToDownload = False
            return None

        #pridanie fotky a titulu
        self.labelVideoTitle.setText(self.yt.title)
        self.labelError.setText("Video successfully found")

    def progressBar(self, chunk, bytes_remaining):
        print("I am in progressBar")

    def download(self):
        if self.lineEditLink.text() and self.lineEditPath.text() and self.readyToDownload:
            self.labelError.setText("Starting download")
            # selecting right video
            video = self.yt.streams
            all_video = video
            video = video.filter(progressive=True, res='720p')

            # choosing first option
            video = video.first()
            if video is None:
                video = all_video.filter(progressive=True)
                video = video.first()
            # downloading the video
            self.labelError.setText(f"{self.labelError.text()} \n {video}")
            video.download(self.folderPath)
        else:
            self.labelError.setText("Error occurs -> Video Link or  Folder Path are not filled correctly")


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