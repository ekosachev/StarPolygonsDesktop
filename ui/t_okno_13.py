# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_okno_13.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,   QMetaObject,   QSize,  Qt)
from PySide6.QtGui import ( QFont,   QPixmap )
from PySide6.QtWidgets import ( QHBoxLayout, QLabel,  QPushButton,  QVBoxLayout, QWidget)

class Ui_MainWindow_13(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 774)
        MainWindow.setStyleSheet(u"background-color: rgb(180, 167, 214);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(2000, 150))
        self.label.setPixmap(QPixmap(u":/newPrefix/theeeory.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/newPrefix/eleven (1).png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/newPrefix/twelwe (1).png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 100))
        self.pushButton_2.setMaximumSize(QSize(100, 100))
        self.pushButton_2.setStyleSheet(u"image: url(:/newPrefix/bytton.png);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/Group 7.png);")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0443\u0433\u043e\u043b \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u043e\u0433\u043e \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

