# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_okno_2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,   QMetaObject,   QSize,  Qt)
from PySide6.QtGui import (   QFont,    QPixmap )
from PySide6.QtWidgets import ( QHBoxLayout, QLabel,  QPushButton,  QVBoxLayout, QWidget)

class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 776)
        MainWindow.setStyleSheet(u"background-color: rgb(180, 167, 214);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(2000, 150))
        self.label.setPixmap(QPixmap(u":/newPrefix/theeeory.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(64)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(36)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 100))
        self.pushButton_2.setMaximumSize(QSize(100, 100))
        self.pushButton_2.setStyleSheet(u"image: url(:/newPrefix/bytton.png);")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/Group 7.png);")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0432\u044f\u0437\u043d\u043e\u0441\u0442\u044c \u0438 \u043d\u0435\u0441\u0432\u044f\u0437\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u043d\u044b\u0439 \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a - \u044d\u0442\u043e \u0442\u0430\u043a\u043e\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0441\u043e\u0431\u043e\u0439 \u0437\u0430\u043c\u043a\u043d\u0443\u0442\u044b\u0439 \u043a\u043e\u043d\u0442\u0443\u0440.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0441\u0432\u044f\u0437\u043d\u044b\u0439 \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a - \u044d\u0442\u043e \u0442\u0430\u043a\u043e\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043d\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u0432\u044f\u0437\u043d\u044b\u043c.", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

