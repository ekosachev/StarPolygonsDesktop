# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1083, 970)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(400, 16777215))
        self.label.setPixmap(QPixmap(u"ui/spBG.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btnConstruct = QPushButton(self.centralwidget)
        self.btnConstruct.setObjectName(u"btnConstruct")
        font = QFont()
        font.setPointSize(22)
        self.btnConstruct.setFont(font)

        self.verticalLayout.addWidget(self.btnConstruct)

        self.btnTheory = QPushButton(self.centralwidget)
        self.btnTheory.setObjectName(u"btnTheory")
        self.btnTheory.setFont(font)

        self.verticalLayout.addWidget(self.btnTheory)

        self.btnExersises = QPushButton(self.centralwidget)
        self.btnExersises.setObjectName(u"btnExersises")
        self.btnExersises.setFont(font)

        self.verticalLayout.addWidget(self.btnExersises)

        self.btnExit = QPushButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setFont(font)

        self.verticalLayout.addWidget(self.btnExit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btnConstruct.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None))
        self.btnTheory.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f \u043f\u043e \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u043c \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430\u043c", None))
        self.btnExersises.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

