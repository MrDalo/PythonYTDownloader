#!usr/bin/python3
# -*- coding: utf-8 -*-

from pytube import YouTube
from PyQt5 import QtWidgets
from gui import Ui_MainWindow



class Downloader(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()
        self.readyToDownload = False
        self.folderPath = None
        self.fileSize = 0
        self.yt = None
        self.progressBar.setValue(0)

        self.buttonPath.clicked.connect(self.findPath)
        self.lineEditLink.textChanged.connect(self.signalFun)

        self.buttonDownload.clicked.connect(self.download)

    def findPath(self):
        self.folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEditPath.setText(self.folderPath)



    def signalFun(self):

        url = self.lineEditLink.text()

        try:
            self.yt = YouTube(url)
            self.yt.register_on_progress_callback(self.progress_bar)
            self.readyToDownload = True
        except:
            self.labelError.setStyleSheet("color : red;")
            self.labelError.setText("Unvalid video URL")
            self.labelVideoTitle.setText('')
            self.readyToDownload = False
            return None

        #pridanie fotky a titulu
        self.labelVideoTitle.setText(self.yt.title)
        self.labelError.setStyleSheet("color : green;")
        self.labelError.setText("Video successfully found")

    def progress_bar(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        p = ((float(size) - float(bytes_remaining)) / float(size)) * float(100)
        print(str(p) + '%', bytes_remaining, ' ', size)
        self.progressBar.setValue(p)

    def download(self):
        if self.lineEditLink.text() and self.lineEditPath.text() and self.readyToDownload:
            self.labelError.setStyleSheet("color : blue;")
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
            self.labelError.setStyleSheet("color : blue;")
            self.labelError.setText(f"{self.labelError.text()}\n\n{video}")
            video.download(self.folderPath)
            self.labelError.setStyleSheet("color : green;")
            self.labelError.setText("Video is successfully download")
        else:
            self.labelError.setText("Error occurs -> Video Link or  Folder Path are not filled correctly")
