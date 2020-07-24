from __future__ import unicode_literals
import re
import mutagen
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDir
from mutagen.easyid3 import EasyID3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(520, 440)
        MainWindow.setWindowIcon(QIcon("youtube.png"))
        MainWindow.setStyleSheet("background-color: rgb(251, 251, 251);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Picture = QtWidgets.QLabel(self.centralwidget)
        self.Picture.setGeometry(QtCore.QRect(10, 11, 65, 60))
        self.Picture.setPixmap(QtGui.QPixmap("youtube.png"))
        self.Picture.setScaledContents(True)
        self.Picture.setAlignment(QtCore.Qt.AlignCenter)
        self.Picture.setWordWrap(False)
        self.Picture.setObjectName("Picture")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(10, 395, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(12)
        self.convertButton.setFont(font)
        self.convertButton.setStyleSheet("QPushButton:hover:!pressed\n"
                                         "{\n"
                                         "    background-color: #3e84c0;\n"
                                         "}\n"
                                         "QPushButton{\n"
                                         "    font-family: Arial, sans-serif;\n"
                                         "    font-weight: 100;\n"
                                         "    color: white;\n"
                                         "    background-color: #458BC6;\n"
                                         "    border: 1px solid #458BC6;\n"
                                         "    border-radius: 4px;\n"
                                         "    padding: 4px;\n"
                                         "}")
        self.convertButton.setObjectName("convertButton")
        self.optionalLabel = QtWidgets.QLabel(self.centralwidget)
        self.optionalLabel.setGeometry(QtCore.QRect(69, 156, 78, 26))
        font = QtGui.QFont()
        font.setFamily("Nunito-Light")
        font.setPointSize(14)
        self.optionalLabel.setFont(font)
        self.optionalLabel.setStyleSheet("QLabel\n"
                                         "{\n"
                                         "    font-family: \'Nunito-Light\';\n"
                                         "    color: #333333\n"
                                         "}")
        self.optionalLabel.setObjectName("optionalLabel")
        self.titleInput = QtWidgets.QLineEdit(self.centralwidget)
        self.titleInput.setGeometry(QtCore.QRect(10, 190, 455, 30))
        self.titleInput.setStyleSheet("QLineEdit{\n"
                                      "    border: 1px solid #458BC6;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 4px;\n"
                                      "    font-family: Arial, sans-serif;\n"
                                      "    font-weight: 100;\n"
                                      "    border-color: #F44336;\n"
                                      "}")
        self.titleInput.setObjectName("titleInput")
        self.optionalLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.optionalLabel_2.setGeometry(QtCore.QRect(86, 239, 78, 26))
        font = QtGui.QFont()
        font.setFamily("Nunito-Light")
        font.setPointSize(14)
        self.optionalLabel_2.setFont(font)
        self.optionalLabel_2.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "    font-family: \'Nunito-Light\';\n"
                                           "    color: #333333\n"
                                           "}")
        self.optionalLabel_2.setObjectName("optionalLabel_2")
        self.artistLabel = QtWidgets.QLabel(self.centralwidget)
        self.artistLabel.setGeometry(QtCore.QRect(10, 233, 68, 37))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(20)
        self.artistLabel.setFont(font)
        self.artistLabel.setStyleSheet("QLabel\n"
                                       "{\n"
                                       "    font-family: \'Nunito\';\n"
                                       "}")
        self.artistLabel.setObjectName("artistLabel")
        self.artistInput = QtWidgets.QLineEdit(self.centralwidget)
        self.artistInput.setGeometry(QtCore.QRect(10, 270, 455, 30))
        self.artistInput.setStyleSheet("QLineEdit{\n"
                                       "    border: 1px solid #458BC6;\n"
                                       "    border-radius: 4px;\n"
                                       "    padding: 4px;\n"
                                       "    font-family: Arial, sans-serif;\n"
                                       "    font-weight: 100;\n"
                                       "    border-color: #F44336;\n"
                                       "}")
        self.artistInput.setObjectName("artistInput")
        self.optionalLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.optionalLabel_3.setGeometry(QtCore.QRect(98, 316, 78, 26))
        font = QtGui.QFont()
        font.setFamily("Nunito-Light")
        font.setPointSize(14)
        self.optionalLabel_3.setFont(font)
        self.optionalLabel_3.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "    font-family: \'Nunito-Light\';\n"
                                           "    color: #333333\n"
                                           "}")
        self.optionalLabel_3.setObjectName("optionalLabel_3")
        self.albumLabel = QtWidgets.QLabel(self.centralwidget)
        self.albumLabel.setGeometry(QtCore.QRect(10, 310, 80, 37))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(20)
        self.albumLabel.setFont(font)
        self.albumLabel.setStyleSheet("QLabel\n"
                                      "{\n"
                                      "    font-family: \'Nunito\';\n"
                                      "}")
        self.albumLabel.setObjectName("albumLabel")
        self.albumInput = QtWidgets.QLineEdit(self.centralwidget)
        self.albumInput.setGeometry(QtCore.QRect(10, 350, 455, 30))
        self.albumInput.setStyleSheet("QLineEdit{\n"
                                      "    border: 1px solid #458BC6;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 4px;\n"
                                      "    font-family: Arial, sans-serif;\n"
                                      "    font-weight: 100;\n"
                                      "    border-color: #F44336;\n"
                                      "}")
        self.albumInput.setObjectName("albumInput")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(89, 20, 340, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setStyleSheet("color: #999999;")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.downloaderLabel = QtWidgets.QLabel(self.centralwidget)
        self.downloaderLabel.setGeometry(QtCore.QRect(10, 77, 154, 37))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(20)
        self.downloaderLabel.setFont(font)
        self.downloaderLabel.setStyleSheet("QLabel\n"
                                           "{\n"
                                           "    font-family: \'Nunito\';\n"
                                           "}")
        self.downloaderLabel.setObjectName("downloaderLabel")
        self.downloaderInput = QtWidgets.QLineEdit(self.centralwidget)
        self.downloaderInput.setGeometry(QtCore.QRect(10, 116, 455, 30))
        self.downloaderInput.setStyleSheet("QLineEdit{\n"
                                           "    border: 1px solid #458BC6;\n"
                                           "    border-radius: 4px;\n"
                                           "    padding: 4px;\n"
                                           "    font-family: Arial, sans-serif;\n"
                                           "    font-weight: 100;\n"
                                           "    border-color: #F44336;\n"
                                           "}")
        self.downloaderInput.setObjectName("downloaderInput")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 150, 51, 37))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel\n"
                                      "{\n"
                                      "    font-family: \'Nunito\';\n"
                                      "}")
        self.titleLabel.setObjectName("titleLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Signals
        self.convertButton.clicked.connect(self.downloadVideoMp3)

    def retranslateUi(self, MainWindow):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.convertButton.setText(_translate("MainWindow", "CONVERT TO .MP3"))
        self.optionalLabel.setText(_translate("MainWindow", "(optional)"))
        self.titleInput.setPlaceholderText(_translate("MainWindow", "Enter title"))
        self.optionalLabel_2.setText(_translate("MainWindow", "(optional)"))
        self.artistLabel.setText(_translate("MainWindow", "Artist"))
        self.artistInput.setPlaceholderText(_translate("MainWindow", "Enter artist"))
        self.optionalLabel_3.setText(_translate("MainWindow", "(optional)"))
        self.albumLabel.setText(_translate("MainWindow", "Album"))
        self.albumInput.setPlaceholderText(_translate("MainWindow", "Enter album"))
        self.Title.setText(_translate("MainWindow", "Youtube Downloader"))
        self.downloaderLabel.setText(_translate("MainWindow", "Youtube link"))
        self.downloaderInput.setPlaceholderText(_translate("MainWindow", "Enter URL"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.downloaderInput.setFont(font)
        self.titleInput.setFont(font)
        self.albumInput.setFont(font)
        self.artistInput.setFont(font)

    def downloadVideoMp3(self):
        try:
            if self.downloaderInput.text().strip() != "":
                url = self.downloaderInput.text().strip()
                SAVE_PATH = str(QFileDialog.getExistingDirectory(None, "Select folder", QDir.homePath()))
                if SAVE_PATH != "":
                    info = youtube_dl.YoutubeDL({'quit': True}).extract_info(url, download=False)
                    info['title'] = re.sub("[\\\/\:\*\?\"\<\>\|\.]", '', info['title'])
                    fullPathForMetaData = f"{SAVE_PATH}/{info['title']}.mp3"
                    fullPath = SAVE_PATH + "/" + info['title'] + ".%(ext)s"
                    ydl_opts = {
                        'writethumbnail': True,
                        'format': 'bestaudio/best',
                        'extractaudio': True,
                        'audioformat': 'mp3',
                        'outtmpl': fullPath,
                        'noplaylist': True,
                        'nocheckcertificate': True,
                        'quit': True,
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192'},
                            {'key': 'EmbedThumbnail'}]
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        QApplication.processEvents()
                        ydl.download([url])
                    try:
                        tag = EasyID3(fullPathForMetaData)
                    except:
                        tag = mutagen.File(fullPathForMetaData, easy=True)
                        tag.add_tags()
                    tag['artist'] = self.artistInput.text()
                    tag['title'] = self.titleInput.text()
                    tag['album'] = self.albumInput.text()
                    tag.save(v2_version=3)
                    self.downloaderInput.setText("")
                    self.artistInput.setText("")
                    self.titleInput.setText("")
                    self.albumInput.setText("")
                    msgBox = QMessageBox(MainWindow)
                    msgBox.setWindowTitle("Download")
                    msgBox.setText("Downloading is complete!")
                    msgBox.exec_()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("An error has occured")
            msgBox.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
