
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from downloader import Downloader

app = QApplication(sys.argv)

downloader = Downloader()
sys.exit(app.exec_())
