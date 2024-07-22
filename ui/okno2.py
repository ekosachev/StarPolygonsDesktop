# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_secondwindow(object):
    def setupUi(self, secondwindow):
        if not secondwindow.objectName():
            secondwindow.setObjectName(u"secondwindow")
        secondwindow.setStyleSheet(u"background-color: rgb(180, 167, 214);")
        self.centralwidget = QWidget(secondwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(700, 100))
        self.label.setMaximumSize(QSize(10000000, 100))
        self.label.setPixmap(QPixmap(u"./pictures/interestingsv/interestingsv.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(700, 400))
        self.label_2.setStyleSheet(u"background-image: url(./pictures/interestingsv/svns.png);")
        self.label_2.setPixmap(QPixmap(u"./pictures/interestingsv/svns.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 350))
        self.label_3.setPixmap(QPixmap(u"./pictures/interestingsv/theorysvnsv.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_6.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 20, 100, 100))
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setStyleSheet(u"image: url(./pictures/interestingsv/knopka1.png);")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(870, 20, 479, 115))
        self.pushButton_2.setMinimumSize(QSize(100, 115))
        self.pushButton_2.setMaximumSize(QSize(479, 16777215))
        self.pushButton_2.setStyleSheet(u"background-image: url(./pictures/interestingsv/back.png);")

        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        secondwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(secondwindow)
        self.statusbar.setObjectName(u"statusbar")
        secondwindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondwindow)

        QMetaObject.connectSlotsByName(secondwindow)
    # setupUi

    def retranslateUi(self, secondwindow):
        secondwindow.setWindowTitle(QCoreApplication.translate("secondwindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

