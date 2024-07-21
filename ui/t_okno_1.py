# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_okno_1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,   QMetaObject,  QSize,   Qt)
from PySide6.QtGui import (  QFont,     QPixmap  )
from PySide6.QtWidgets import ( QGridLayout, QHBoxLayout, QLabel,
    QPushButton,  QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 777)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(180, 167, 214);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(2000, 150))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/theeeory.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 100))
        self.pushButton_2.setMaximumSize(QSize(100, 100))
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(u"image: url(:/newPrefix/bytton.png);")
        self.pushButton_2.setFlat(False)

        def test(self):
            print('pressed')


        self.horizontalLayout_11.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/Group 7.png);")

        self.horizontalLayout_11.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a - {n / m} - \u044d\u0442\u043e \u0444\u043e\u0440\u043c\u0430, \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u043f\u0443\u0442\u0451\u043c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0432\u0435\u0440\u0448\u0438\u043d \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0433\u043e n - \u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430 \u0447\u0435\u0440\u0435\u0437 m \u043f\u0443\u0441\u0442\u044b\u0445 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439", None))
        self.label_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f: n - \u0432\u0435\u0440\u0448\u0438\u043d\u0430, m - \u0448\u0430\u0433, \u0437\u043c - \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a, \u0441 - \u0441\u0432\u044f\u0437\u043d\u044b\u0439 \u0437\u043c, \u043d\u0441 - \u043d\u0435\u0441\u0432\u044f\u0437\u043d\u044b\u0439 \u0437\u043c", None))
    # retranslateUi

