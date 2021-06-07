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

        self.folderPath = None

        self.buttonPath.clicked.connect(self.findPath)

        self.buttonDownload.clicked.connect(self.download)



    def findPath(self):
        self.folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEditPath.setText(self.folderPath)




    def download(self):
        if self.lineEditLink.text() and self.lineEditPath.text():
            print(self.lineEditLink.text()," | ", self.lineEditPath.text())
        else:
            print("Error occurs -> Path or Link is not filled")


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